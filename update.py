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
    'scala210': {
        'from'                  : 'java:7',
        'jupyter_scala_install' : jupyterscala210_install },
    'scala211': {
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

RUN pip3 install jupyter

$jupyter_scala_install

# Running Jupyter Notebook in docker has an issue.
# https://github.com/ipython/ipython/issues/7062

# According to the discussion above,
# it only works correctly when it starts with a parameterized innter script.
RUN { echo '#!/bin/bash'; \
      echo 'jupyter notebook --ip=* --no-browser'; \
    } > /entrypoint.sh \
 && chmod +x /entrypoint.sh


VOLUME /notebooks
WORKDIR /notebooks
EXPOSE 8888

CMD ["/entrypoint.sh"]
'''.strip())


from os import path, mkdir
for k, v in params.iteritems():
    if not path.exists(k): mkdir(k)
    with open(path.join(k, 'Dockerfile'), 'w') as f:
        f.write(template.safe_substitute(v))
