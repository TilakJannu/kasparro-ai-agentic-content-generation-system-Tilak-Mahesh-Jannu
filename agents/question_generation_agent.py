from core.agent_base import Agent


class QuestionGenerationAgent(Agent):
    """
    Autonomous agent that:
    - generates categorized user questions
    - evaluates its own output
    - expands questions until coverage is sufficient

    This agent decides *for itself* when it has done enough work.
    """

    MIN_QUESTIONS = 15

    def can_act(self, state) -> bool:
        return state.product is not None and state.questions is None

    def act(self, state) -> None:
        product = state.product
        name = product["name"]
        attr = product["attributes"]

        questions = {
            "Informational": [],
            "Usage": [],
            "Safety": [],
            "Purchase": [],
            "Comparison": []
        }

        # -------- Phase 1: Core generation --------

        self._generate_core_questions(questions, name, attr)

        # -------- Phase 2: Self-evaluation & expansion --------

        while not self._is_sufficient(questions):
            self._expand_questions(questions, name, attr)

        state.questions = questions

    # ==============================
    # Internal reasoning methods
    # ==============================

    def _is_sufficient(self, questions: dict) -> bool:
        """
        Agent's internal evaluation of completeness.
        """
        total = sum(len(v) for v in questions.values())
        return total >= self.MIN_QUESTIONS

    def _generate_core_questions(self, q, name, attr):
        q["Informational"].extend([
            f"What is {name}?",
            f"What benefits does {name} provide?"
        ])

        q["Usage"].extend([
            f"How should {name} be used?"
        ])

        q["Safety"].append("Are there any side effects?")
        q["Purchase"].append("What is the price of this product?")
        q["Comparison"].append(
            f"How does {name} compare to similar products?"
        )

    def _expand_questions(self, q, name, attr):
        """
        Agent-driven expansion strategy.
        Chooses which category to enrich next.
        """

        # Prioritize underrepresented categories
        category = min(q, key=lambda k: len(q[k]))

        if category == "Informational":
            self._expand_informational(q, name, attr)

        elif category == "Usage":
            self._expand_usage(q, name, attr)

        elif category == "Safety":
            self._expand_safety(q, attr)

        elif category == "Purchase":
            self._expand_purchase(q)

        elif category == "Comparison":
            self._expand_comparison(q, name)

    # -------- Category-specific strategies --------

    def _expand_informational(self, q, name, attr):
        if attr.get("ingredients"):
            q["Informational"].append(
                f"What are the key ingredients in {name}?"
            )
        if attr.get("concentration"):
            q["Informational"].append(
                f"What is the concentration of Vitamin C in {name}?"
            )

    def _expand_usage(self, q, name, attr):
        q["Usage"].extend([
            "Can this product be used daily?",
            "Should it be used in the morning or evening?"
        ])

    def _expand_safety(self, q, attr):
        q["Safety"].extend([
            "Is this product suitable for sensitive skin?",
            "Is mild tingling normal?"
        ])

    def _expand_purchase(self, q):
        q["Purchase"].append(
            "Is this product worth the price?"
        )

    def _expand_comparison(self, q, name):
        q["Comparison"].append(
            f"What makes {name} different from other serums?"
        )
