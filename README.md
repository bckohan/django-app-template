# django-app-template

A [cookiecutter](https://cookiecutter.readthedocs.io) GitHub template for Django apps,
based on the tooling and workflow patterns from
[django-enum](https://github.com/django-commons/django-enum) and
[django-typer](https://github.com/django-commons/django-typer).

## Using This Template

### On GitHub (recommended)

1. Click **"Use this template"** → **"Create a new repository"**
2. After the repo is created, the **Bootstrap** GitHub Action will run automatically on your
   first push to `main`. It reads the repo name, owner, and description from GitHub's metadata
   and opens a PR with all template files rendered.
3. Review and merge the PR.
4. **Choose your test strategy** — delete one of the two test workflows:
   - Keep `test.yml`, delete `test-db.yml` — SQLite only (like django-typer)
   - Keep `test-db.yml`, delete `test.yml` — full DB matrix (like django-enum)

### Locally

```bash
uvx cookiecutter gh:YOUR_ORG/django-app-template
```

## What Gets Generated

| File | Description |
|------|-------------|
| `pyproject.toml` | hatchling build, uv dependency groups, ruff/mypy/pyright config |
| `justfile` | task runner (setup, test, lint, docs, release) |
| `src/<package>/` | source package with `__init__.py`, `apps.py`, `py.typed` |
| `tests/settings.py` | multi-DB Django settings (reads `RDBMS` env var) |
| `doc/` | Sphinx + Furo docs with ReadTheDocs config |
| `.github/workflows/test.yml` | SQLite testing on Linux + Windows + macOS |
| `.github/workflows/test-db.yml` | Full DB testing (Postgres, MySQL, MariaDB, Oracle) |
| `.github/workflows/lint.yml` | ruff + mypy + pyright static analysis |
| `.github/workflows/release.yml` | Automated PyPI publish on version tags |
| `.github/workflows/zizmor.yml` | CI security scanning |
| `.github/workflows/scorecard.yml` | OpenSSF Scorecard |
| `.github/workflows/update_coc.yml` | Auto-sync Code of Conduct from django-commons |
| `.pre-commit-config.yaml` | pre-commit hooks (lint, format, docs, package) |
| `.codecov.yml` | Codecov coverage config |
| `LICENSE` | MIT license |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` | Community files |

## Derived Variables

All values are derived automatically from GitHub repository metadata — no manual input needed:

| Variable | Source |
|----------|--------|
| `project_slug` | repository name |
| `package_name` | repository name with `-` → `_` |
| `description` | repository description |
| `author_name` | owner's GitHub display name |
| `author_email` | owner's public GitHub email (falls back to `@users.noreply.github.com`) |
| `github_owner` | repository owner (org or user) |
| `year` | current year |

## Tooling

- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Task runner:** [just](https://just.systems/)
- **Linter / formatter:** [ruff](https://docs.astral.sh/ruff/)
- **Type checking:** mypy + pyright
- **Docs:** Sphinx + Furo + ReadTheDocs
- **Tests:** pytest + pytest-django
- **CI:** GitHub Actions
