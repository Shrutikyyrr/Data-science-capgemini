# Section 9 – CI/CD + GitHub Actions

## What this does
Every time you `git push` to any branch, GitHub Actions automatically:
1. Checks out the code
2. Sets up Python 3.11
3. Installs dependencies
4. Runs all pytest tests
5. Reports pass/fail in the GitHub Actions tab

## Setup
1. Push this folder to your GitHub repo
2. Go to repo → Actions tab → you'll see the workflow running

## Workflow file location
`.github/workflows/ci.yml`

## Run tests locally (same as CI)
```bash
pip install -r requirements.txt
pytest test_app.py -v
```

## CI/CD Explained
- CI (Continuous Integration): Auto-run tests on every push — catch bugs early
- CD (Continuous Deployment): Auto-deploy to server after tests pass (not in scope here)
- GitHub Actions: Free CI/CD platform built into GitHub, configured via YAML files
