# Architecture

```
src/xray_lab/
  filters.py   image filters (contrast, edges)
  detect.py    bright-region detection + drawing boxes
  utils.py     load/save helpers
  cli.py       command line interface
```
Data flow: load image -> filter or detect -> save result.
