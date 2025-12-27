Multi-Agent Content Generation System

1. Problem Statement

Modern content platforms often need to generate large volumes of structured, reusable content from limited structured data (for example, product catalogs).
Traditional approaches rely on monolithic scripts or tightly coupled logic, making systems hard to scale, extend, or maintain.

The objective of this project is to design and implement a production-style agentic automation system that transforms a small, fixed product dataset into multiple machine-readable content pages, while demonstrating:

clear agent boundaries

modular system design

reusable content logic

deterministic, structured outputs

The focus is on engineering design and automation, not creative content writing or UI development.

2. Solution Overview

This project implements a multi-agent content generation pipeline that processes a single product dataset and automatically produces:

an FAQ page (categorized user questions),

a product description page,

a comparison page against a fictional product,

all as clean JSON outputs.

The system is intentionally designed as a set of cooperating agents, each with a single responsibility, coordinated by a thin orchestrator.
Reusable logic blocks and declarative templates ensure that the system is extensible and maintainable.

Key design goals:

separation of concerns

composability

determinism

machine-readability

3. Scope & Assumptions
In Scope

Processing a single structured product dataset

Rule-based generation of user questions

Template-driven assembly of multiple content pages

JSON-only, machine-readable outputs

Deterministic execution (same input → same output)

Out of Scope

External data sources or research

LLM prompting or creative text generation

UI or frontend development

Database persistence

Natural language optimization

Assumptions

The input product data is trusted and provided in the expected structure

All generated content must be strictly derived from the given dataset

The fictional comparison product is intentionally minimal and static

4. System Architecture
4.1 High-Level Architecture

The system follows a layered agentic architecture:

Raw Product Data
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


A central Orchestrator manages execution order and data flow but does not perform any transformation or business logic.

4.2 Design Principles
Single-Responsibility Agents

Each agent performs exactly one task and exposes a clear input/output contract.

Reusable Logic Blocks

All domain-specific logic is implemented as pure functions, independent of agents and templates.

Template-Driven Assembly

Page structure is defined declaratively via templates, not hardcoded logic.

Machine-Readable First

All intermediate and final artifacts are structured objects. Final outputs are valid JSON.

5. Agent Design & Responsibilities
5.1 ProductParserAgent

Responsibility

Validate raw product input

Normalize data into a canonical internal model

Input

Raw product dataset

Output

Normalized product object with stable field structure

Key Characteristics

Pure transformation

No content generation

No page awareness

5.2 QuestionGenerationAgent

Responsibility

Automatically generate categorized user questions

Derive questions using deterministic, rule-based logic

Input

Normalized product model

Output

Dictionary of categorized questions (Informational, Usage, Safety, Purchase, Comparison)

Key Characteristics

No answers

No formatting

Represents user intent discovery only

5.3 ContentBlockAgent

Responsibility

Compose reusable content blocks by invoking logic functions

Input

Normalized product model

Output

Named content blocks (benefits, usage, safety, pricing)

Key Characteristics

Page-agnostic

Reusable across multiple templates

No orchestration logic

5.4 TemplateAssemblyAgent

Responsibility

Assemble page-level structures using declarative templates

Input

Template definition

Required data fields

Output

Structured page object

Key Characteristics

Generic and template-driven

No content generation

Enforces required fields

5.5 OutputValidationAgent

Responsibility

Validate assembled pages before serialization

Enforce page-type–specific structural rules

Input

Assembled page object

Output

Validated page or explicit error

Key Characteristics

Acts as a final gatekeeper

No data mutation

Ensures machine-readability

6. Reusable Logic Blocks

Logic blocks are implemented as pure functions that transform structured input into structured output.

Examples include:

benefits extraction

usage structuring

safety information aggregation

pricing normalization

product comparison assembly

These blocks:

have no side effects

contain no orchestration logic

are independently testable

are reusable across page types

7. Templates

Templates are data-only JSON definitions that specify:

page type

required fields

structural expectations

Templates do not:

generate content

apply formatting rules

contain logic

This allows new page types to be added by defining new templates without modifying existing agents.

8. Orchestration Flow

The orchestrator coordinates execution as a deterministic step pipeline:

Parse and normalize product data

Generate categorized user questions

Build reusable content blocks

Assemble pages using templates

Validate outputs

Write final JSON files

The orchestrator contains no business logic, ensuring agents remain reusable and independently testable.

9. Testing Strategy

Testing is performed at the component level, not via end-to-end mocks.

Logic blocks are tested in isolation for correctness and determinism

Template assembly is tested for required-field enforcement

Validation agent is tested for acceptance and rejection cases

This approach ensures correctness while avoiding unnecessary complexity.

10. Extensibility & Maintainability

The system is designed to scale naturally:

New page types → add new templates

New content rules → add new logic blocks

New workflows → add new agents

Existing agents and logic blocks remain unchanged, minimizing regression risk.

11. Design Rationale

This architecture mirrors real-world production agentic systems where:

responsibilities are explicit,

logic is composable,

orchestration is transparent,

outputs are deterministic and machine-consumable.

The system demonstrates engineering maturity rather than content creativity.

12. Conclusion

This project successfully demonstrates the design and implementation of a modular, agentic content generation system with:

clear agent boundaries,

reusable logic blocks,

declarative templates,

deterministic JSON outputs.

The resulting system is readable, extensible, and aligned with production-grade automation principles.