# Getting Started

This guide will help you create and set up a new Python project using the template.

## Creating a New Project

Ensure you have Copier installed:

```bash
python -m venv .copier_venv
source .copier_venv/bin/activate
pip install copier
```

Generate your project:

```bash
copier copy gh:pa-decarvalho/python-template path/to/your/git/repo
```

Delete the virtualenv

```bash
rm -rf .copier_venv
```

## Updating Your Project

Once your project is initialized and pushed to a repository, you can update it using Task commands:

```bash
# Update your project with the latest template changes
task copier:update

# Update your project while keeping your current answers as defaults
task copier:update-defaults
```

The `copier:update` command will pull the latest changes from the template and allow you to update your answers to the template questions.
The `copier:update-defaults` command will do the same but use your previous answers as default values, making it easier to update while maintaining your current configuration.
