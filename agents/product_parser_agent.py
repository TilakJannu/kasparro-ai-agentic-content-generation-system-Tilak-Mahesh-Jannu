class ProductParserAgent:
    """
    Responsibility:
    - Validate raw product input
    - Normalize it into a canonical internal product model

    This agent performs:
    ✔ validation
    ✔ normalization

    This agent does NOT perform:
    ✘ content generation
    ✘ formatting
    ✘ orchestration
    """

    REQUIRED_FIELDS = [
        "name",
        "concentration",
        "skin_type",
        "key_ingredients",
        "benefits",
        "how_to_use",
        "side_effects",
        "price"
    ]

    def run(self, raw_data: dict) -> dict:
        """
        Entry point for the agent.
        """
        self._validate_input(raw_data)
        normalized_product = self._normalize(raw_data)
        return normalized_product

    def _validate_input(self, raw_data: dict):
        """
        Ensures all required fields are present.
        """
        missing_fields = [
            field for field in self.REQUIRED_FIELDS
            if field not in raw_data
        ]

        if missing_fields:
            raise ValueError(
                f"Missing required product fields: {missing_fields}"
            )

    def _normalize(self, raw_data: dict) -> dict:
        """
        Converts raw product data into a stable internal schema
        used consistently across the system.
        """
        return {
            "name": raw_data["name"],
            "attributes": {
                "concentration": raw_data["concentration"],
                "skin_type": self._ensure_list(raw_data["skin_type"]),
                "ingredients": self._ensure_list(raw_data["key_ingredients"]),
                "benefits": self._ensure_list(raw_data["benefits"]),
                "usage": raw_data["how_to_use"],
                "side_effects": raw_data["side_effects"],
                "price": raw_data["price"]
            }
        }

    def _ensure_list(self, value):
        """
        Normalizes values into lists for downstream consistency.
        """
        if isinstance(value, list):
            return value
        return [value]
