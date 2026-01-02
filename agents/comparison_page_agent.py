from core.agent_base import Agent
from logic_blocks.comparison import build_comparison_block


class ComparisonPageAgent(Agent):
    """
    Autonomous agent responsible for assembling the comparison page.

    This agent:
    - reacts to parsed product data
    - builds a deterministic comparison
    - publishes the comparison page to shared state
    """

    def can_act(self, state) -> bool:
        """
        The agent can act if:
        - product data exists
        - comparison page has not yet been assembled
        """
        return (
            state.product is not None and
            "comparison_page" not in state.pages
        )

    def act(self, state) -> None:
        """
        Assemble the comparison page.
        """
        primary_product = state.product

        # Deterministic fictional competitor (allowed by assignment)
        competitor_product = {
            "name": "RadiancePlus Vitamin C Serum",
            "attributes": {
                "concentration": "8%",
                "benefits": ["Brightening"],
                "price": 899
            }
        }

        comparison_block = build_comparison_block(
            primary_product,
            competitor_product
        )

        comparison_page = {
            "page_type": "comparison_page",
            "comparison": comparison_block
        }

        state.pages["comparison_page"] = comparison_page
