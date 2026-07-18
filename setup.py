# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.82
""" setup of ae namespace package portion kivy_sideloading: kivy mixin and widgets to integrate a sideloading server in your app. """
import pathlib
import sys
from typing import Any
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs: dict[str, Any] = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    'description': 'ae namespace package portion kivy_sideloading: kivy mixin and widgets to integrate a sideloading server in your app',
    'extras_require': {
        'dev': [
            'aedev_project_tpls',
            'ae_ae',
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
        'docs': [],
        'tests': [
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
    },
    'install_requires': [
        'kivy',
        'ae_files',
        'ae_i18n',
        'ae_sideloading_server',
        'ae_gui',
        'ae_kivy',
        'ae_kivy_file_chooser',
        'ae_kivy_iterable_displayer',
        'ae_kivy_qr_displayer',
    ],
    'keywords': [
        'configuration',
        'development',
        'environment',
        'productivity',
    ],
    'license': 'GPL-3.0-or-later',
    'long_description': (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    'long_description_content_type': 'text/markdown',
    'name': 'ae_kivy_sideloading',
    'package_data': {
        '': [
            'widgets.kv',
            'img/sideloading_activate.png',
            'img/light_1/sideloading_activate.png',
            'loc/de/Msg.txt',
            'loc/en/Msg.txt',
            'loc/es/Msg.txt',
        ],
    },
    'packages': [
        'ae.kivy_sideloading',
        'ae.kivy_sideloading.img',
        'ae.kivy_sideloading.loc',
        'ae.kivy_sideloading.img.light_1',
        'ae.kivy_sideloading.loc.de',
        'ae.kivy_sideloading.loc.en',
        'ae.kivy_sideloading.loc.es',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/ae-group/ae_kivy_sideloading/-/issues',
        'Documentation': 'https://ae.readthedocs.io/en/latest/_autosummary/ae.kivy_sideloading.html',
        'Repository': 'https://gitlab.com/ae-group/ae_kivy_sideloading',
        'Source': 'https://ae.readthedocs.io/en/latest/_modules/ae/kivy_sideloading.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/ae-group/ae_kivy_sideloading',
    'version': '0.3.29',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    ...
