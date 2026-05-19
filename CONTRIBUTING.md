# Contributing to python-learning-notes

This is a personal learning repository — Python notes, snippets, and small exercises with a **civil & environmental engineering** flavour, maintained during my Master's program at **THD**.

## What contributions make sense here

- Bug fixes in example scripts
- Cleaner / more idiomatic Python rewrites of existing snippets
- Additional engineering-focused examples (hydraulics, structural mechanics, units, lab-data parsing)
- Documentation improvements and typo fixes

## How to contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/<short-name>`
3. Keep changes small and focused (one concept per PR)
4. Run any examples locally before opening a PR
5. Open a Pull Request describing the change and its purpose

## Code style

- Python 3.10+
- PEP 8, 4-space indentation
- Type hints where they add clarity
- Docstrings for non-trivial functions (Google or NumPy style)
- Prefer `pandas` / `numpy` for tabular and numerical work
- Keep dependencies minimal and pinned in `requirements.txt`

## File layout

- Group examples in numbered topic folders (e.g. `04_engineering/`)
- One concept per file; small, readable scripts over large modules
- Sample data goes into a `data/` subfolder where applicable

## Code of conduct

Be respectful and constructive. This is a learning space — questions and corrections are welcome.

