# Task Manager

A small full-stack task manager built with Flask, SQLite and vanilla JavaScript.
I built this to understand how a web request travels from the browser to a
server and a database, and back again.

## Features

- View, add and delete tasks
- REST API backend returning JSON
- Tasks stored in SQLite, so they survive a server restart

## Tech stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML and vanilla JavaScript (`fetch`)

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a task |
| DELETE | `/tasks/<id>` | Delete a task |

## Running it locally

```
pip install flask
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## What I learned

- Designing a small REST API and returning JSON from Flask
- Connecting a front end to a backend with `fetch`
- Using parameterised SQL queries to guard against SQL injection
- Reading error messages properly, and changing one thing at a time when debugging
