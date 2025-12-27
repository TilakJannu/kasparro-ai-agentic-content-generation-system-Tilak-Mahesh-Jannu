Multi-Agent Content Generation System
1. Introduction

Modern digital platforms often need to generate consistent, structured content (FAQs, product pages, comparisons) from limited structured data such as product catalogs.
Many systems solve this using monolithic scripts, which quickly become difficult to extend, test, or maintain.

This project addresses that problem by designing a modular, agentic content generation system.
Instead of one large script, the system is composed of independent agents, reusable logic blocks, and declarative templates that work together to produce machine-readable content pages.

The focus of this project is system design and automation, not creative writing or UI development.

2. What the System Does

Given a single structured product dataset, the system automatically generates:

an FAQ page containing categorized user questions,

a Product Description page built from reusable content blocks,

a Comparison page against a fictional but structured product,

All outputs are produced as clean JSON files, suitable for APIs, CMS pipelines, or further automation.

The system is deterministic:

the same input will always produce the same output.

3. Design Philosophy

The system is built around four core principles:

1. Single Responsibility

Each agent does one job only, with a clear input and output.

2. Separation of Concerns

Agents coordinate work

Logic blocks transform data

Templates define structure

The orchestrator manages flow

No layer does another layer’s job.

3. Reusability

Logic blocks and agents are designed to be reused across:

multiple page types

different products

future workflows

4. Machine-First Output

All outputs are structured JSON — not prose — ensuring reliability and downstream compatibility.

4. System Architecture Overview

At a high level, the system works as a step-based agent pipeline:

Product Data
   ↓
ProductParserAgent
   ↓
QuestionGenerationAgent
   ↓
ContentBlockAgent
   ↓
TemplateAssemblyAgent
   ↓
OutputValidationAgent
   ↓
JSON Outputs


A thin Orchestrator coordinates execution but contains no business logic.

5. Agent Responsibilities
5.1 ProductParserAgent

Purpose: Normalize and validate raw product input.

Converts raw product data into a canonical internal model

Ensures consistent field structure for downstream agents

Performs no content generation

This agent acts as the foundation of the pipeline.

5.2 QuestionGenerationAgent

Purpose: Discover user intent.

Automatically generates categorized user questions

Uses rule-based logic derived from product attributes

Produces no answers and no formatting

This agent answers the question:

“What would users naturally ask about this product?”

5.3 ContentBlockAgent

Purpose: Build reusable content components.

Invokes pure logic blocks to extract benefits, usage, safety, and pricing

Produces named, structured content blocks

Has no knowledge of pages or templates

These blocks are reusable across multiple page types.

5.4 TemplateAssemblyAgent

Purpose: Assemble pages using templates.

Reads declarative templates

Injects required data fields

Produces page-level structured objects

It performs composition only, with no content logic.

5.5 OutputValidationAgent

Purpose: Act as the final safety gate.

Validates page structure based on page type

Ensures required fields are present

Rejects invalid or incomplete outputs

This guarantees machine-readable correctness.

6. Reusable Logic Blocks

Logic blocks are implemented as pure functions that:

accept structured input,

return structured output,

contain no side effects.

Examples include:

extracting benefits,

structuring usage instructions,

aggregating safety information,

normalizing pricing,

assembling comparison data.

Because they are pure and isolated, these blocks are easy to test and reuse.

7. Templates

Templates are data-only JSON definitions that describe:

page type,

required fields,

structural expectations.

They do not contain:

logic,

conditionals,

content generation.

This makes the system easy to extend — new pages can be added by defining new templates without modifying agents.

8. Orchestration Flow

The orchestrator executes the pipeline in a clear, deterministic order:

Parse and normalize product data

Generate categorized user questions

Build reusable content blocks

Assemble pages using templates

Validate outputs

Write final JSON files

The orchestrator is intentionally thin and transparent.

9. Testing Strategy

Testing is performed at the component level:

Logic blocks are tested independently

Template assembly is tested for contract enforcement

Output validation is tested for acceptance and rejection cases

This ensures correctness without unnecessary complexity.

10. Extensibility

The system is designed to scale naturally:

New page types → add new templates

New content rules → add new logic blocks

New workflows → add new agents

Existing components remain unchanged, minimizing risk.

11. Conclusion

This project demonstrates how a production-style agentic system can be built using:

clear agent boundaries,

reusable logic blocks,

declarative templates,

deterministic orchestration.

The result is a clean, extensible, and maintainable content automation pipeline aligned with real-world engineering practices.