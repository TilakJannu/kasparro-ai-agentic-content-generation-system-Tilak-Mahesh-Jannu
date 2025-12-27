from agents.output_validation_agent import OutputValidationAgent

def run_tests():
    validator = OutputValidationAgent()

    valid_page = {
        "page_type": "product_page",
        "name": "GlowBoost",
        "benefits_block": [],
        "usage_block": {},
        "safety_block": {},
        "pricing_block": {}
    }

    validator.run(valid_page)
    print("✔ Valid product page passed")

    try:
        validator.run({"name": "Broken Page"})
    except ValueError:
        print("✔ Invalid page correctly rejected")

if __name__ == "__main__":
    run_tests()
