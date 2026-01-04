from core.contact_info import contact_info

contact_info = contact_info

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

certifications = [
    {"name": "Comptia Network+", "pdf": "CompTIA_Network+_ce_certificate.pdf"},
    {"name": "Comptia Security+", "pdf": "CompTIA_Security+_ce_certificate.pdf"},
]

education = {
    "univeristy": "University of Kentucky",
    "degree": "B.S. Electrical Engineering - Graduation Date: Fall 2007",
    "focus": "Power Systems / Computer Science"
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
    "Servo / Syncro systems",
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
    "contract": False,
    "job_title": "",
    "contact_type": None,
    "contact_name": None,
    "contact_pone": None,
    "bullets": []
}

gigavend = job_template.copy()
gigavend['company'] = "Gigavend Money Services"
gigavend['start_date'] = "Sep 2024"
gigavend['end_date'] =  "Nov 2025"
gigavend['contract'] = True
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

solar_energy_solutions = job_template.copy()
solar_energy_solutions['company'] = "Solar Energy Solutions"
solar_energy_solutions['start_date'] = "Aug 2022"
solar_energy_solutions['end_date'] =  "Feb 2024"
solar_energy_solutions['job_title'] = "Electrician Apprentice | Maintenance Technician"
solar_energy_solutions['contact_type'] = "Site Supervisor"
solar_energy_solutions['contact_name'] = "Robert McCoy"
solar_energy_solutions['contact_phone'] = "(859) 559 - 6575"
solar_energy_solutions['bullets'] = [
    "Use technical diagrams and manuals to install, test, troubleshoot, and commission solar panels and inverters, ensuring optimal\
    performance while conforming to the NEC (National Electric Code).",

    "Leverage my background in designing power distribution systems to quickly identify and address the potential for future system\
    failures, faults, and performance issues.",

    "Successfully diagnosed and resolved complex issues related to solar array inverters and electrical panels by applying troubleshooting\
    techniques, minimizing downtime, and enhancing overall efficiency of the solar energy systems.",

    "Ability to work independently or as part of a team, with effective communication and interpersonal skills to effectively collaborate with\
    colleagues, contractors, and customers.",

    "Commitment to SOPs (Standard Operating Procedures) and safety protocols, including OSHA regulations and NEC (National Electric\
    Code) best practices, maintaining a safe working environment for myself and my team.",
]
jobs.append(solar_energy_solutions)

osprey_global = job_template.copy()
osprey_global['company'] = "Osprey Global"
osprey_global['start_date'] = "Jun 2020"
osprey_global['end_date'] =  "Jan 2025"
osprey_global['contract'] = True
osprey_global['job_title'] = "Sales Representative | Customer Service"
osprey_global['contact_type'] = "Site Supervisor"
osprey_global['contact_name'] = "William Burke"
osprey_global['contact_phone'] = "(859) 967 - 4845"
osprey_global['bullets'] = [
    "Surveyed prospects to determine if our products were a good fit for them, and if they qualified, the information from the interactions\
    would be used to deliver a data driven pitch about why our products were a good fit for their needs.",

    "Developed and fostered strong relationships with customers after purchase and assisted with set-up, install, and maintenance of their\
    equipment.",

    "Traveled across the Midwest to trade shows to set up and merchandise our booths at many of the largest gun and outdoor equipment\
    expos in the U.S.",
]
jobs.append(osprey_global)

uber_scientific = job_template.copy()
uber_scientific['company'] = "Uber Scientific"
uber_scientific['start_date'] = "May 2016"
uber_scientific['end_date'] =  "Dec 2019"
uber_scientific['job_title'] = "SEO | Project Manager | Product Design"
uber_scientific['contact_type'] = "Owner"
uber_scientific['contact_name'] = "Gary Houck"
uber_scientific['contact_phone'] = "(859) 955 - 0169"
uber_scientific['bullets'] = [
    "Developed an inventory projection system that optimized component procurement from various suppliers for large-scale\
    manufacturing of multi-component products, adhering to CPSC and FDA regulations, reducing cost, and increased ROI and margins.",

    "Development of multi-million dollar projects from concept to market, including market research, product development, vendor and\
    contract negotiations, and budget management while meeting key product deliverable deadlines.",

    "Excelled in managing multiple projects concurrently while mitigating risk factors in a rapidly evolving global supply chain environment.",

    "Monitored and analyzed SEO tactics and strategies in a constant effort to optimize e-commerce sales conversion rates. Leading team\
    of remote graphic designers and copy writers constantly improving product images, mockups, and copy for desktop and mobile\
    platforms. Data driven analysis, optimization, and management of Pay-Per-Click advertising campaigns on amazon.com.",
]
jobs.append(uber_scientific)

