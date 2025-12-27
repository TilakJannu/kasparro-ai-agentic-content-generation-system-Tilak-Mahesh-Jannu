from agents.template_assembly_agent import TemplateAssemblyAgent


def run_tests():
    print("Running Step 7 (TemplateAssemblyAgent) tests...\n")

    agent = TemplateAssemblyAgent()

    # -------------------------
    # Test 1: Successful Assembly
    # -------------------------
    template = {
        "page_type": "product_page",
        "fields": ["name", "price"]
    }

    data = {
        "name": "GlowBoost Vitamin C Serum",
        "price": 699
    }

    page = agent.run(template, data)

    assert page["page_type"] == "product_page"
    assert page["name"] == "GlowBoost Vitamin C Serum"
    assert page["price"] == 699

    print("✔ Test 1 passed: successful assembly")

    # -------------------------
    # Test 2: Missing Required Field
    # -------------------------
    broken_data = {
        "name": "GlowBoost Vitamin C Serum"
    }

    try:
        agent.run(template, broken_data)
        raise AssertionError("Expected KeyError for missing field")
    except KeyError as e:
        print("✔ Test 2 passed: missing field detected")

    # -------------------------
    # Test 3: No Extra Fields Added
    # -------------------------
    extra_data = {
        "name": "GlowBoost Vitamin C Serum",
        "price": 699,
        "extra_field": "should not appear"
    }

    page = agent.run(template, extra_data)

    assert "extra_field" not in page
    assert len(page.keys()) == 3  # page_type + name + price

    print("✔ Test 3 passed: extra fields ignored")

    print("\n✅ All Step 7 tests passed successfully!")


if __name__ == "__main__":
    run_tests()
