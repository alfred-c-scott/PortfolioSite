projects = dict()

project_1_description = "This 5.6MW project was completed ahead of schedule by a team of 5 electricians and mechanical contractors. A total of\
    10,368 540W Panels, 32 120KVA 3 phase Solaredge inverters, 2x Schweitzer SEL 751 Feeder Protection relays installed on a commercial site in AR.\
    |My primary responsibility on this site was to install the inverters, verify string voltages, design the material layout, and install the network\
    cable, network cable conduit, environmental sensor network, and Ageto Systems monitoring system, and feeder protection relays.\
    |Aside from the blistering heat of the Arkansas Summer, this was one of my favorite projects I have ever worked on, and was able to demonstrate my\
    understanding of 3 phase power systems, IT infrastructure, and love of building awesome stuff."

project_1_specs = [
    {"label": "Capacity", "value": "5.6 MW"},
    {"label": "Panels", "value": "10,368 x 540W"},
    {"label": "Inverters", "value": "32 x 120KVA 3-Phase SolarEdge"},
    {"label": "Protection Relays", "value": "2 x Schweitzer SEL 751"},
    {"label": "Sensor Suite", "value": ["Anemometer", "Panel Thermocouples", "Irradiance Meter"]},
]

project_1_comm_images = [
    {"src": "little_rock/comm_0.jpg", "caption": "North Side Communications Box"},
    {"src": "little_rock/comm_1.jpg", "caption": "South Side Communications Box"},
    {"src": "little_rock/comm_2.jpg", "caption": "Computer & Gateway Cabinet"},
    {"src": "little_rock/comm_3.jpg", "caption": "Solar Edge 120KVA 3-Phase Inverter"},
    {"src": "little_rock/comm_4.jpg", "caption": "North Side roof penetration"},
    {"src": "little_rock/comm_5.jpg", "caption": "North Side rigid grounding"},
    {"src": "little_rock/comm_6.jpg", "caption": "Dual rigid run for Power and Comms"},
]

project_1_pv_images = [
    {"src": "little_rock/pv_0.jpg", "caption": "Caption placeholder"},
    {"src": "little_rock/pv_1.jpg", "caption": "Caption placeholder"},
    {"src": "little_rock/pv_2.jpg", "caption": "Caption placeholder"},
]

project_1_diagram_images = [
    {"src": "little_rock/diagram_0.png", "caption": "Caption placeholder"},
    {"src": "little_rock/diagram_1.png", "caption": "Caption placeholder"},
]

project_1_diagram_pdf = "little_rock/diagram.pdf"

project_1 = {
    "name": "Little Rock, Arkansas - PV Installation",
    "description": project_1_description,
    "index_image": "little_rock/solar_thumbnail.jpg",
    "project_image": "little_rock/sunrise.jpg",
    "specs": project_1_specs,
    "comm_images": project_1_comm_images,
    "pv_images": project_1_pv_images,
    "diagram_images": project_1_diagram_images,
    "diagram_pdf": project_1_diagram_pdf,
    "image_slide_show": [
        "little_rock/comm_0.jpg",
        "little_rock/comm_1.jpg",
        "little_rock/comm_2.jpg",
        "little_rock/comm_3.jpg",
        "little_rock/comm_4.jpg",
        "little_rock/comm_5.jpg",
        "little_rock/comm_6.jpg",
        "little_rock/pv_0.jpg",
        "little_rock/pv_1.jpg",
        "little_rock/pv_2.jpg",
    ]
}

projects.update(project_1)
