#!/bin/bash

# ----------
# test.sh
# ----------


GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

TARGET_TEST=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --*)
      TARGET="${1#--}"
      if [[ -z "$TARGET" ]]; then
        echo -e " ${RED}✘${NC} Invalid target flag: $1"
        exit 1
      fi
      TARGET_TEST="tests/test_${TARGET}.py"
      shift
      ;;
    *)
      echo -e " ${RED}✘${NC} Unknown option: $1"
      exit 1
      ;;
  esac
done

echo -e "${GREEN}\nSpawning Postgresql Docker Container${NC}"
docker compose -f tests/docker-compose.test.yml up --build -d

echo -e "${GREEN}\nWaiting for database to be ready...${NC}"
sleep 1
until docker exec gigavend-test-db pg_isready -U postgres -d gigavend-test > /dev/null; do
  echo "Waiting for database to be ready..."
  sleep 2
done
echo -e " ${GREEN}✔${NC} Database is ready"

# ----------
echo -e "${GREEN}\nCleaning up any existing test database${NC}"
RESULT=$(docker exec gigavend-test-db psql -U postgres -d postgres -c "DROP DATABASE IF EXISTS \"gigavend-test\";")
echo -e " ${GREEN}✔${NC} ${RESULT}"

RESULT=$(docker exec gigavend-test-db psql -U postgres -d postgres -c "CREATE DATABASE \"gigavend-test\";")
echo -e " ${GREEN}✔${NC} ${RESULT}"
# ----------
echo -e "${GREEN}\nStarting Python Virtual Environment${NC}"
source .venv/bin/activate

if [[ $(which python) == *".venv"* ]]; then
    echo -e " ${GREEN}✔${NC} Python Virtual Environment is active"
else
    echo -e " ${RED}✘${NC} Python Virtual Environment is not active"
    exit 1
fi

# ----------
echo -e "${GREEN}\nLoading Environment Variables${NC}"
set -a
source tests/.env.test
set +a
if [[ "$DB_PORT" == "5433" ]]; then
    echo -e " ${GREEN}✔${NC} Environment variables loaded"
else
    echo -e " ${RED}✘${NC} Environment variables not loaded"
    exit 1
fi
export PYTHONPATH=.

# ----------
echo -e "${GREEN}\nRunning Migrations${NC}"
alembic upgrade head

# ----------
# echo -e "${GREEN}\nPopulating Database with Test Data${NC}"
# python app/tests/populate_db_test.py

# ----------
echo -e "${GREEN}\nRunning Tests${NC}"
if [[ -n "$TARGET_TEST" ]]; then
    echo -e " ${GREEN}✔${NC} Target: $TARGET_TEST"
    pytest -v -s "$TARGET_TEST"
else
    pytest -v -s
fi

# ----------
echo -e "${GREEN}\nCleaning up any existing test database${NC}"
RESULT=$(docker exec gigavend-test-db psql -U postgres -d postgres -c "DROP DATABASE IF EXISTS \"gigavend-test\";")
echo -e " ${GREEN}✔${NC} ${RESULT}"

# ----------
echo -e "${GREEN}\nShutting down Postgresql Docker Container${NC}"
docker compose -f tests/docker-compose.test.yml down

# ----------
echo -e "${GREEN}\nStopping Python Virtual Environment${NC}"
deactivate
