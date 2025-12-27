def build_pricing_block(product: dict) -> dict:
    """
    Builds pricing information.
    """
    return {
        "price": product["attributes"].get("price"),
        "currency": "INR"
    }