kentucky_utilities = job_template.copy()
kentucky_utilities['company'] = "Kentucky Utilities"
kentucky_utilities['start_date'] = "Nov 2014"
kentucky_utilities['end_date'] =  "May 2016"
kentucky_utilities['job_title'] = "SEO | Project Manager | Product Design"
kentucky_utilities['contact_type'] = "Human Resources"
kentucky_utilities['contact_phone'] = "(502) 627 - 2000"
kentucky_utilities['bullets'] = [
    "Led power distribution projects overseeing design, planning, and installation of high-voltage electrical distribution systems, ensuring\
    reliable and efficient delivery of electricity to customers",

    "Oversaw the design and installation of a smart grid metering system which enabled real-time monitoring, analysis, and control of\
    electric grid functions, allowing for faster fault identification, isolation, and restoration, minimizing downtime, and improving reliability",

    "Conducted power factor analysis to assess power quality and efficiency of power distribution systems and implemented measures\
    such as capacitor banks to optimize power quality, resulting in enhanced system performance, reduced energy waste, and improved\
    power quality for customers.",

    "Designed power distribution and prepared studies for a variety of end users, including hospitals, office buildings, industrial,\
    commercial, and governmental facilities requiring High Voltage Single and Three Phase electrical service.",
]
jobs.append(kentucky_utilities)


malones = job_template.copy()
malones['company'] = "Malone's Steakhouse | Harry's Bar | Bella Notte"
malones['start_date'] = "May 2007"
malones['end_date'] =  "Nov 2014"
malones['job_title'] = "Bar Manager | Bartender | Trainer"
malones['contact_type'] = "Human Resources"
malones['contact_name'] = "Eric Reihing"
malones['contact_phone'] = "(859) 264-8894"
malones['bullets'] = [
    "Maintained a high level of productivity in an extremely high volume, fast paced, and stressful environment.",

    "Responsible for the training and development of all Servers and Bartenders in Wine, Liquor, and Beer education and sales.",

    "Distributor Relations - Making bi-weekly orders to Wine, Spirits, equipment distributors maintaining effective inventory levels while\
    minimizing overhead and maintaining productive relationship with the vendors.",

    "Conducted weekly inventory counts used to analyze, correct, and improve bar performance, sales, and profit margins. "
]
jobs.append(malones)

unites_states_navy = job_template.copy()
unites_states_navy['company'] = "United States Navy"
unites_states_navy['start_date'] = "May 2002"
unites_states_navy['end_date'] =  "May 2006"
unites_states_navy['job_title'] = "Fire Controlman | Electronics Technician | VBSS Team"
unites_states_navy['bullets'] = [
    "Managed and led a diverse team of professionals, ensuring efficient workflow and the achievement of maintenance objectives.",

    "Oversaw operations, delegated tasks, and provided guidance ensuring work was completed on time and within quality standards.",

    "Conducted maintenance, repair, and replacement of high-voltage DC motors and servos, 400 Hz converters, high-power amplifiers,\
    air compressors, hydraulic, and pneumatic drive systems.",

    "Ordered and tracked repair parts for the Phalanx, Tomahawk, Harpoon, and MK-45 weapon systems within the Naval and Marine\
    Corps repair parts requisition system.",

    "VBSS Team member responsible for the boarding, inspection, and search of foreign vessels suspected of piracy, as well as the\
    smuggling drugs, weapons, and terrorist personnel through the Persian Gulf, Horn of Africa, and Red Sea."
]
jobs.append(unites_states_navy)
