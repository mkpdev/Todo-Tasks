# Todo-Task-Nested

Design an API change to make it possible to create a nested list of subtasks for every task (even for subtasks)

## About

The backend is written in Django, django-restframework, which consists of an API which can retrive, create, update or delete contents.

## Setup

Clone this repo and cd:

```
git clone https://github.com/mkpdev/Todo-Tasks.git
cd Todo-Tasks
```

Create environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Migrations

```

python3 manage.py migrate

```

## Run

```

python3 manage.py runserver

```

## API Docs

refer [api-docs.md](api-doc.md)
