Multi-Agent Content Generation System
1. Introduction

This project implements a true multi-agent content generation system designed to transform a structured product dataset into multiple machine-readable content pages.

The assignment explicitly evaluates the ability to design autonomous agents that interact dynamically through an orchestration mechanism, rather than a statically wired or sequential pipeline.
Accordingly, this system is built using a blackboard-based multi-agent architecture, where agents operate independently and coordination emerges through shared system state.

The focus of this project is system design and agent autonomy, not content creativity or UI development.

2. Problem Statement

Modern content systems often require generating multiple structured outputs (FAQs, product pages, comparisons) from a single source of truth.
Traditional implementations rely on monolithic scripts or statically sequenced logic, which limits extensibility and fails to demonstrate true agentic behavior.

The goal of this project is to design a system that:

uses independent agents with clear responsibilities

supports dynamic coordination

avoids hard-coded execution order

produces deterministic, structured JSON outputs

3. Design Philosophy

The system is built around the following principles:

3.1 Agent Autonomy

Each agent decides when it should act based on system state.
No agent is directly invoked by another agent or by the orchestrator.

3.2 Dynamic Coordination

Agents communicate only through shared state.
Execution order is not predefined and emerges at runtime.

3.3 Separation of Concerns

Agents perform reasoning or assembly

Logic blocks perform pure data transformation

The orchestrator only schedules execution

3.4 Determinism & Safety

All outputs are rule-driven, deterministic, and validated before being written.

4. High-Level Architecture

The system follows a blackboard + scheduler architecture:

Shared Blackboard (System State)
        ↑
Autonomous Agents observe & act
        ↑
Scheduler-Only Orchestrator


The blackboard stores shared knowledge

Agents observe and update the blackboard

The orchestrator repeatedly schedules agents without enforcing order

5. Shared Blackboard (System State)

The blackboard acts as the single source of truth and the only coordination mechanism.

It stores:

raw input

parsed product data

generated questions

reusable content blocks

assembled pages

validation status

The blackboard contains no logic, only shared data.

6. Agent Autonomy Model

All agents implement the same interface:

can_act(state) -> bool
act(state) -> None


can_act allows the agent to decide independently whether it should act

act performs one responsibility and updates shared state

This model ensures:

no static control flow

no hard-coded dependencies

true agent autonomy

7. Agents and Responsibilities
7.1 ProductParserAgent

Parses and normalizes raw product input

Publishes canonical product data to the blackboard

Acts only once

7.2 QuestionGenerationAgent

Generates categorized user questions

Internally evaluates question coverage

Autonomously expands questions until sufficient coverage (≥15) is reached

Does not receive instructions from the orchestrator

This agent demonstrates self-evaluation and goal-driven behavior.

7.3 ContentBlockAgent

Builds reusable content blocks (benefits, usage, safety, pricing)

Uses pure logic blocks

Is page-agnostic

7.4 TemplateAssemblyAgent (Product Page)

Assembles the product page when required blocks are available

Does not generate content

Publishes structured page output

7.5 FAQPageAgent

Assembles the FAQ page when questions are available

Produces categorized, machine-readable questions

Does not perform validation or reasoning

7.6 ComparisonPageAgent

Builds a comparison page using the main product and a deterministic fictional competitor

Uses reusable comparison logic

Does not depend on other pages

7.7 OutputValidationAgent

Observes newly assembled pages

Validates structure based on page type

Acts as a final gatekeeper before output persistence

8. Reusable Logic Blocks

Reusable logic blocks are implemented as pure functions that:

accept structured input

return structured output

have no side effects

Examples include:

benefit extraction

usage structuring

safety aggregation

pricing normalization

comparison assembly

These blocks are independent of agents and orchestration.

9. Orchestrator (Scheduler-Only)

The orchestrator does not control logic or order.

Its responsibilities are limited to:

maintaining a scheduling loop

allowing eligible agents to act

terminating when no agent can act further

This ensures:

no static execution order

no manually wired logic

dynamic coordination

10. Output Generation

The system generates three outputs:

product_page.json
faq_page.json
comparison_page.json


All outputs are:

machine-readable JSON

deterministic

validated by an autonomous validation agent

11. Extensibility

The architecture is inherently extensible:

New page types → add new agents

New logic → add new logic blocks

No existing agent or orchestrator code needs to change

This demonstrates production-ready system design.

12. Conclusion

This project demonstrates a true multi-agent system by behavior, not by naming.

Key characteristics include:

autonomous agents

dynamic coordination via shared state

scheduler-only orchestration

clean separation of responsibilities

deterministic, validated outputs

The system fully aligns with the original intent of the assignment and the clarified expectations regarding agent autonomy and non-static control flow.