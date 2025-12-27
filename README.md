Multi-Agent Content Generation System
What does this system do?

This project implements a modular, multi-agent automation system that converts a structured product dataset into machine-readable content pages.

Given a single product input, the system autonomously generates:

an FAQ page (categorized user questions),

a Product description page,

a Comparison page (against a fictional product),

all as clean JSON outputs, suitable for downstream automation.

Is this agentic or monolithic?

✔ Agentic, not monolithic

The system is built as a pipeline of single-responsibility agents, coordinated by a thin orchestrator.

Key characteristics:

each agent has a clear input/output contract

reusable logic blocks are isolated from agents

templates are declarative and data-only

no “one big script” or hidden global state

This mirrors real production agentic systems.

How do I run it?
Prerequisites

Python 3.9+

Run the full pipeline

From the project root:

python -m orchestrator.pipeline

Outputs

After a successful run, the following files are generated:

outputs/
  faq.json
  product_page.json
  comparison_page.json


No external APIs, models, or configuration are required.

Where is the system design explained?

📄 Detailed system design documentation is available here:

docs/projectdocumentation.md


This document explains:

agent responsibilities and boundaries

orchestration flow

reusable logic blocks

template-driven assembly

design assumptions and constraints