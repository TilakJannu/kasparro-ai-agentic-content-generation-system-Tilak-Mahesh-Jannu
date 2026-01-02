Multi-Agent Content Generation System
Overview

This project implements a true multi-agent content generation system that transforms a structured product dataset into multiple machine-readable content pages.

The system is designed to demonstrate agent autonomy, dynamic coordination, and non-static orchestration, as required by the Applied AI Engineer assignment.

Given a single product input, the system autonomously generates:

a Product Page

an FAQ Page (categorized user questions)

a Comparison Page (against a deterministic fictional product)

All outputs are produced as clean JSON, suitable for downstream automation.

Why This Is a True Multi-Agent System

This system is not a sequential pipeline.

It uses a blackboard-based agentic architecture, where:

agents are independent and autonomous

agents decide when to act based on shared state

agents never call each other directly

the orchestrator acts only as a scheduler

execution order emerges dynamically at runtime

Agent Autonomy Model

Each agent implements the same interface:

can_act(state) -> bool
act(state) -> None


Agents:

observe shared system state

decide independently when they can contribute

publish results back to the shared state

No agent knows what other agents exist.

System Architecture
Shared Blackboard (State)
        ↑
Autonomous Agents observe & act
        ↑
Scheduler-only Orchestrator

Core Components

Blackboard (core/state.py)
Shared system state used for indirect coordination

Agents (agents/)

ProductParserAgent

QuestionGenerationAgent (self-evaluating, goal-driven)

ContentBlockAgent

TemplateAssemblyAgent (Product Page)

FAQPageAgent

ComparisonPageAgent

OutputValidationAgent

Logic Blocks (logic_blocks/)
Pure, reusable functions for domain logic

Orchestrator (orchestrator/pipeline.py)
Scheduler loop that enables agents to act dynamically

Generated Outputs

After execution, the system produces:

outputs/
├── product_page.json
├── faq_page.json
└── comparison_page.json


All outputs are:

deterministic

machine-readable

validated by an autonomous validation agent

How to Run
Prerequisites

Python 3.9+

Run the System

From the project root:

python -m orchestrator.pipeline


No external APIs or models are required.

Key Design Decisions

Blackboard Pattern
Enables indirect, dynamic agent coordination

Scheduler-Only Orchestrator
Prevents static control flow

Self-Evaluating Agents
For example, the QuestionGenerationAgent autonomously decides when it has generated sufficient questions (≥15)

Strict Separation of Concerns
Parsing, reasoning, assembly, and validation are handled by different agents

Documentation

Detailed system design and architectural rationale are available in:

docs/projectdocumentation.md


This includes:

agent responsibilities

coordination model

extensibility strategy

design assumptions