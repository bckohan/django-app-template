from django.apps import AppConfig


class {{cookiecutter.project_slug.replace('-', '').replace('_', '').title()}}Config(AppConfig):
    name = "{{cookiecutter.package_name}}"
    verbose_name = "{{cookiecutter.project_slug.replace('-', ' ').replace('_', ' ').title()}}"
