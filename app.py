from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        done BOOLEAN DEFAULT 0
    )''')
    conn.commit()
    conn.close()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify([
        {'id': row[0], 'title': row[1], 'description': row[2], 'done': bool(row[3])}
        for row in tasks
    ])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description, done) VALUES (?, ?, ?)', 
                   (data['title'], data.get('description', ''), int(data.get('done', False))))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return jsonify({'message': 'Task created', 'id': task_id}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''UPDATE tasks SET title = ?, description = ?, done = ? WHERE id = ?''',
                   (data['title'], data.get('description', ''), int(data.get('done', False)), task_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
