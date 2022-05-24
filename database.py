import sqlite3 as sql
from typing import Any
from task import Task
from meeting import Meeting
from note import Note
from user import User

USERS = "usuarios.db"
TASKS = "tareas.db"
NOTES = "notas.db"
MEETINGS = "reuniones.db"

class DataBase:
    
    def create_users_database(self) -> None:
        self.conn = sql.connect(USERS)
        self.conn.commit()
        self.conn.close()
    
    def create_users_table(self) -> None:
        self.conn = sql.connect(USERS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS usuarios(
                usuario_id INTEGER PRIMARY KEY,
                usuario text,
                contraseña text,
                puntaje integer
            )"""
        )
        self.conn.commit()
        self.conn.close()
    
    def create_tasks_database(self) -> None:
        self.conn = sql.connect(TASKS)
        self.conn.commit()
        self.conn.close()

    def create_tasks_table(self) -> None:
        self.conn = sql.connect(TASKS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS tareas(
                usuario_id integer,
                nombre text,
                descripción text,
                nivel_de_relevancia integer,
                fecha_de_creación date,
                fecha_límite date,
                hecha text
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def create_notes_database(self) -> None:
        self.conn = sql.connect(NOTES)
        self.conn.commit()
        self.conn.close()

    def create_notes_table(self) -> None:
        self.conn = sql.connect(NOTES)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS notas(
                usuario_id integer,
                nombre text,
                descripción text,
                nivel_de_relevancia integer,
                fecha_de_creación date,
                fuente text,
                tamaño_fuente float
            )"""
        )
        self.conn.commit()
        self.conn.close()
    
    def create_meetings_database(self) -> None:
        self.conn = sql.connect(MEETINGS)
        self.conn.commit()
        self.conn.close()

    def create_meetings_table(self) -> None:
        self.conn = sql.connect(MEETINGS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS reuniones(
                usuario_id integer,
                nombre text,
                descripción text,
                nivel_de_relevancia integer,
                fecha_de_creación date,
                link text,
                fecha_reunión date
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def insert_user(self, user: User) -> None:
        self.conn = sql.connect(USERS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"INSERT INTO usuarios VALUES({user.user_id}, '{user.username}', '{user.password}', {user.points})"
        )
        self.conn.commit()
        self.conn.close()

    def insert_task(self, user_id: int, task: Task) -> None:
        self.conn = sql.connect(TASKS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"INSERT INTO tareas VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (user_id, 
            task.name, task.description,
            task.relevance_level, task.creation_date,
            task.due_date, task.state
            )
        )
        self.conn.commit()
        self.conn.close()
    
    def insert_meeting(self, user_id: int, meeting: Meeting) -> None:
        self.conn = sql.connect(MEETINGS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"INSERT INTO reuniones VALUES(?, ?, ?, ?, ?, ?, ?)",
            (user_id,
            meeting.name, meeting.description,
            meeting.relevance_level, meeting.creation_date,
            meeting.link, meeting.meeting_date
            )
        )
        self.conn.commit()
        self.conn.close()
    
    def insert_note(self, user_id: int, note: Note) -> None:
        self.conn = sql.connect(NOTES)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"INSERT INTO notas VALUES(?, ?, ?, ?, ?, ?, ?)",
            (user_id,
            note.name, note.description,
            note.relevance_level, note.creation_date,
            note.font, note.font_size
            )
        )
        self.conn.commit()
        self.conn.close()

    def read_rows(self, database_name: str) -> list:
        self.conn = sql.connect(f"{database_name}.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM '{database_name}'")
        data = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return data
    
    def search(self, database_name: str, field: Any) -> list:
        self.conn = sql.connect(f"{database_name}.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM '{database_name}' WHERE usuario_id='{field}'")
        data = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return data
    
    def update(self, user_id: int, field: Any, updated_field: Any) -> None:
        self.conn = sql.connect("usuarios.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"UPDATE usuarios set '{field}' = '{updated_field}' WHERE usuario_id={user_id}")
        self.conn.commit()
        self.conn.close()

    def delete_user(self, field: Any) -> None:
        self.conn = sql.connect(f"{USERS}")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM usuarios WHERE usuario_id='{field}'")
        self.conn.commit()
        self.conn.close()
    
    def delete_item(self, database_name: str, user_id: int, name: str) -> None:
        self.conn = sql.connect(f"{database_name}.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM '{database_name}' WHERE usuario_id=? and nombre=?", (user_id, name))
        self.conn.commit()
        self.conn.close()
