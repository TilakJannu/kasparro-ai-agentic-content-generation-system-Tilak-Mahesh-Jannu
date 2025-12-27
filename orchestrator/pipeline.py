import json
import os

from data.input_product import PRODUCT_DATA
from agents.product_parser_agent import ProductParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_block_agent import ContentBlockAgent
from agents.template_assembly_agent import TemplateAssemblyAgent
from agents.output_validation_agent import OutputValidationAgent
from logic_blocks.comparison import build_comparison_block


# -------------------------
# Helpers
# -------------------------

def load_template(path: str) -> dict:
    """
    Loads a JSON template from disk.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_output(path: str, data: dict):
    """
    Writes JSON output to disk.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)



# -------------------------
# Orchestration Pipeline
# -------------------------

def run_pipeline():
    # Initialize agents
    parser = ProductParserAgent()
    question_agent = QuestionGenerationAgent()
    block_agent = ContentBlockAgent()
    assembler = TemplateAssemblyAgent()
    validator = OutputValidationAgent()

    # STEP 1–2: Parse product data
    product = parser.run(PRODUCT_DATA)

    # STEP 3: Generate questions
    questions = question_agent.run(product)

    # STEP 4–5: Build reusable content blocks
    blocks = block_agent.run(product)

    # -------------------------
    # FAQ PAGE
    # -------------------------
    faq_template = load_template("templates/faq_template.json")
    faq_page = assembler.run(
        faq_template,
        {"questions": questions}
    )
    faq_page = validator.run(faq_page)
    write_output("outputs/faq.json", faq_page)

    # -------------------------
    # PRODUCT PAGE
    # -------------------------
    product_template = load_template("templates/product_template.json")
    product_page_data = {
        "name": product["name"],
        **blocks
    }
    product_page = assembler.run(product_template, product_page_data)
    product_page = validator.run(product_page)
    write_output("outputs/product_page.json", product_page)

    # -------------------------
    # COMPARISON PAGE
    # -------------------------
    fictional_competitor = {
        "name": "RadiancePlus Serum",
        "ingredients": ["Vitamin C"],
        "benefits": ["Brightening"],
        "price": 899
    }

    comparison_block = build_comparison_block(product, fictional_competitor)

    comparison_template = load_template("templates/comparison_template.json")
    comparison_page = assembler.run(
        comparison_template,
        {"comparison": comparison_block}
    )
    comparison_page = validator.run(comparison_page)
    write_output("outputs/comparison_page.json", comparison_page)


# -------------------------
# Entry Point
# -------------------------

if __name__ == "__main__":
    run_pipeline()
