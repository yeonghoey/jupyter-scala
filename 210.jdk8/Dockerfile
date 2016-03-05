# Jupyter Notebook with jupyter-scala
# https://github.com/alexarchambault/jupyter-scala

FROM java:8

MAINTAINER Yeongho Kim <yeonghoey@gmail.com>

RUN apt-get update \
 && apt-get install -y \
    curl \
    python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install jupyter click

RUN curl -L -o jupyter-scala-2.10 https://git.io/vzhR7 \
 && chmod +x jupyter-scala-2.10 \
 && ./jupyter-scala-2.10 \
 && rm -f jupyter-scala-2.10

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