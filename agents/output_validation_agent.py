class OutputValidationAgent:
    """
    Responsibility:
    - Validate assembled page objects before serialization

    This agent performs:
    ✔ structural validation
    ✔ required-field checks

    This agent does NOT:
    ✘ modify content
    ✘ generate data
    ✘ write output files
    """

    REQUIRED_BASE_FIELDS = ["page_type"]

    def run(self, page: dict) -> dict:
        """
        Entry point for validation.

        Input:
        - page: assembled page dictionary

        Output:
        - same page if valid
        - raises ValueError if invalid
        """
        self._validate_base_structure(page)
        self._validate_page_specific_structure(page)
        return page

    # -------------------------
    # Internal validation
    # -------------------------

    def _validate_base_structure(self, page: dict):
        if not isinstance(page, dict):
            raise ValueError("Page must be a dictionary")

        for field in self.REQUIRED_BASE_FIELDS:
            if field not in page:
                raise ValueError(f"Missing required base field: '{field}'")

    def _validate_page_specific_structure(self, page: dict):
        page_type = page.get("page_type")

        if page_type == "faq_page":
            self._validate_faq_page(page)

        elif page_type == "product_page":
            self._validate_product_page(page)

        elif page_type == "comparison_page":
            self._validate_comparison_page(page)

        else:
            raise ValueError(f"Unknown page_type: '{page_type}'")

    # -------------------------
    # Page-type validators
    # -------------------------

    def _validate_faq_page(self, page: dict):
        if "questions" not in page:
            raise ValueError("FAQ page must contain 'questions'")

        if not isinstance(page["questions"], dict):
            raise ValueError("'questions' must be a dictionary")

    def _validate_product_page(self, page: dict):
        required_fields = [
            "name",
            "benefits_block",
            "usage_block",
            "safety_block",
            "pricing_block"
        ]

        for field in required_fields:
            if field not in page:
                raise ValueError(
                    f"Product page missing required field: '{field}'"
                )

    def _validate_comparison_page(self, page: dict):
        if "comparison" not in page:
            raise ValueError("Comparison page must contain 'comparison'")

        comparison = page["comparison"]

        if not isinstance(comparison, dict):
            raise ValueError("'comparison' must be a dictionary")

        if "product_a" not in comparison or "product_b" not in comparison:
            raise ValueError(
                "Comparison must include 'product_a' and 'product_b'"
            )
