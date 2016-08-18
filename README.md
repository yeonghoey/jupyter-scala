# Jupyter Notebook with jupyter-scala

[![](https://images.microbadger.com/badges/image/dockoey/jupyter-scala.svg)](https://microbadger.com/images/dockoey/jupyter-scala "Get your own image badge on microbadger.com")

### Supported Tags
* `210.jdk7`
* `210.jdk8` 
* `211.jdk7`, `latest`
* `211.jdk8`

### Usage
##### Qucik start
```shell
docker run --rm -it -p 8888:8888 dockoey/jupyter-scala
```

##### Other options
```shell
docker run --rm -it -p 8888:8888 \
  -v "$(pwd):/notebooks" \
  -e JUPYTER_PASSWORD=abcd1234 \
  dockoey/jupyter-scala
```

### Note
* Special commands / API for [jupyter-scala](https://github.com/alexarchambault/jupyter-scala#special-commands--api)
* For editing scala code conveniently, I tinkered default [notebook frontend configuration](http://jupyter-notebook.readthedocs.org/en/latest/frontend_config.html).  
  `indentUnit:2`, `smartIndent:false`
