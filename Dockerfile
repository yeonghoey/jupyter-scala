# Jupyter Notebook with jupyter-scala
# https://github.com/alexarchambault/jupyter-scala
#
# Based on python3, java8, scala 2.11.7

FROM java:8

MAINTAINER Yeongho Kim <yeonghoey@gmail.com>

RUN apt-get update \
 && apt-get install -y \
    curl \
    python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install jupyter

# jupyter-scala
# https://github.com/alexarchambault/jupyter-scala/tree/topic/update-readme
RUN curl -L -o jupyter-scala https://git.io/vzhRi \
 && chmod +x jupyter-scala \
 && ./jupyter-scala \
 && rm -f jupyter-scala


# Running jupyter notebook in docker has an issue.
# https://github.com/ipython/ipython/issues/7062

# According to the discussion above,
# it only works correctly when it starts with a parameterized innter script.

RUN { echo '#!/bin/bash'; \
      echo 'jupyter notebook --ip=* --no-browser'; \
    } > /start-jupyter-notebook.sh \
 && chmod +x /start-jupyter-notebook.sh


VOLUME /notebooks
WORKDIR /notebooks
EXPOSE 8888

CMD ["/start-jupyter-notebook.sh"]
