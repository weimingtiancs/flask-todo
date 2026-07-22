import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)
app.json.ensure_ascii = False

def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL)")
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tasks")
def get_tasks():
    conn = get_db()
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    conn = get_db()
    cur = conn.execute("INSERT INTO tasks (task) VALUES (?)", (data["task"],))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "task": data["task"]}

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "删除成功"}

if __name__ == "__main__":
    app.run(debug=True)