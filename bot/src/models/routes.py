from src.config import API_URL, PAGE_SIZE
from src.tools.routing_helper import (
    add_list_on_component,
    component_between_price,
    select_component_type,
)

COMPONENT_URLS = {
    "cpu": f"{API_URL}/3/browse/",
    "mb": f"{API_URL}/5/browse/",
    "ram": f"{API_URL}/7/browse/",
    "hdd": f"{API_URL}/8/browse/",
    "ssd": f"{API_URL}/39/browse/",
    "gpu": f"{API_URL}/2/browse/",
    "pc": f"{API_URL}/12/browse/",
    "cf": f"{API_URL}/87/browse/",
    "box": f"{API_URL}/10/browse/",
    "psu": f"{API_URL}/11/browse/",
}

DESKTOP_DEFAULTS = {
    "ram": "formats=130758",
    "hdd": "bus=204750&sizes=204422&types=203914",
    "gpu": "gpu_brands=106034&gpu_brands=106027",
    "psu": "has_active_pfc=1",
}

CPU_SOCKETS = {
    "*": ["cpu", "mb", "pc"],
    "lga12": {"cpu": "sockets=1165742", "mb": "sockets=1153273", "pc": "socket=505022"},
    "lga17": {
        "cpu": "sockets=1495133",
        "mb": "sockets=1490218",
        "pc": "socket=1503117",
    },
    "lga18": {
        "cpu": "sockets=1973425",
        "mb": "sockets=1973357",
        "pc": "socket=1828585",
    },
    "am4": {"cpu": "sockets=590711", "mb": "sockets=593822", "pc": "socket=1767310"},
    "am5": {"cpu": "sockets=1647089", "mb": "sockets=1646832", "pc": "socket=1636542"},
}

RAM_TYPES = {
    "*": ["ram", "mb"],
    "ddr4": {"ram": "types=130774", "mb": "memory_types=130774"},
    "ddr5": {"ram": "types=1490246", "mb": "memory_types=1490246"},
}

CASE_SIZES = {
    "*": ["mb", "box"],
    "mini-itx": {"mb": "mb_format=131150", "box": "motherboard_formats=251395"},
    "micro-atx": {"mb": "mb_format=131143", "box": "motherboard_formats=251385"},
    "atx": {"mb": "mb_format=131146", "box": "motherboard_formats=251389"},
    "extended-atx": {"mb": "mb_format=131154", "box": "motherboard_formats=251399"},
}

SSD_TYPES = {
    "sata": "format_families=1560425&base_buses=1559283",
    "nvme": "base_buses=1559281",
}

CPU_COOLING_TYPES = {
    "liquid": "types=276488",
    "air": "fan_size=276511&has_heatpipes=1&types=276479",
}

CASE_FAN_SIZES = {120: "sizes=1545572", 140: "sizes=1545648"}

PSU_CERTS = {
    "bronze": "certification_start=248008",
    "silver": "certification_start=248022",
    "gold": "certification_start=248027",
    "platinum": "certification_start=248031",
}

GPU_PERFORMANCE = {
    30: "tdmark_time_spy_score_start=4000",
    60: "tdmark_time_spy_score_start=7000",
    90: "tdmark_time_spy_score_start=10000",
    120: "tdmark_time_spy_score_start=12000",
}

# Source: Linus Tech Tips tier list of PSUs
PSU_RECOMMENDATIONS = [
    "brands=248119",
    "brands=248112",
    "brands=248110",
    "brands=817237",
    "brands=248106",
    "brands=248080",
    "brands=685786",
    "brands=959779",
    "brands=1229461",
    "brands=248257",
    "brands=248116",
    "brands=248124",
    "brands=1413870",
    "brands=1314034",
]

COMPONENT_RELATION_CONSTRAINTS = {
    "socket": CPU_SOCKETS,
    "ram_type": RAM_TYPES,
    "case_size": CASE_SIZES,
}

COMPONENT_CUSTOM_CONSTRAINTS = {
    "recommended_psu_only": add_list_on_component(["psu"], PSU_RECOMMENDATIONS),
    "ssd_type": select_component_type(["ssd"], SSD_TYPES),
    "cpu_cooling": select_component_type(["pc"], CPU_COOLING_TYPES),
    "fan_size": select_component_type(["cf"], CASE_FAN_SIZES),
    "psu_cert": select_component_type(["psu"], PSU_CERTS),
    "gpu_perf": select_component_type(["gpu"], GPU_PERFORMANCE),
    "price_range": component_between_price,
}


def get_url_with_constraints(component, **kwargs):
    base_url = COMPONENT_URLS.get(component)
    if base_url is None:
        raise ValueError(f"Invalid component type: {component}")

    constraints = []
    if component in DESKTOP_DEFAULTS:
        constraints.append(DESKTOP_DEFAULTS[component])
    for key, value in kwargs.items():
        constraint = COMPONENT_RELATION_CONSTRAINTS.get(key)
        if constraint:
            if component not in constraint.get("*"):
                continue
            selection = constraint.get(value)
            if not selection:
                raise ValueError(f"Invalid value: {value} for constraint: {key}")
            constraints.append(selection.get(component))
        else:
            constraint = COMPONENT_CUSTOM_CONSTRAINTS.get(key)
            if not constraint:
                raise ValueError(f"Invalid constraint of name: {key}")
            resolved_constraint = constraint(component, value)
            if resolved_constraint is None:
                continue
            if not resolved_constraint:
                raise ValueError(f"Couldn't resolve constraint: {key} for value: {value}")
            constraints.append(resolved_constraint)

    return f"{base_url}?page_size={PAGE_SIZE}&{'&'.join(constraints)}"
