import click
from notebook.auth import passwd

def pwline():
    if click.confirm('Do you want to use password?'):
        pw = passwd()
        return r"c.NotebookApp.password = '{}'".format(pw)
    else:
        return ''

from os import path, mkdir
JUPYTERBASE = '/root/.jupyter'
CONFIGFILE = 'jupyter_notebook_config.py'

if not path.exists(JUPYTERBASE): mkdir(JUPYTERBASE)
with open(path.join(JUPYTERBASE, CONFIGFILE), 'w') as f:
    f.write('\n'.join([
        r"c.NotebookApp.ip = '*'",
        r"c.NotebookApp.open_browser = False",
        pwline()
    ]))