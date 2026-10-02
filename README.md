# X-Ray Lab 

A small OpenCV project made for practising Git versioning: commits, branches, tags and GitHub Releases.

## Setup
```
python -m venv .venv
.venv\Scripts\activate        # Windows  (Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

## Run
Run from the repo root. The code lives in `src/`, so tell Python where to find it:

Windows PowerShell:
```
$env:PYTHONPATH="src"
python -m xray_lab --version
python -m xray_lab --input assets/sample_xray.png --mode contrast
python -m xray_lab --input assets/sample_xray.png --mode edges --output output/edges.png
python -m xray_lab --input assets/sample_xray.png --mode detect --output output/boxes.png
```
Mac/Linux: use `PYTHONPATH=src python -m xray_lab ...`

## Test
```
pytest
```

## Structure
| Folder | Purpose |
|---|---|
| `src/xray_lab/` | application code |
| `tests/` | automated tests |
| `docs/` | documentation, versioning rules |
| `assets/` | sample images |
| `scripts/` | helper scripts |

See `PRACTICE_GUIDE.md` for the tagging and release exercises.
