def build_comparison_block(product: dict, competitor: dict) -> dict:
    """
    Builds a comparison structure between the main product
    and a fictional competitor.
    """
    return {
        "product_a": {
            "name": product["name"],
            "ingredients": product["attributes"].get("ingredients", []),
            "benefits": product["attributes"].get("benefits", []),
            "price": product["attributes"].get("price")
        },
        "product_b": competitor
    }
