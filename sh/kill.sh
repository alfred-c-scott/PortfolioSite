#!/bin/bash

# kill.sh - Stop the server and reload environment variables

ENV_FILE=".env"
PORT=8030

echo "Stopping server and reloading environment..."

# Step 1: Kill the server
echo "Stopping FastAPI server on port $PORT..."

# Find and kill ALL processes using port 8030
PIDS=$(lsof -ti:$PORT 2>/dev/null)
if [ -n "$PIDS" ]; then
    for PID in $PIDS; do
        echo "Found process $PID using port $PORT"
        kill $PID 2>/dev/null && echo "Killed process $PID"

        # Give process time to stop gracefully
        sleep 1

        # Force kill if still running
        if kill -0 $PID 2>/dev/null; then
            kill -9 $PID 2>/dev/null && echo "Force killed process $PID"
        fi
    done
else
    echo "No process found using port $PORT"
fi

echo "Server stopped"

# Step 2: Reload environment variables
echo "Reloading environment variables from $ENV_FILE..."
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: $ENV_FILE file not found!"
    exit 1
fi

# Export variables from .env file
set -a  # automatically export all variables
source "$ENV_FILE"
set +a  # stop auto-exporting

echo "Environment variables reloaded"
echo "Server killed"
echo "Use ./run.sh to start the server again"