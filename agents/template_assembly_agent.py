class TemplateAssemblyAgent:
    """
    Responsibility:
    - Assemble structured pages using declarative templates

    This agent performs:
    ✔ template-based assembly
    ✔ structural composition

    This agent does NOT:
    ✘ generate content
    ✘ validate output
    ✘ orchestrate flow
    """

    def run(self, template: dict, data: dict) -> dict:
        """
        Entry point for the agent.

        Inputs:
        - template: declarative page template
        - data: dictionary containing all required fields

        Output:
        - Assembled page object
        """
        page = {
            "page_type": template["page_type"]
        }

        for field in template["fields"]:
            if field not in data:
                raise KeyError(
                    f"Missing required field '{field}' for page type '{template['page_type']}'"
                )
            page[field] = data[field]

        return page
