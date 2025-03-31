PRICE_RANGE_LENGTH = 2


def add_list_on_component(keys, array):
    def condition(component, value):
        if component not in keys:
            return None
        if value:
            return "&".join(array)
        return ""

    return condition


def select_component_type(keys, options):
    def condition(component, value):
        if component not in keys:
            return None
        if options.get(value) is not None:
            return options.get(value)
        return ""

    return condition


def component_between_price(component, price_range):
    if len(price_range) != PRICE_RANGE_LENGTH:
        raise ValueError(f"Invalid price range for component: {component}")
    start, end = price_range
    if start is None or end is None:
        return None
    if start is None:
        return f"offer_price_usd_end={end}"
    if end is None:
        return f"offer_price_usd_start={start}"
    if start > end:
        return None
    return f"offer_price_usd_start={start}&offer_price_usd_end={end}"
