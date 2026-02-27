# Contributing

Contributions are encouraged! Please use the issue page to submit feature requests or bug reports. Issues with attached PRs will be given priority and have a much higher likelihood of acceptance. Please also open an issue and associate it with any submitted PRs. Before PRs can be merged all added code test coverage must be 100%.

We are actively seeking additional maintainers. If you're interested, please open an issue or [contact me](https://github.com/bckohan).

## Installation

### Install Just

We provide a platform independent justfile with recipes for all the development tasks. You should [install just](https://just.systems/man/en/installation.html) if it is not on your system already.

``{{cookiecutter.project_slug}}`` uses [uv](https://docs.astral.sh/uv) for environment, package, and dependency management. ``just setup`` will install the necessary build tooling if you do not already have it:

```bash
just setup <python version>
```

**This will also install pre-commit** If you wish to submit code that does not pass pre-commit checks you can disable pre-commit by running:

```bash
just run pre-commit uninstall
```

### Install the Dev environment

To install all development dependencies run the ``install`` recipe:

```bash
just install
```

### Windows

There is a symbolic link to the top level examples directory in tests. On Windows to make sure this link is created you need to be in [developer mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) and to configure git to allow symbolic links:

```console
git config --global core.symlinks true
```

## Documentation

`{{cookiecutter.project_slug}}` documentation is generated using [Sphinx](https://www.sphinx-doc.org) with the [furo](https://github.com/pradyunsg/furo) theme. Any new feature PRs must provide updated documentation for the features added. To build the docs run doc8 to check for formatting issues then run Sphinx:

```bash
just docs  # builds docs
just check-docs  # lint the docs
just check-docs-links  # check for broken links in the docs
```

Run the docs with auto rebuild using:

```bash
just docs-live
```

## Static Analysis

`{{cookiecutter.project_slug}}` uses [ruff](https://docs.astral.sh/ruff/) for Python linting, header import standardization and code formatting. [mypy](http://mypy-lang.org/) and [pyright](https://github.com/microsoft/pyright) are used for static type checking. Before any PR is accepted the following must be run, and static analysis tools should not produce any errors or warnings. Disabling certain errors or warnings where justified is acceptable:

To fix formatting and linting problems that are fixable run:

```bash
just fix
```

To run all static analysis without automated fixing you can run:

```bash
just check
```

## Running Tests

`{{cookiecutter.project_slug}}` is set up to use [pytest](https://docs.pytest.org) to run unit tests. All the tests are housed in `tests`. Before a PR is accepted, all tests must be passing and the code coverage must be at 100%. A small number of exempted error handling branches are acceptable.

To run the full suite:

```shell
just test
```

To run a single test, or group of tests in a class:

```shell
just test <path_to_tests_file>::ClassName::FunctionName
```

### Debugging tests

To debug a test use the ``debug-test`` recipe:

```shell
just debug-test <path_to_tests_file>::ClassName::FunctionName
```

This will set a breakpoint at the start of the test.

## Versioning

`{{cookiecutter.project_slug}}` strictly adheres to [semantic versioning](https://semver.org).

## Issuing Releases

The release workflow is triggered by tag creation. You must have [git tag signing enabled](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits). Our justfile has a release shortcut:

```bash
just release x.x.x
```

## Just Recipes

Run just with no recipe to see a list of all available commands:

```bash
just
```
