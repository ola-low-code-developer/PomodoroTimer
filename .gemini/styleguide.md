# Style Guide

This document outlines the coding style and conventions for this project.

## Python

*   **Code Style:** Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
*   **Docstrings:** Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
*   **Typing:** Use type hints for all function signatures.

## Pre-commit Hooks

This project uses pre-commit hooks to enforce code style and quality. To install the hooks, run in a virtual environement:

```bash
pip install -r requirements-dev.txt
pre-commit install
```

To run the hooks on all files, use:

```bash
pre-commit run --all-files
```
