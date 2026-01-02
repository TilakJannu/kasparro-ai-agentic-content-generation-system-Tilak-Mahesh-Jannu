import json
import os

from core.state import Blackboard
from data.input_product import PRODUCT_DATA

from agents.product_parser_agent import ProductParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_block_agent import ContentBlockAgent
from agents.template_assembly_agent import TemplateAssemblyAgent
from agents.faq_page_agent import FAQPageAgent
from agents.comparison_page_agent import ComparisonPageAgent
from agents.output_validation_agent import OutputValidationAgent


def run_pipeline():
    state = Blackboard(PRODUCT_DATA)

    agents = [
        ProductParserAgent(),
        QuestionGenerationAgent(),
        ContentBlockAgent(),
        TemplateAssemblyAgent(),
        FAQPageAgent(),
        ComparisonPageAgent(),
        OutputValidationAgent()
    ]

    progress = True
    while progress:
        progress = False
        for agent in agents:
            if agent.can_act(state):
                agent.act(state)
                progress = True

    os.makedirs("outputs", exist_ok=True)

    for page_name, page in state.pages.items():
        if page_name in state.validated_pages:
            with open(
                f"outputs/{page_name}.json",
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(page, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    run_pipeline()
