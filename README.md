# Task Management REST API

This is a simple REST API for managing tasks, built using Python Flask and SQLite.

## Endpoints
- `GET /tasks` – List all tasks.
- `POST /tasks` – Add a new task. JSON body must include `"title"` (string), optional `"completed"` (boolean).
- `PUT /tasks/:id` – Update a task by ID. JSON body can include `"title"` and/or `"completed"`.
- `DELETE /tasks/:id` – Delete a task by ID.

## Setup & Run
1. Ensure you have Python 3 and pip installed.
2. Install Flask: `pip install flask`
3. Run the API server: `python app.py`
4. The API server will start at `http://127.0.0.1:5000`

## Database
Uses SQLite database file `tasks.db` created automatically on first run.

## Notes
- Data is persisted in `tasks.db`.
- Make sure to send JSON body for POST and PUT requests.
