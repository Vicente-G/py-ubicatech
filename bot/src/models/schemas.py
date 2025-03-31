from src.config import REDIRECT_URL


def cpu_schema(product_element):
    specs = product_element.get("specs")
    clp_prices = product_element.get("prices_per_currency")[0]
    id = product_element.get("id")
    return {
        "name": product_element.get("name"),
        "brand": product_element.get("brand_name"),
        "image": product_element.get("picture_url"),
        "price_usd": product_element.get("normal_price_usd"),
        "price_clp": clp_prices.get("normal_price"),
        "solotodo_link": f"{REDIRECT_URL}/{id}",
        "cores": specs.get("core_count_value"),
        "threads": specs.get("thread_count_value"),
        "base_clock": specs.get("frequency"),
        "boost_clock": specs.get("max_turbo_frequency"),
        "tdp": specs.get("tdp"),
        "socket": specs.get("socket_unicode"),
        "architecture": specs.get("core_architecture_unicode"),
        "integrated_graphics": specs.get("graphics_unicode"),
        "cpu_cooler": specs.get("cooler_unicode"),
        "benchmark_single_core": specs.get("cinebench_r20_single_score"),
        "benchmark_multi_core": specs.get("cinebench_r20_multi_score"),
    }
