# Versioning rules for this project

- Format: `MAJOR.MINOR.PATCH` (Semantic Versioning)
  - PATCH: bug fix, nothing else changes (1.0.0 -> 1.0.1)
  - MINOR: new feature, nothing breaks (1.0.1 -> 1.1.0)
  - MAJOR: breaking change (1.1.0 -> 2.0.0)
- Version number lives in `src/xray_lab/__init__.py`.
- Every release gets: a CHANGELOG entry, a git tag `vX.Y.Z`, and a GitHub Release.
- `main` branch is always working. Changes arrive via short branches (`fix/...`, `feat/...`) and Pull Requests.
- Built files (.exe, installers) are NOT committed; attach them to the GitHub Release.
