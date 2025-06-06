# 📝 Task Management REST API

A simple Flask REST API to manage tasks. Data is stored in a SQLite database.

## 📦 Requirements
- Python 3
- Flask

Install dependencies:
```
pip install -r requirements.txt
```

## 🚀 Run the API
```
python app.py
```

## 🔁 API Endpoints

- `GET /tasks` – Get all tasks
- `POST /tasks` – Create a task (JSON: `{title, description, done}`)
- `PUT /tasks/<id>` – Update a task
- `DELETE /tasks/<id>` – Delete a task
