# Contributing to Awesome Agent Frameworks

Thank you for helping keep this list useful. This repository is a curated awesome list, not a comprehensive directory. Entries should help developers discover frameworks and tools for building, running, connecting, evaluating, or observing agent systems.

## Scope

Good submissions usually fit one of these categories:

- Agent SDK / framework
- Agent graph / runtime
- RAG / knowledge system
- Memory / context system
- Low-code builder / agent app
- Tool / protocol / connector layer
- Developer / computer-use agent
- Data / ingestion / MLOps substrate
- Observability / evals
- Model serving / gateway
- Database / infrastructure product
- Protocol / standard only

Submissions may be declined when they are general AI resources, generic DevOps tools, model lists, prompt collections, unrelated infrastructure, promotional pages, or projects without enough documentation to evaluate.

## Entry Format

Entries are stored in [`data/frameworks.json`](data/frameworks.json). Add or edit
the JSON object for the project, including its `name`, `category`, GitHub `url`,
`repo`, and short neutral `description`.

The generated README entry must use this format:

```markdown
- [Name](https://github.com/owner/repo) ![GitHub Repo stars](https://img.shields.io/github/stars/owner/repo?style=social) - Short neutral description.
```

Requirements:

- Use the canonical project name.
- Link the name to the canonical GitHub repository.
- Include a valid GitHub repository stars badge from `shields.io`.
- Keep the description short, factual, and neutral.
- Start descriptions with a capital letter and end them with a period.
- Do not use marketing claims, hype, emojis, or subjective praise.
- Do not include per-entry metadata such as product form, execution model, or persistence topology.

## Sorting and Categories

- Put the entry in the single best category.
- Keep entries alphabetically sorted within each category by project name.
- Do not add duplicate projects under multiple names.
- Do not add alternate links for the same project as separate entries.
- Run `python3 scripts/generate-readme.py` after editing `data/frameworks.json`.
- Run `python3 scripts/generate-readme.py --check` to verify the README is current.
- Run `python3 scripts/validate-data.py` to lint the JSON data and generated README.
- Include both `data/frameworks.json` and the regenerated `README.md` in the pull request.
- Do not edit generated README entries directly without updating `data/frameworks.json`.

## Pull Request Checklist

Before opening a pull request, confirm:

- [ ] The project fits this repository's scope.
- [ ] The project URL and GitHub repository URL both work.
- [ ] The entry uses the required format.
- [ ] The description is objective and concise.
- [ ] The entry is in the right category.
- [ ] The category remains alphabetically sorted.
- [ ] The project is not already listed.
- [ ] `data/frameworks.json` was updated.
- [ ] `python3 scripts/generate-readme.py` was run and the regenerated `README.md` is included.
- [ ] `python3 scripts/generate-readme.py --check` passes.
- [ ] `python3 scripts/validate-data.py` passes.

Final decisions on inclusion, category placement, and wording rest with the maintainers.
