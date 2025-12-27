from logic_blocks.benefits import build_benefits_block
from logic_blocks.usage import build_usage_block
from logic_blocks.safety import build_safety_block
from logic_blocks.pricing import build_pricing_block


class ContentBlockAgent:
    """
    Responsibility:
    - Compose reusable content blocks by invoking pure logic functions

    This agent performs:
    ✔ content block composition
    ✔ structured aggregation

    This agent does NOT:
    ✘ generate questions
    ✘ assemble pages
    ✘ apply templates
    ✘ write output files
    """

    def run(self, product: dict) -> dict:
        """
        Entry point for the agent.

        Input:
        - Normalized product model

        Output:
        - Dictionary of named content blocks
        """
        return {
            "benefits_block": self._build_benefits(product),
            "usage_block": self._build_usage(product),
            "safety_block": self._build_safety(product),
            "pricing_block": self._build_pricing(product)
        }

    # -------------------------
    # Internal composition
    # -------------------------

    def _build_benefits(self, product: dict) -> list:
        return build_benefits_block(product)

    def _build_usage(self, product: dict) -> dict:
        return build_usage_block(product)

    def _build_safety(self, product: dict) -> dict:
        return build_safety_block(product)

    def _build_pricing(self, product: dict) -> dict:
        return build_pricing_block(product)
