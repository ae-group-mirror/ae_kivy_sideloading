# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.59
""" setup of ae namespace package portion kivy_sideloading: kivy mixin and widgets to integrate a sideloading server in your app. """
# noinspection PyUnresolvedReferences
import sys
print(f"SetUp {__name__=} {sys.executable=} {sys.argv=} {sys.path=}")

# noinspection PyUnresolvedReferences
import setuptools

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [       'Development Status :: 3 - Alpha', 'Natural Language :: English', 'Operating System :: OS Independent',
        'Programming Language :: Python', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9', 'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed'],
    'description': 'ae namespace package portion kivy_sideloading: kivy mixin and widgets to integrate a sideloading server in your app',
    'extras_require': {       'dev': [       'aedev_project_tpls', 'ae_ae', 'anybadge', 'coverage-badge', 'aedev_project_manager', 'flake8',
                       'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools'],
        'docs': [],
        'tests': [       'anybadge', 'coverage-badge', 'aedev_project_manager', 'flake8', 'mypy', 'pylint', 'pytest',
                         'pytest-cov', 'pytest-django', 'typing', 'types-setuptools']},
    'install_requires': [       'kivy', 'ae_files', 'ae_i18n', 'ae_sideloading_server', 'ae_gui', 'ae_kivy', 'ae_kivy_file_chooser',
        'ae_kivy_iterable_displayer', 'ae_kivy_qr_displayer'],
    'keywords': ['configuration', 'development', 'environment', 'productivity'],
    'license': 'GPL-3.0-or-later',
    'long_description': ('<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project ae.ae v0.3.101 -->\n'
 '<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.namespace_root_tpls v0.3.22 -->\n'
 '# kivy_sideloading 0.3.28\n'
 '\n'
 '[![GitLab develop](https://img.shields.io/gitlab/pipeline/ae-group/ae_kivy_sideloading/develop?logo=python)](\n'
 '    https://gitlab.com/ae-group/ae_kivy_sideloading)\n'
 '[![LatestPyPIrelease](\n'
 '    https://img.shields.io/gitlab/pipeline/ae-group/ae_kivy_sideloading/release0.3.28?logo=python)](\n'
 '    https://gitlab.com/ae-group/ae_kivy_sideloading/-/tree/release0.3.28)\n'
 '[![PyPIVersions](https://img.shields.io/pypi/v/ae_kivy_sideloading)](\n'
 '    https://pypi.org/project/ae-kivy-sideloading/#history)\n'
 '\n'
 '>ae namespace package portion kivy_sideloading: kivy mixin and widgets to integrate a sideloading server in your '
 'app.\n'
 '\n'
 '[![Coverage](https://ae-group.gitlab.io/ae_kivy_sideloading/coverage.svg)](\n'
 '    https://ae-group.gitlab.io/ae_kivy_sideloading/coverage/index.html)\n'
 '[![MyPyPrecision](https://ae-group.gitlab.io/ae_kivy_sideloading/mypy.svg)](\n'
 '    https://ae-group.gitlab.io/ae_kivy_sideloading/lineprecision.txt)\n'
 '[![PyLintScore](https://ae-group.gitlab.io/ae_kivy_sideloading/pylint.svg)](\n'
 '    https://ae-group.gitlab.io/ae_kivy_sideloading/pylint.log)\n'
 '\n'
 '[![PyPIImplementation](https://img.shields.io/pypi/implementation/ae_kivy_sideloading)](\n'
 '    https://gitlab.com/ae-group/ae_kivy_sideloading/)\n'
 '[![PyPIPyVersions](https://img.shields.io/pypi/pyversions/ae_kivy_sideloading)](\n'
 '    https://gitlab.com/ae-group/ae_kivy_sideloading/)\n'
 '[![PyPIWheel](https://img.shields.io/pypi/wheel/ae_kivy_sideloading)](\n'
 '    https://gitlab.com/ae-group/ae_kivy_sideloading/)\n'
 '[![PyPIFormat](https://img.shields.io/pypi/format/ae_kivy_sideloading)](\n'
 '    https://pypi.org/project/ae-kivy-sideloading/)\n'
 '[![PyPILicense](https://img.shields.io/pypi/l/ae_kivy_sideloading)](\n'
 '    https://gitlab.com/ae-group/ae_kivy_sideloading/-/blob/develop/LICENSE.md)\n'
 '[![PyPIStatus](https://img.shields.io/pypi/status/ae_kivy_sideloading)](\n'
 '    https://libraries.io/pypi/ae-kivy-sideloading)\n'
 '[![PyPIDownloads](https://img.shields.io/pypi/dm/ae_kivy_sideloading)](\n'
 '    https://pypi.org/project/ae-kivy-sideloading/#files)\n'
 '\n'
 '\n'
 '## installation\n'
 '\n'
 '\n'
 'execute the following command to install the\n'
 'ae.kivy_sideloading package\n'
 'in the currently active virtual environment:\n'
 ' \n'
 '```shell script\n'
 'pip install ae-kivy-sideloading\n'
 '```\n'
 '\n'
 'if you want to contribute to this portion then first fork\n'
 '[the ae_kivy_sideloading repository at GitLab](\n'
 'https://gitlab.com/ae-group/ae_kivy_sideloading "ae.kivy_sideloading code repository").\n'
 'after that pull it to your machine and finally execute the\n'
 'following command in the root folder of this repository\n'
 '(ae_kivy_sideloading):\n'
 '\n'
 '```shell script\n'
 'pip install -e .[dev]\n'
 '```\n'
 '\n'
 'the last command will install this package portion, along with the tools you need\n'
 'to develop and run tests or to extend the portion documentation. to contribute only to the unit tests or to the\n'
 'documentation of this portion, replace the setup extras key `dev` in the above command with `tests` or `docs`\n'
 'respectively.\n'
 '\n'
 'more detailed explanations on how to contribute to this project\n'
 '[are available here](\n'
 'https://gitlab.com/ae-group/ae_kivy_sideloading/-/blob/develop/CONTRIBUTING.rst)\n'
 '\n'
 '\n'
 '## namespace portion documentation\n'
 '\n'
 'information on the features and usage of this portion are available at\n'
 '[ReadTheDocs](\n'
 'https://ae.readthedocs.io/en/latest/_autosummary/ae.kivy_sideloading.html\n'
 '"ae_kivy_sideloading documentation").\n'),
    'long_description_content_type': 'text/markdown',
    'name': 'ae_kivy_sideloading',
    'package_data': {       '': [       'widgets.kv', 'img/sideloading_activate.png', 'img/light_1/sideloading_activate.png',
                    'loc/es/Msg.txt', 'loc/de/Msg.txt', 'loc/en/Msg.txt']},
    'packages': [       'ae.kivy_sideloading', 'ae.kivy_sideloading.loc', 'ae.kivy_sideloading.img', 'ae.kivy_sideloading.loc.es',
        'ae.kivy_sideloading.loc.de', 'ae.kivy_sideloading.loc.en', 'ae.kivy_sideloading.img.light_1'],
    'project_urls': {       'Bug Tracker': 'https://gitlab.com/ae-group/ae_kivy_sideloading/-/issues',
        'Documentation': 'https://ae.readthedocs.io/en/latest/_autosummary/ae.kivy_sideloading.html',
        'Repository': 'https://gitlab.com/ae-group/ae_kivy_sideloading',
        'Source': 'https://ae.readthedocs.io/en/latest/_modules/ae/kivy_sideloading.html'},
    'python_requires': '>=3.9',
    'url': 'https://gitlab.com/ae-group/ae_kivy_sideloading',
    'version': '0.3.28',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
