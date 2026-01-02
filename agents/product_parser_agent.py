from core.agent_base import Agent

class ProductParserAgent(Agent):
    """
    Bootstrap agent responsible for parsing and normalizing
    raw product input data into a canonical internal format.

    This agent:
    - acts only once
    - publishes normalized product data to shared state
    - does not depend on any other agent
    """

    def can_act(self, state) -> bool:
        """
        The agent can act if:
        - raw input exists
        - product has not yet been parsed
        """
        return state.raw_input is not None and state.product is None

    def act(self, state) -> None:
        """
        Normalize raw product data and store it in shared state.
        """
        raw = state.raw_input

        state.product = {
            "name": raw["name"],
            "attributes": {
                "concentration": raw.get("concentration"),
                "skin_type": raw.get("skin_type"),
                "ingredients": raw.get("key_ingredients"),
                "benefits": raw.get("benefits"),
                "usage": raw.get("how_to_use"),
                "side_effects": raw.get("side_effects"),
                "price": raw.get("price")
            }
        }
