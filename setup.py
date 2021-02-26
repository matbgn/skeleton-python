try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'projectname',
    'description': 'My Project',
    'author': 'My Name',
    'author_email': 'My Email',
    'url': 'URL to get it at',
    'version': '0.1',
    'install_requires': ['pytest', 'pytest-cov', 'mock'],
    'packages': ['ch.matbgn.iit.NAME'],
    'scripts': []
}

setup(**config)
