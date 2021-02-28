from setuptools import setup

setup(
   name='wsgi_framework',
   version='1.5',
   description='Is a pretty simple wsgi framework',
   author='Yerzhan Aitzhanov',
   author_email='yerzhan.aitzhanov@gmail.com',
   packages=['wsgi_framework'],
   install_requires=['jinja2', 'gunicorn']
)
