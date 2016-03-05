from os import path, mkdir, environ
from notebook.auth import passwd

def pwline():
    pwstr = environ.get('JUPYTER_PASSWORD')
    if pwstr: return r"c.NotebookApp.password = '{}'".format(passwd(pwstr))
    else: return ''

BASEDIR = '/root/.jupyter'
CONFIGFILE = 'jupyter_notebook_config.py'

if not path.exists(BASEDIR): mkdir(BASEDIR)
with open(path.join(BASEDIR, CONFIGFILE), 'w') as f:
    f.write('\n'.join([
        r"c.NotebookApp.ip = '*'",
        r"c.NotebookApp.open_browser = False",
        pwline()
    ]))