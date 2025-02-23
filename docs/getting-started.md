# Getting Started

This guide will help you create and set up a new Python project using the template.

## Creating a New Project

1. Ensure you have Copier installed:

```bash
python -m venv .copier_venv
source .copier_venv/bin/activate
pip install copier
```

2. Generate your project:

```bash
copier copy gh:pa-decarvalho/python-template path/to/your/git/repo
```

3. Delete the virtualenv

```bash
rm -rf .copier_venv
```
