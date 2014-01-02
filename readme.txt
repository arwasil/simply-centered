# Readme

## Setup
```bash
pip install -r requirements.txt
cp settings_local.template settings_local.py
cp pre-commit.template .git/hooks/pre-commit
```

## Working locally
```bash
python manage.py runserver
```

## Deploying
```bash
git add .
git commit -m 'changes!'
git push
```