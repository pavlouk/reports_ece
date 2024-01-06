import sqlite3
from datetime import datetime
from bus_app.dataclasses import Todo

connection = sqlite3.connect("./todos.db")
cursor = connection.cursor()


def create_table():
    cursor.execute(
        (
            "CREATE TABLE IF NOT EXISTS todos ("
            "task text,"
            "category text,"
            "date_added text,"
            "date_completed text,"
            "status integer,"
            "position integer )"
        )
    )


def insert_todo(todo: Todo):
    cursor.execute("SELECT COUNT(*) FROM todos")
    count = cursor.fetchone()[0]
    
    with connection:
        cursor.execute(
            (
                "INSERT INTO todos "
                "VALUES (:task, :category, :date_added, :date_completed, :status, :position)"
            ),
            {
                "task": todo.task,
                "category": todo.category,
                "date_added": todo.date_added,
                "date_completed": todo.date_completed,
                "status": todo.status,
                "position": count if count else 0,
            },
        )


def get_all_todos() -> list[Todo]:
    cursor.execute("SELECT * FROM todos")

    todos = []
    for result in cursor.fetchall():
        todos.append(Todo(*result))

    return todos


def delete_todo(position: int):
    cursor.execute("SELECT COUNT(*) FROM todos")
    count = cursor.fetchone()[0]

    with connection:
        cursor.execute(
            ("DELETE FROM todos WHERE position = :position"), {"position": position}
        )
        for pos in range(position + 1, count):
            cursor.execute(
                (
                    "UPDATE todos "
                    "SET position = :position_new "
                    "WHERE position = :position_old"
                ),
                {"position_old": pos, "position_new": pos - 1},
            )


def update_todo(position: int, task: str, category: str):
    if task and category:
        with connection:
            cursor.execute(
                (
                    "UPDATE todos "
                    "SET task = :task, category = :category "
                    "WHERE position = :position"
                ),
                {"position": position, "task": task, "category": category},
            )
        return

    if task:
        with connection:
            cursor.execute(
                ("UPDATE todos SET task = :task WHERE position = :position"),
                {"position": position, "task": task},
            )
        return

    if category:
        with connection:
            cursor.execute(
                (
                    "UPDATE todos "
                    "SET category = :category "
                    "WHERE position = :position"
                ),
                {"position": position, "category": category},
            )
        return
    return

def complete_todo(position: int):
    with connection:
        cursor.execute(
            (
                "UPDATE todos "
                "SET status = 2, date_completed = :date_completed "
                "WHERE position = :position"
            ),
            {
                "date_completed": datetime.now().isoformat(),
                "position": position,
            },
        )
