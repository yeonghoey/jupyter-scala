# Jupyter Notebook with jupyter-scala

[![](https://badge.imagelayers.io/dockoey/jupyter-scala:latest.svg)](https://imagelayers.io/?images=dockoey/jupyter-scala:latest 'Get your own badge on imagelayers.io')

### Supported Tags
* `jdk7-scala210`
* `jdk8-scala210` 
* `jdk7-scala211`, `latest`
* `jdk8-scala211`

### Usage

```shell
docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" dockoey/jupyter-scala
```

### Note
* [jupyter-scala](https://github.com/alexarchambault/jupyter-scala) is currently being updated. Read guides for a [new version](https://github.com/alexarchambault/jupyter-scala/tree/topic/update-readme).
* For editing scala code conveniently, I tinkered default [notebook frontend configuration](http://jupyter-notebook.readthedocs.org/en/latest/frontend_config.html).  
  `indentUnit:2`, `smartIndent:false`
