import re
import sys
import os
from venv import EnvBuilder

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def build_env(path, **kwargs):
    print(f'building new virtualenv in at : {path} ...')
    builder = EnvBuilder(**kwargs)
    builder.create(path)


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)


if {{ cookiecutter.make_virtualenv }}:
    envdir = os.path.join(PROJECT_DIRECTORY, 'env')
    if not os.path.exists(envdir):
        try:
            build_env(envdir, with_pip=True)
        except Exception as err:

            print('{OH NO! error occured during creation of virtualenv:', err, 'exiting...', sep='\n')
            sys.exit(1)
