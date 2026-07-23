# Gemini Autonomous Software Engineer Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/Google-Gemini%202.0%20Flash-4285F4?logo=google&logoColor=white" alt="Google Gemini 2.0 Flash" />
  <img src="https://img.shields.io/badge/Google%20GenAI-SDK-34A853?logo=google&logoColor=white" alt="Google GenAI SDK" />
  <img src="https://img.shields.io/badge/uv-Package%20Manager-5C4EE5" alt="uv Package Manager" />
  <img src="https://img.shields.io/badge/Architecture-Agentic%20Loop-orange" alt="Agentic Loop Architecture" />
  <img src="https://img.shields.io/badge/AI-Function%20Calling-red" alt="Function Calling" />
</p>

## Overview

Gemini Autonomous Software Engineer Agent is an AI-powered coding assistant built with Google Gemini 2.0 Flash. The agent can navigate codebases, analyze source files, execute Python scripts, identify bugs, and apply targeted fixes through an iterative decision-making process.

Designed around modern agentic patterns, the system follows an Observe → Analyze → Act workflow. This allows it to solve software engineering tasks with limited human intervention while operating within a controlled working environment.

---

## Tech Stack

| Category | Technology |
|---|---|
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

- Navigates project directories and repository structures.
- Identifies files relevant to a given task.
- Builds contextual understanding of the codebase.

### Source Code Analysis

- Reads and interprets source code across multiple files.
- Maintains context throughout the execution cycle.
- Understands dependencies and relationships between files.

### Automated Code Modification

- Applies targeted code changes.
- Fixes bugs and implementation issues.
- Refactors code while preserving intended behavior.

### Script Execution and Validation

- Executes Python scripts to validate proposed solutions.
- Uses execution feedback to refine subsequent actions.
- Supports iterative debugging and verification workflows.

### Context and Execution History

- Tracks conversation history and prior actions.
- Stores tool outputs during the active session.
- Supports multi-step reasoning across complex tasks.

---

## Architecture

The agent operates through a continuous decision-making loop:

```text
Observe
   ↓
Analyze Context
   ↓
Select Tool
   ↓
Execute Action
   ↓
Evaluate Result
   ↓
Repeat Until Task Completion
```

This architecture allows the system to progressively improve its understanding of the task and adjust its approach based on execution results.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-autonomous-agent.git
cd gemini-autonomous-agent
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> Never commit your `.env` file or API keys to version control.

### 3. Install Dependencies

```bash
uv sync
```

### 4. Run the Agent

Example task:

```bash
uv run main.py   "Fix the bug in the calculator app: 3 + 7 * 2 shouldn't be 20."   --verbose
```

---

## Security and Sandboxing

The agent operates within a designated working directory, ensuring that file access and modifications remain restricted to a controlled environment.

This design reduces the risk of unintended changes outside the target workspace and provides a safer foundation for experimenting with autonomous code execution.

---

## Use Cases

- Repository exploration and codebase analysis.
- Automated debugging of Python applications.
- Targeted source code modifications.
- Iterative script execution and validation.
- Prototyping tool-enabled AI agents.
- Exploring safe patterns for autonomous software engineering workflows.

---

## Project Scope

This project focuses on the orchestration layer of an autonomous coding agent, including:

- Agentic reasoning loops.
- Function calling.
- Tool selection and execution.
- Context management.
- Source code inspection.
- Controlled file modification.
- Execution-based validation.

It is intended as a practical implementation of an AI agent capable of interacting with local software projects through explicit tools and operational constraints.

---

## Author

### Ignacio Robles

Cloud Engineer | Full-Stack Developer | AI Solutions Builder

Building intelligent systems that connect AI agents with business data, software products, and cloud-native architectures.

- GitHub: https://github.com/your-profile
- LinkedIn: https://linkedin.com/in/your-profile
- Website: https://yourwebsite.com
