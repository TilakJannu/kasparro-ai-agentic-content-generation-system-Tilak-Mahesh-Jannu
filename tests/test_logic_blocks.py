from data.input_product import PRODUCT_DATA
from agents.product_parser_agent import ProductParserAgent

from logic_blocks.benefits import build_benefits_block
from logic_blocks.usage import build_usage_block
from logic_blocks.safety import build_safety_block
from logic_blocks.pricing import build_pricing_block
from logic_blocks.comparison import build_comparison_block


def run_tests():
    print("Running Step 4 Logic Block Tests...\n")

    parser = ProductParserAgent()
    product = parser.run(PRODUCT_DATA)

    # ------------------------
    # Benefits Block
    # ------------------------
    benefits = build_benefits_block(product)
    assert isinstance(benefits, list)
    assert "Brightening" in benefits
    print("✔ Benefits block passed")

    # ------------------------
    # Usage Block
    # ------------------------
    usage = build_usage_block(product)
    assert isinstance(usage, dict)
    assert "instructions" in usage
    assert "recommended_time" in usage
    print("✔ Usage block passed")

    # ------------------------
    # Safety Block
    # ------------------------
    safety = build_safety_block(product)
    assert isinstance(safety, dict)
    assert "side_effects" in safety
    assert "applicable_skin_types" in safety
    assert "Oily" in safety["applicable_skin_types"]
    print("✔ Safety block passed")

    # ------------------------
    # Pricing Block
    # ------------------------
    pricing = build_pricing_block(product)
    assert pricing["price"] == 699
    assert pricing["currency"] == "INR"
    print("✔ Pricing block passed")

    # ------------------------
    # Comparison Block
    # ------------------------
    competitor = {
        "name": "RadiancePlus Serum",
        "ingredients": ["Vitamin C"],
        "benefits": ["Brightening"],
        "price": 899
    }

    comparison = build_comparison_block(product, competitor)
    assert "product_a" in comparison
    assert "product_b" in comparison
    assert comparison["product_b"]["name"] == "RadiancePlus Serum"
    print("✔ Comparison block passed")

    print("\n✅ All Step 4 logic block tests passed successfully!")


if __name__ == "__main__":
    run_tests()
