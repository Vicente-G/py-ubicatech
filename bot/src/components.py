from http import HTTPStatus

import requests

from src.config import PAGE_SIZE
from src.models.routes import get_url_with_constraints
from src.models.schemas import cpu_schema


def extract_products(result_element):
    entries = result_element.get("product_entries")
    product = entries[0].get("product")
    prices = entries[0].get("metadata")
    product.update(**prices)
    return product


def get_components(component, schemify, **kwargs):
    url = get_url_with_constraints(component, **kwargs)
    response = requests.get(url, timeout=10)
    if response.status_code != HTTPStatus.OK:
        raise Exception(f"HTTP Error on cpu fetch {response.status_code}: {response.text}")

    result = response.json()
    products = list(map(extract_products, result.get("results")))
    for page in range(2, 2 + result.get("count") // PAGE_SIZE):
        response = requests.get(f"{url}&page={page}", timeout=10)
        if response.status_code != HTTPStatus.OK:
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        result = response.json()
        products.extend(list(map(extract_products, result.get("results"))))

    return list(map(schemify, products))


def get_cpu(**kwargs):
    return get_components("cpu", cpu_schema, **kwargs)
