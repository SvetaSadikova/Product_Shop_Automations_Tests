# Product Shop Automations Tests
Test application
---
https://berpress.github.io/online-grocery-store/ 

Create and activate virtual environment
---
python -m venv env
---

Run in terminal
---
pip install -r requirements.txt

Install pre-commit https://pre-commit.com/
---
pip install pre-commit
pre-commit run --all-files

Configure yaml file
---
pre-commit sample-config > .pre-commit-config.yaml
