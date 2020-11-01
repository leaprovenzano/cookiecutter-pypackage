# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

----
{% if cookiecutter.pypi == 'y' -%}
[![pypi version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{% endif -%}
{% if cookiecutter.travis == 'y' -%}
[![travis build](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})
{% endif -%}
{% if cookiecutter.rtd == 'y' -%}
[![documentation status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest)
{% endif -%}
{% if cookiecutter.codecov == 'y' -%}
[![coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/{{ cookiecutter.main_branch }}/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/{{ cookiecutter.main_branch }}/graph/badge.svg)
{% endif -%}

------------------------------------------------------------------------

-   *Free software*: MIT license
-   *Documentation*: [docs](https://{{ cookiecutter.project_slug }}.readthedocs.io)
-   *Supported Python Versions*: >=3.7

------------------------------------------------------------------------

{% if cookiecutter.pypi == 'y' -%}
## Getting Started:


Install the latest stable version with pip:

    $ pip install {{ cookiecutter.project_slug }}

---
{% endif -%}

{% if cookiecutter.rtd == 'y' -%}
## Checkout the docs:

It's best to checkout the [docs](https://{{ cookiecutter.project_slug }}.readthedocs.io). There you'll find detailed
documentation of {{ cookiecutter.project_slug }}'s features and lots of examples of how to
use them.
{% endif -%}
