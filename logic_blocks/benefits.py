def build_benefits_block(product: dict) -> list:
    """
    Extracts and returns product benefits.
    """
    return product["attributes"].get("benefits", [])
