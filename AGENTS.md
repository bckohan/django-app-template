# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A [cookiecutter](https://cookiecutter.readthedocs.io/) GitHub template for bootstrapping new Django app repositories. The template is modeled after [django-enum](https://github.com/django-commons/django-enum) and [django-typer](https://github.com/django-commons/django-typer).

When a new repo is created from this template, `.github/workflows/bootstrap.yml` auto-runs on first push to `main`, derives all values from the GitHub API, renders the cookiecutter template in-place, and opens a PR.

## Repo Structure

- `cookiecutter.json` — template variables and `_copy_without_render` list
- `.github/workflows/bootstrap.yml` — one-shot bootstrap workflow
- `{{cookiecutter.project_slug}}/` — cookiecutter template directory

Everything inside `{{cookiecutter.project_slug}}/` is rendered by cookiecutter; the outer repo is the template scaffolding itself.

## Jinja2 Conflict Rules

**Workflow `.yml` files** are listed in `_copy_without_render` in `cookiecutter.json` so they are copied verbatim — this preserves `${{ }}` GitHub Actions syntax without Jinja2 trying to expand it.

**`justfile`** uses this workaround at the top:
```
{%- set lb = '{{' -%}
{%- set rb = '}}' -%}
```
All just `{{ VAR }}` syntax is written as `{{ lb }}VAR{{ rb }}`. The `test-all` recipe uses a `#!/usr/bin/env bash` shebang with bash `if [ -z "..." ]` syntax instead of just's `{{ if }}` expressions.

When adding new files to the template that use `{{ }}` syntax (just recipes, shell scripts, etc.), apply the same workarounds or add the file to `_copy_without_render`.

## Auto-Derived Variables

The bootstrap workflow derives these from GitHub — do not prompt for them:
- `project_slug` ← repository name
- `package_name` ← repo name with `-` → `_`
- `github_owner` ← `github.repository_owner`
- `author_name` ← GitHub API `/users/$owner` (fallback: login)
- `author_email` ← GitHub API (fallback: `owner@users.noreply.github.com`)
- `year` ← `date +%Y`

## Testing the Template

Smoke test — renders using default `cookiecutter.json` values:
```bash
rm -rf /tmp/cc-test && uvx cookiecutter . --no-input --output-dir /tmp/cc-test
```
Output lands at `/tmp/cc-test/my-django-app/`.

## Template Project Tooling (inside `{{cookiecutter.project_slug}}/`)

The generated project uses `just` as a task runner, `uv` for dependency management, and `hatchling` as the build backend.

### Setup
```bash
just setup        # create venv + install pre-commit hooks
just install      # install all dev dependencies via uv
```

### Tests
```bash
just test                      # run tests (SQLite)
just test-all                  # run all tests with coverage
just test-all psycopg3         # run with PostgreSQL backend
just test tests/test_foo.py    # run a specific file
just coverage                  # generate coverage report
```

### Linting / Formatting
```bash
just fix          # auto-fix lint + format (ruff)
just check        # run all static checks without modifying files
just precommit    # run pre-commit hooks
```

### Type Checking
```bash
just check-types  # runs both mypy and pyright
```

### Docs
```bash
just docs         # build Sphinx HTML and open in browser
just docs-live    # live-reload dev server
just check-docs   # lint docs with doc8
```

### Django Management
```bash
just manage migrate
just manage shell
just manage [any command]
```

## Test Strategy

Two workflow files are generated: `test.yml` (SQLite only, runs on Linux/Windows/macOS) and `test-db.yml` (full matrix: SQLite + PostgreSQL + MySQL + MariaDB + Oracle). After bootstrapping, the user deletes whichever they don't need.

`tests/settings.py` selects the database backend via the `RDBMS` environment variable (`sqlite`, `postgres`, `mysql`, `mariadb`, `oracle`).

### Django Version / DB Client Groups

Django version and database client are selected at test-run time via `uv` dependency groups — no lock-file pinning. The relevant groups defined in `pyproject.toml`:

- Django version groups (mutually conflicting): `dj42`, `dj52`, `dj60`
- PostgreSQL: `psycopg2`, `psycopg3` (mutually conflicting)
- MySQL/MariaDB: `mysqlclient14`, `mysqlclient2x` (mutually conflicting)
- Oracle: `cx_oracle`, `oracledb` (mutually conflicting)

CI passes these as `--group` flags directly to `just test-all`:
```
just test-all --group psycopg3 -p "$TEST_PYTHON" --group dj52
just test-all -p "$TEST_PYTHON" --group dj52   # SQLite (no DB client group)
```

The `[tool.uv] conflicts` table in `pyproject.toml` declares which groups are mutually exclusive so `uv` can validate them.

## Expected LSP Noise

`just-lsp`, Pylance, and cSpell report false positives on template files because they parse Jinja2 syntax as real source code. This is harmless.
