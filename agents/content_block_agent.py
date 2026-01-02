from core.agent_base import Agent
from logic_blocks.benefits import build_benefits_block
from logic_blocks.usage import build_usage_block
from logic_blocks.safety import build_safety_block
from logic_blocks.pricing import build_pricing_block


class ContentBlockAgent(Agent):
    """
    Autonomous agent responsible for constructing reusable
    content blocks from normalized product data.

    This agent:
    - reacts to the presence of product data
    - builds content blocks exactly once
    - publishes results to shared state
    """

    def can_act(self, state) -> bool:
        """
        The agent can act if:
        - product data exists
        - content blocks have not yet been created
        """
        return state.product is not None and not state.content_blocks

    def act(self, state) -> None:
        """
        Build reusable content blocks using pure logic functions.
        """
        product = state.product

        state.content_blocks = {
            "benefits_block": build_benefits_block(product),
            "usage_block": build_usage_block(product),
            "safety_block": build_safety_block(product),
            "pricing_block": build_pricing_block(product)
        }
