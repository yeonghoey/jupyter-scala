# Jupyter Notebook with jupyter-scala
# https://github.com/alexarchambault/jupyter-scala
#
# Based on python3, java8
# Supporting kernel: python3, scala211, scala210

FROM java:8

MAINTAINER Yeongho Kim <yeonghoey@gmail.com>

RUN apt-get update \
 && apt-get install -y \
    curl \
    python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install jupyter

# https://github.com/alexarchambault/jupyter-scala/tree/topic/update-readme
# jupyter-scala
RUN curl -L -o jupyter-scala https://git.io/vzhRi \
 && chmod +x jupyter-scala \
 && ./jupyter-scala \
 && rm -f jupyter-scala

# jupyter-scala 2.10
RUN curl -L -o jupyter-scala-2.10 https://git.io/vzhR7 \
 && chmod +x jupyter-scala-2.10 \
 && ./jupyter-scala-2.10 \
 && rm -f jupyter-scala-2.10

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
