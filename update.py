jupyterscala210_install = r'''
RUN curl -L -o jupyter-scala-2.10 https://git.io/vzhR7 \
 && chmod +x jupyter-scala-2.10 \
 && ./jupyter-scala-2.10 \
 && rm -f jupyter-scala-2.10
'''.strip()

jupyterscala211_install = r'''
RUN curl -L -o jupyter-scala https://git.io/vzhRi \
 && chmod +x jupyter-scala \
 && ./jupyter-scala \
 && rm -f jupyter-scala
'''.strip()

params = {
    'jdk7-scala210': {
        'from'                  : 'java:7',
        'jupyter_scala_install' : jupyterscala210_install },
    'jdk8-scala210': {
        'from'                  : 'java:8',
        'jupyter_scala_install' : jupyterscala210_install },

    'jdk7-scala211': {
        'from'                  : 'java:7',
        'jupyter_scala_install' : jupyterscala211_install },
    'jdk8-scala211': {
        'from'                  : 'java:8',
        'jupyter_scala_install' : jupyterscala211_install }
}


from string import Template
template = Template(r'''
# Jupyter Notebook with jupyter-scala
# https://github.com/alexarchambault/jupyter-scala

FROM $from

MAINTAINER Yeongho Kim <yeonghoey@gmail.com>

RUN apt-get update \
 && apt-get install -y \
    curl \
    python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install jupyter click

$jupyter_scala_install

# Set indentUnit 2 as scala standard.
# Off smartIndent because it works weird for scala.
ENV NBCONFIG /root/.jupyter/nbconfig
RUN mkdir -p $NBCONFIG \
 && { echo '{"CodeCell":{"cm_config":'; \
      echo '{"indentUnit":2,"smartIndent":false}'; \
      echo '}}'; \
    } > /$NBCONFIG/notebook.json

# Add entry point which runs `bootstrap.py` before launch jupyter notebook.
# It provides convenient settings for ip and password at runtime.
COPY bootstrap.py /bootstrap.py

RUN { echo '#!/bin/bash'; \
      echo 'set -e'; \
      echo 'python3 /bootstrap.py'; \
      echo 'jupyter notebook'; \
    } > /entrypoint.sh \
 && chmod +x /entrypoint.sh


VOLUME /notebooks
WORKDIR /notebooks
EXPOSE 8888

CMD ["/entrypoint.sh"]
'''.strip())


bootstrap = r'''
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
'''.strip()

from os import path, mkdir
for k, v in params.iteritems():
    if not path.exists(k): mkdir(k)
    with open(path.join(k, 'Dockerfile'), 'w') as f:
        f.write(template.safe_substitute(v))
    with open(path.join(k, 'bootstrap.py'), 'w') as f:
        f.write(bootstrap)
