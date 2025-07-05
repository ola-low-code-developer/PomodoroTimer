# Gemini CLI Usage Guide for this Project

This document provides guidelines and best practices for interacting with the Gemini CLI agent within this project. Following these recommendations will help you leverage the agent effectively, maintain code quality, and ensure smooth collaboration.

## 1. Understanding the Gemini CLI

The Gemini CLI is an interactive agent designed to assist with software engineering tasks directly from your command line. It can help with:
*   Fixing bugs
*   Adding features
*   Refactoring code
*   Explaining code
*   Generating new application prototypes
*   Managing files and directories
*   Running shell commands

## 2. Key Interaction Principles

To get the most out of the Gemini CLI, keep the following principles in mind:

### a. Provide Clear and Concise Instructions
Be specific about what you want the agent to do. The more precise your instructions, the better the outcome.

**Good Example:**
"Refactor `app/main.py` to use `pathlib` for file operations instead of `os.path`."

**Less Effective Example:**
"Change `main.py`."

### b. Provide Sufficient Context
When asking the agent to modify code, ensure it has access to all necessary context. This often means mentioning relevant files or directories. The agent can read files and search content, so guide it to the information it needs.

### c. Break Down Complex Tasks
For large features or refactorings, break them into smaller, manageable steps. This allows for incremental progress and easier review.

### d. Review and Confirm Changes
Always review the changes proposed by the agent before confirming. The agent will typically show you a diff or the new file content.

## 3. "Plan Mode" Explained

The Gemini CLI often operates in a "plan mode" for significant tasks. This is a crucial safety and efficiency feature:

("Plan Mode" Instructions

You are operating in Plan Mode. You may inspect files, analyze the codebase, and create a detailed implementation plan, but you are strictly forbidden from making any modifications or running commands that alter the system.)

*   **Purpose:** Before making any modifications, the agent will propose a plan of action. This plan outlines the steps it intends to take, the files it will interact with, and the rationale behind its approach.
*   **Your Role:** You *must* review and approve this plan. This gives you control over the changes and allows you to provide feedback or adjust the strategy before any code is written.
*   **Benefits:**
    *   **Transparency:** You understand the agent's thought process.
    *   **Control:** You can steer the agent if its initial plan isn't aligned with your expectations.
    *   **Safety:** Prevents unintended or destructive changes.
    *   **Efficiency:** Ensures the agent is on the right track, reducing the need for rollbacks.

## 4. Project-Specific Context and Conventions

The Gemini CLI is configured to respect this project's conventions.

### a. Code Style and Quality
This project adheres to the guidelines outlined in `.gemini/styleguide.md`. The agent is aware of these standards and will strive to produce code that complies with them.

### b. Dependencies and Environment
The project uses a `venv/` for dependency management. The agent will typically assume this environment for running commands like `pip install` or `pytest`.

### c. Logging
The application uses Python's `logging` module. You can enable debug logging by running the application with the `--debug` flag:
```bash
python -m app.main --debug
```

## 5. Configuration

The agent's default behavior can be influenced by the settings in `.gemini/config`. This file contains settings such as the default model, temperature, and maximum tokens.

## 6. History

Your interaction history with the Gemini CLI is stored in `.gemini/history`. This can be useful for reviewing past sessions or understanding previous decisions.

## 7. General Good Practices

*   **Be Explicit with Paths:** When referring to files, use absolute paths or paths relative to the project root to avoid ambiguity.
*   **Verify Tool Outputs:** Pay attention to the output of tool calls (e.g., `read_file`, `run_shell_command`) to ensure they executed as expected.
*   **Iterate and Refine:** Don't expect perfect results on the first try. Use the agent as an assistant, iterating on instructions and refining its output.
*   **Use `git status` and `git diff`:** Regularly check the state of your repository to understand what changes the agent has made or is proposing.
