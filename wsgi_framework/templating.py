import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)


def render(template_path: str, **kwargs):
    template = env.get_template(template_path)
    return [template.render(**kwargs).encode('utf-8')]
