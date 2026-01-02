class Blackboard:
    """
    Shared system state (blackboard) used by all agents.

    Responsibilities:
    - Store shared knowledge
    - Enable indirect agent coordination
    - Act as the single source of truth

    This class contains NO logic.
    """

    def __init__(self, raw_input: dict):
        # Raw input provided at system start
        self.raw_input = raw_input

        # Parsed / normalized product data
        self.product = None

        # Generated user questions
        self.questions = None

        # Reusable content blocks
        self.content_blocks = {}

        # Assembled pages (by page_type)
        self.pages = {}

        # Track which pages have been validated
        self.validated_pages = set()
