name = "Alfred Clark Scott"
address = "Lexington, KY 40508"
phone = "(859) 433-6773"
email = "alfred.scott@protonmail.com"
github = "github.com/alfred-c-scott"
site = "power-lab.xyz"
professional_summary = {
    "paragraph_1": "Skilled and versatile engineer, programmer and electronics technician with more than 20 years of experience spanning power distribution\
        engineering, renewable energy field operations, military weapon systems electronics technician, and software development. Expertise in\
        hydraulic and pneumatic systems and component-level troubleshooting of electrical circuits, with a strong track record of safe, methodical\
        diagnostics in complex, high-risk environments. Proven ability to interpret complex wiring diagrams, relay logic, and technical\
        documentation to identify root cause, implement durable corrective actions, and document results for compliance and repeatability.",
    "paragraph_2": "Power Distribution Engineer at Kentucky Utilities (LG&E), supported the reliability and safety of high voltage residential and commercial distribution\
        systems through redundant designs, field coordination, and technical analysis—helping ensure reliable service delivery and rapid\
        restoration when outages occurred.",
    "paragraph_3": "As a Solar Installer/Maintenance Technician, performed installation support, commissioning, troubleshooting, and preventative\
        maintenance for networked high capacity photovoltaic systems, inverters, electrical interconnects, and associated power monitoring and\
        control systems, ensuring system performance and adherence to safety standards.",
    "paragraph_4": "During Operation Enduring Freedom served as Electronics Technician (CIWS) in the U.S. Navy, diagnosed and repaired intricate\
        electronic and electromechanical systems under high-tempo operational conditions, maintaining readiness through disciplined\
        maintenance practices and detailed documentation. which required a strong understanding of PLCs, robotics, servos, steppers, as well\
        as 60Hz->400Hz power converters and high power amplifiers such as klystrons and magnetrons.",
    "paragraph_5": "Additionally, novice level expertise in microcontroller development and embedded programming on ESP32 and STM32 platforms,\
        integrating various sensors and communication protocols over UART, SPI, and I2C interfaces, and validating performance through unit\
        testing and troubleshooting."
}

bullets = [
    "3 Phase Power Systems",
    "Switchgear Installation",
    "CT Installation and wiring",
    "Transformer sizing/installation",
    "Distribution system design",
    "High Voltage AC/DC Maintenance",
    "Grid Tied Solar Systems",
    "Hydraulic Drive Systems",
    "Servo / Synchro systems",
    "Motors and Generators",
    "Autodesk Eagle/Fusion 360",
    "Through Hole Soldering",
    "Surface Mount Soldering",
    "Schweitzer PLC installation",
    "OAuth 2.0 with TOTP 2FA",
    "C / C++ / Python / SQL / Ansible",
    "FastAPI / SQLAlchemy / Pydantic",
    "Unix / Linux (Debian variants)",
    "PostgreSQL Database",
    "AI IDEs Cursor/Claude Code",
]

jobs = list()

job_template = {
    "company": "",
    "start_date": "",
    "end_date": "",
    "job_title": "",
    "contact_type": "",
    "contact_name": "",
    "contact_pone": "",
    "bullets": []
}

gigavend = job_template.copy()
gigavend['company'] = "Gigavend Money Services"
gigavend['start_date'] = "Sep 2024"
gigavend['end_date'] =  "Nov 2025"
gigavend['job_title'] = "Project Lead | Software Engineer | Infrastructure Engineer"
gigavend['contact_type'] = "Owner"
gigavend['contact_name'] = "Gary Houck"
gigavend['contact_phone'] = "(859) 955 - 0169"
gigavend['bullets'] = [
    "Developed C++ library for Pertech Industries 6100K scanner encapsulating low-level hardware commands to be implemented in a QT6\
    QML GUI. Supported multi-format document scanning system for check and ID card processing with configurable parameters including\
    color schemes (grayscale, color, UV, infrared), and real-time sensor monitoring.",

    "Developed C++ library for the DigitalPersona 4500 fingerprint scanner enabling fingerprint capture for login system. Enabling\
    enrollment, and verification functionality being used in QT6 QML application on Financial Kiosks and ATM machines",

    "Designed and developed a full-stack check cashing application using FastAPI, SQLAlchemy, and PostgreSQL, implementing role-based\
    authentication with JWT tokens, two-factor auth via TOTP, and real-time customer review workflows with automated barcode\
    scanning using Azure Document Intelligence APIs. Leveraging AI models such as Claude for frontend HTML layouts and JavaScript API\
    calls",

    "Built scalable cloud-native infrastructure integrating AWS S3 for file storage, Twilio SMS verification, and containerized the Python\
    FastAPI application with Docker, implementing custom middleware for token refresh, session management, and automated database\
    migrations with Alembic"
]

jobs.append(gigavend)