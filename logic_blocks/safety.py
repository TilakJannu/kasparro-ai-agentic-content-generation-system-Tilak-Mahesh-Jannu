def build_safety_block(product: dict) -> dict:
    """
    Builds safety-related information.
    """
    return {
        "side_effects": product["attributes"].get("side_effects"),
        "applicable_skin_types": product["attributes"].get("skin_type", [])
    }
