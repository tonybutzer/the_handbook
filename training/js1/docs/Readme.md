# Notes

This documantation tree was created by sphinx-quickstart with the following characteristics:
- mostly default values
- adding .md files via conf.py


# Modify conf.py

```
source_suffix = ['.rst', '.md']


import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
```


# Makefile 

webServer:
    (cd ./build/html; python -m SimpleHTTPServer)

local:
    make clean; make html

publish:
    make clean; make html
(cd ../../; make)
