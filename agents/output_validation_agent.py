from core.agent_base import Agent


class OutputValidationAgent(Agent):
    """
    Autonomous agent responsible for validating assembled pages.

    This agent:
    - observes assembled pages in shared state
    - validates structure based on page_type
    - marks pages as validated
    - does NOT control orchestration or execution order
    """

    # -------------------------
    # Agent interface methods
    # -------------------------

    def can_act(self, state) -> bool:
        """
        The agent can act if at least one page exists
        that has not yet been validated.
        """
        return any(
            page_name not in state.validated_pages
            for page_name in state.pages
        )

    def act(self, state) -> None:
        """
        Validate all unvalidated pages in shared state.
        """
        for page_name, page in state.pages.items():
            if page_name in state.validated_pages:
                continue

            self._validate_page(page)
            state.validated_pages.add(page_name)

    # -------------------------
    # Internal validation logic
    # -------------------------

    def _validate_page(self, page: dict) -> None:
        if not isinstance(page, dict):
            raise ValueError("Page must be a dictionary")

        if "page_type" not in page:
            raise ValueError("Missing required field: 'page_type'")

        page_type = page["page_type"]

        if page_type == "product_page":
            self._validate_product_page(page)

        elif page_type == "faq_page":
            self._validate_faq_page(page)

        elif page_type == "comparison_page":
            self._validate_comparison_page(page)

        else:
            raise ValueError(f"Unknown page_type: {page_type}")

    # -------------------------
    # Page-specific validators
    # -------------------------

    def _validate_product_page(self, page: dict) -> None:
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

    def _validate_faq_page(self, page: dict) -> None:
        if "questions" not in page:
            raise ValueError("FAQ page missing required field: 'questions'")

        if not isinstance(page["questions"], dict):
            raise ValueError("'questions' must be a dictionary")

    def _validate_comparison_page(self, page: dict) -> None:
        if "comparison" not in page:
            raise ValueError(
                "Comparison page missing required field: 'comparison'"
            )

        if not isinstance(page["comparison"], dict):
            raise ValueError("'comparison' must be a dictionary")
