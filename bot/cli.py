import argparse
import json

from src.components import get_cpu
from src.models.routes import (
    CASE_FAN_SIZES,
    CASE_SIZES,
    COMPONENT_URLS,
    CPU_COOLING_TYPES,
    CPU_SOCKETS,
    GPU_PERFORMANCE,
    PSU_CERTS,
    RAM_TYPES,
    SSD_TYPES,
)
from src.tools import ignore_wildcard, remove_nulls


def main():
    parser = argparse.ArgumentParser(
        description="Get SoloTodo PC components based on custom constraints and options."
    )
    parser.add_argument(
        "component",
        nargs=1,
        type=str,
        choices=COMPONENT_URLS.keys(),
        help="The component type to browse in the SoloTodo API.",
    )

    parser.add_argument(
        "--socket",
        type=str,
        choices=list(filter(ignore_wildcard, CPU_SOCKETS.keys())),
        help="Socket type of CPU. Available for components: cpu, mb, pc.",
    )

    parser.add_argument(
        "--ram-type",
        type=str,
        choices=list(filter(ignore_wildcard, RAM_TYPES.keys())),
        help="RAM type. Available for components: ram, mb.",
    )

    parser.add_argument(
        "--case-size",
        type=str,
        choices=list(filter(ignore_wildcard, CASE_SIZES.keys())),
        help="Case size. Available for components: mb, box.",
    )

    parser.add_argument(
        "--ssd-type",
        type=str,
        choices=SSD_TYPES.keys(),
        help="SSD bus type. Available for components: ssd.",
    )

    parser.add_argument(
        "--cpu-cooling",
        type=str,
        choices=CPU_COOLING_TYPES.keys(),
        help="Procesor Cooling type. Available for components: pc.",
    )

    parser.add_argument(
        "--fan-size",
        type=int,
        choices=CASE_FAN_SIZES.keys(),
        help="Case Fan size in mm. Available for components: cf.",
    )

    parser.add_argument(
        "--psu-cert",
        type=str,
        choices=PSU_CERTS.keys(),
        help="PSU certification. Available for components: psu.",
    )

    parser.add_argument(
        "--gpu-perf",
        type=int,
        choices=GPU_PERFORMANCE.keys(),
        help="GPU performance level on fps high settings. Available for components: gpu.",
    )

    parser.add_argument(
        "--recommended-psu-only",
        action="store_true",
        help="Show only recommended brands of PSUs. Available for components: psu.",
    )

    parser.add_argument(
        "--min-price",
        type=float,
        help="Minimum price in USD for the component. Available for all components.",
    )
    parser.add_argument(
        "--max-price",
        type=float,
        help="Maximum price in USD for the component. Available for all components.",
    )
    args = parser.parse_args()._get_kwargs()
    component = args.pop(0)[1][0]
    max_price, min_price = args.pop(-1)[1], args.pop(-1)[1]
    if max_price or min_price:
        args.append(("price_range", (min_price, max_price)))
    if component == "cpu":
        with open("temp.json", "w") as file:
            file.write(json.dumps(get_cpu(**dict(filter(remove_nulls, args)))))
    else:
        raise ValueError("Not Implemented Error: Only 'cpu' is supported for now.")


if __name__ == "__main__":
    main()
