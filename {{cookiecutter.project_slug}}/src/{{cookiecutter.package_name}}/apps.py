from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "{{cookiecutter.package_name}}"
    verbose_name = "{{cookiecutter.project_slug.replace('-', ' ').replace('_', ' ').title()}}"
