class QuestionGenerationAgent:
    """
    Responsibility:
    - Generate categorized user questions derived strictly from product data
    - Apply deterministic, rule-based logic (no static question lists)

    This agent does NOT:
    - Answer questions
    - Format content
    - Know about pages or templates
    """

    def run(self, product: dict) -> dict:
        name = product["name"]
        attr = product["attributes"]

        return {
            "Informational": self._generate_informational(name, attr),
            "Usage": self._generate_usage(name, attr),
            "Safety": self._generate_safety(name, attr),
            "Purchase": self._generate_purchase(name, attr),
            "Comparison": self._generate_comparison(name)
        }

    # -------------------------
    # Rule-based generators
    # -------------------------

    def _generate_informational(self, name: str, attr: dict) -> list:
        questions = []

        questions.append(f"What is {name}?")

        if attr.get("benefits"):
            questions.append(
                f"What benefits does {name} provide?"
            )

        if attr.get("ingredients"):
            questions.append(
                f"What are the key ingredients in {name}?"
            )

        if attr.get("concentration"):
            questions.append(
                f"What does the {attr['concentration']} concentration indicate?"
            )

        if attr.get("skin_type"):
            questions.append(
                f"Which skin types is {name} suitable for?"
            )

        return questions

    def _generate_usage(self, name: str, attr: dict) -> list:
        questions = []

        if attr.get("usage"):
            questions.append(
                f"How should {name} be used?"
            )

        questions.append(
            f"When should {name} be applied in a skincare routine?"
        )

        questions.append(
            f"Can {name} be used daily?"
        )

        return questions

    def _generate_safety(self, name: str, attr: dict) -> list:
        questions = []

        questions.append(
            f"Are there any side effects associated with {name}?"
        )

        if attr.get("side_effects"):
            questions.append(
                "What side effects should users be aware of?"
            )

        if attr.get("skin_type"):
            questions.append(
                "Is this product suitable for sensitive skin?"
            )

        return questions

    def _generate_purchase(self, name: str, attr: dict) -> list:
        questions = []

        if attr.get("price") is not None:
            questions.append(
                f"What is the price of {name}?"
            )

        questions.append(
            "Is this product good value for money?"
        )

        questions.append(
            "Who should consider purchasing this product?"
        )

        return questions

    def _generate_comparison(self, name: str) -> list:
        return [
            f"How does {name} compare to other similar products?",
            f"What makes {name} different from competing alternatives?"
        ]
