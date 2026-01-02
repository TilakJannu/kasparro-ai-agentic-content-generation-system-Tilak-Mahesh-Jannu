from core.agent_base import Agent


class FAQPageAgent(Agent):
    """
    Autonomous agent responsible for assembling the FAQ page.

    This agent:
    - reacts to generated questions
    - assembles the FAQ page exactly once
    - publishes it to shared state
    """

    def can_act(self, state) -> bool:
        """
        The agent can act if:
        - questions exist
        - FAQ page has not yet been assembled
        """
        return (
            state.questions is not None and
            "faq_page" not in state.pages
        )

    def act(self, state) -> None:
        """
        Assemble the FAQ page from generated questions.
        """
        faq_page = {
            "page_type": "faq_page",
            "questions": state.questions
        }

        state.pages["faq_page"] = faq_page
