def build_usage_block(product: dict) -> dict:
    """
    Builds structured usage instructions.
    """
    return {
        "instructions": product["attributes"].get("usage"),
        "recommended_time": "Morning"
    }
