# Gemini Autonomous Software Engineer Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Google-Gemini%202.0%20Flash-4285F4?logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20GenAI-SDK-34A853?logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/uv-Package%20Manager-5C4EE5" />
  <img src="https://img.shields.io/badge/Architecture-Agentic%20Loop-orange" />
  <img src="https://img.shields.io/badge/AI-Function%20Calling-red" />
</p>

## Overview

Gemini Autonomous Software Engineer Agent is an AI-powered coding assistant built with Google Gemini 2.0 Flash. The agent can autonomously navigate codebases, analyze source files, execute Python scripts, identify bugs, and apply fixes through an iterative reasoning process.

Designed around modern agentic patterns, the system follows an Observe → Think → Act workflow, enabling it to solve software engineering tasks with minimal human intervention while operating inside a secure sandboxed environment.

---

## Tech Stack

| Category | Technology |
|-----------|------------|
| AI Model | Google Gemini 2.0 Flash |
| SDK | Google GenAI SDK |
| Language | Python 3.11+ |
| Package Manager | uv |
| Architecture | Agentic Loop |
| Capabilities | Function Calling, Tool Orchestration, Context Management |
| Security | Sandboxed File Operations |

---

## Key Features

### Autonomous Repository Exploration

- Navigates project structures and directories.
- Identifies relevant files for a given task.
- Builds contextual understanding of the codebase.

### Source Code Analysis

- Reads and interprets source code across multiple files.
- Maintains context throughout the reasoning process.
- Understands dependencies and file relationships.

### Automated Code Modification

- Applies targeted code changes.
- Fixes bugs and implementation issues.
- Refactors code while preserving intended behavior.

### Script Execution and Validation

- Executes Python scripts to validate solutions.
- Uses execution feedback to refine decisions.
- Supports iterative debugging workflows.

### Persistent Agent Memory

- Tracks conversation history.
- Stores tool outputs and previous actions.
- Enables multi-step autonomous reasoning.

---

## Architecture

The agent operates through a continuous decision-making loop:

text Observe    ↓ Analyze Context    ↓ Select Tool    ↓ Execute Action    ↓ Evaluate Result    ↓ Repeat Until Task Completion 

This architecture allows the system to iteratively improve its understanding and approach until the requested objective is achieved.

---

## Installation

### Clone the Repository

bash git clone https://github.com/your-username/gemini-autonomous-agent.git cd gemini-autonomous-agent 

### Configure Environment Variables

Create a .env file:

env GEMINI_API_KEY=your_api_key_here 

### Install Dependencies

bash uv sync 

### Run the Agent

Example task:

bash uv run main.py \ "Fix the bug in the calculator app: 3 + 7 * 2 shouldn't be 20." \ --verbose 

---

## Security and Sandboxing

The agent operates within a designated working directory, ensuring all file modifications remain restricted to a controlled environment.

This project demonstrates how autonomous AI systems can safely interact with local codebases through carefully designed operational guardrails.

---

## Learning Objectives

This project explores practical applications of:

- Agentic AI Systems
- Autonomous Reasoning Loops
- Function Calling
- Tool-Based AI Architectures
- Code Generation and Refactoring
- Context-Aware Decision Making
- Safe AI Execution Environments

---

## Acknowledgements

Special thanks to Boot.dev for promoting a hands-on, project-driven approach to software engineering education. Their practical methodology served as a strong source of inspiration throughout the development of this project.

---

## Author

### Ignacio Robles

Cloud Engineer | Fullstack Dev | AI Solutions Builder

Building intelligent systems that connect AI agents with real-world business data and cloud-native architectures.

- GitHub: https://github.com/your-profile
- LinkedIn: https://linkedin.com/in/your-profile
- Website: https://yourwebsite.com
