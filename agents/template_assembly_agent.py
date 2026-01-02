from core.agent_base import Agent


class TemplateAssemblyAgent(Agent):
    """
    Autonomous agent responsible for assembling page-level
    structures from shared state.

    This agent:
    - observes shared state readiness
    - assembles pages exactly once
    - does not impose execution order
    """

    def can_act(self, state) -> bool:
        """
        The agent can act if:
        - product data exists
        - content blocks exist
        - product page has not yet been assembled
        """
        return (
            state.product is not None and
            state.content_blocks and
            "product_page" not in state.pages
        )

    def act(self, state) -> None:
        """
        Assemble the product page from available state fragments.
        """
        product = state.product

        product_page = {
            "page_type": "product_page",
            "name": product["name"]
        }

        # Inject reusable content blocks
        product_page.update(state.content_blocks)

        # Publish assembled page to shared state
        state.pages["product_page"] = product_page
