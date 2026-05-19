# python-learning-notes

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Personal Python study notes, snippets, and small exercises with a **civil & environmental engineering** flavour. Maintained as part of my Master's coursework at *Technische Hochschule Deggendorf* (THD), Germany.

## Why this repo

Most Python tutorials are generic. As a civil engineer I keep needing examples that map to real engineering tasks: unit handling, parsing tabular lab data, numerical integration for hydraulics, simple FEM concepts, etc. This repo is my running notebook.

## Structure

```
python-learning-notes/
├── 01_basics/            # syntax, types, control flow
├── 02_numpy_pandas/      # array & dataframe patterns for lab data
├── 03_plotting/          # matplotlib recipes
├── 04_engineering/       # small engineering scripts (units, beams, hydraulics)
└── 05_exercises/         # solved exercises from THD courses
```

## How to use

```bash
git clone https://github.com/koosha77/python-learning-notes
cd python-learning-notes
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Contributing

This is primarily a personal notebook, but pull requests with corrections, idiomatic improvements, or additional engineering examples are welcome. See `CONTRIBUTING.md`.

## License

MIT — free to use, copy and adapt with attribution.
