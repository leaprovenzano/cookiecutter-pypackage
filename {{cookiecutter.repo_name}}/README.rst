{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/
     :alt: Updates
{% endif %}


.. image:: https://img.shields.io/badge/hypothesis-tested-brightgreen.svg
   :alt: Tested with Hypothesis
   :target: https://hypothesis.readthedocs.io

----

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}
* Documentation: `docs`_
* Supported Python Versions: >=3.6

----


{{ cookiecutter.project_short_description }}



Getting Started:
~~~~~~~~~~~~~~~~

Install the latest stable version with pip::

   $ pip install {{ cookiecutter.project_slug }}


**Checkout the docs**:

It's best to checkout the `docs`_. There you'll find detailed
documentation of {{ cookiecutter.project_name }}}'s features and lots of examples of
how to use them.

What's is it?
~~~~~~~~~~~~~

* TODO

Principles:
~~~~~~~~~~~

* TODO

.. _docs: https://{{ cookiecutter.repo_name | replace("_", "-") }}.readthedocs.io
