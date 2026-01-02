# from core.state import Blackboard
# from data.input_product import PRODUCT_DATA

# state = Blackboard(PRODUCT_DATA)

# assert state.raw_input is not None
# assert state.product is None
# assert state.questions is None
# assert state.content_blocks == {}
# assert state.pages == {}
# assert state.validated_pages == set()

# print("Step 1 Blackboard initialized correctly")


# from core.agent_base import Agent

# class DummyAgent(Agent):
#     def can_act(self, state):
#         return True

#     def act(self, state):
#         print("Acting")

# # This should work without errors
# DummyAgent()
# print("Agent interface works correctly")

# from core.state import Blackboard
# from agents.product_parser_agent import ProductParserAgent
# from data.input_product import PRODUCT_DATA

# state = Blackboard(PRODUCT_DATA)
# agent = ProductParserAgent()

# assert agent.can_act(state) is True
# agent.act(state)
# assert state.product is not None
# assert agent.can_act(state) is False

# print("Step 3 ProductParserAgent works correctly")

# from core.state import Blackboard
# from agents.question_generation_agent import QuestionGenerationAgent
# from agents.product_parser_agent import ProductParserAgent
# from data.input_product import PRODUCT_DATA

# state = Blackboard(PRODUCT_DATA)

# parser = ProductParserAgent()
# question_agent = QuestionGenerationAgent()

# assert question_agent.can_act(state) is False

# parser.act(state)
# assert question_agent.can_act(state) is True

# question_agent.act(state)
# assert state.questions is not None
# assert question_agent.can_act(state) is False

# print("Step 4 QuestionGenerationAgent works correctly")
# from core.state import Blackboard
# from agents.product_parser_agent import ProductParserAgent
# from agents.content_block_agent import ContentBlockAgent
# from data.input_product import PRODUCT_DATA

# state = Blackboard(PRODUCT_DATA)

# parser = ProductParserAgent()
# content_agent = ContentBlockAgent()

# assert content_agent.can_act(state) is False

# parser.act(state)
# assert content_agent.can_act(state) is True

# content_agent.act(state)
# assert state.content_blocks
# assert content_agent.can_act(state) is False

# print("Step 5 ContentBlockAgent works correctly")


# from core.state import Blackboard
# from agents.product_parser_agent import ProductParserAgent
# from agents.content_block_agent import ContentBlockAgent
# from agents.template_assembly_agent import TemplateAssemblyAgent
# from data.input_product import PRODUCT_DATA

# state = Blackboard(PRODUCT_DATA)

# parser = ProductParserAgent()
# content_agent = ContentBlockAgent()
# template_agent = TemplateAssemblyAgent()

# assert template_agent.can_act(state) is False

# parser.act(state)
# content_agent.act(state)

# assert template_agent.can_act(state) is True
# template_agent.act(state)

# assert "product_page" in state.pages
# assert template_agent.can_act(state) is False

# print("Step 6 TemplateAssemblyAgent works correctly")

# from core.state import Blackboard
# from agents.output_validation_agent import OutputValidationAgent

# state = Blackboard(raw_input={})
# state.pages["product_page"] = {
#     "page_type": "product_page",
#     "name": "Test Product",
#     "benefits_block": [],
#     "usage_block": {},
#     "safety_block": {},
#     "pricing_block": {}
# }

# validator = OutputValidationAgent()

# assert validator.can_act(state) is True
# validator.act(state)
# assert "product_page" in state.validated_pages
# assert validator.can_act(state) is False

# print("Step 7 OutputValidationAgent works correctly")


# from core.state import Blackboard
# from agents.faq_page_agent import FAQPageAgent

# state = Blackboard(raw_input={})
# state.questions = {
#     "Informational": ["What is this product?"]
# }

# agent = FAQPageAgent()

# assert agent.can_act(state) is True
# agent.act(state)

# assert "faq_page" in state.pages
# assert agent.can_act(state) is False

# print("Step 9 FAQPageAgent works correctly")

from core.state import Blackboard
from agents.comparison_page_agent import ComparisonPageAgent

state = Blackboard(raw_input={})
state.product = {
    "name": "GlowBoost Serum",
    "attributes": {
        "benefits": ["Brightening"],
        "price": 699
    }
}

agent = ComparisonPageAgent()

assert agent.can_act(state) is True
agent.act(state)

assert "comparison_page" in state.pages
assert agent.can_act(state) is False

print("Step 10 ComparisonPageAgent works correctly")
