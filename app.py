import sqlite3
from flask import Flask, jsonify, request, g, abort

app = Flask(__name__)
DATABASE = 'tasks.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db:
        db.close()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    cur = db.execute('SELECT * FROM tasks')
    tasks = [dict(row) for row in cur.fetchall()]
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400, description="Task must have a 'title'")
    title = data['title']
    completed = data.get('completed', False)
    db = get_db()
    cur = db.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, completed))
    db.commit()
    task_id = cur.lastrowid
    task = {'id': task_id, 'title': title, 'completed': completed}
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        abort(400, description="Request body must be JSON")
    title = data.get('title')
    completed = data.get('completed')

    db = get_db()
    cur = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cur.fetchone()
    if not task:
        abort(404, description="Task not found")

    new_title = title if title is not None else task['title']
    new_completed = completed if completed is not None else task['completed']
    db.execute('UPDATE tasks SET title = ?, completed = ? WHERE id = ?', (new_title, new_completed, task_id))
    db.commit()

    updated_task = {'id': task_id, 'title': new_title, 'completed': new_completed}
    return jsonify(updated_task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = get_db()
    cur = db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cur.fetchone()
    if not task:
        abort(404, description="Task not found")
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()
    return '', 204

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
