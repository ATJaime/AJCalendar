import sqlite3 as sql
from typing import Any
from task import Task
from meeting import Meeting
from note import Note

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
            """CREATE TABLE usuarios(
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
            """CREATE TABLE tareas(
                usuario_id INTEGER PRIMARY KEY,
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
            """CREATE TABLE notas(
                usuario_id INTEGER PRIMARY KEY,
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
            """CREATE TABLE reuniones(
                usuario_id INTEGER PRIMARY KEY,
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

    def insert_user(self, user_id: int, username: str, password: str, points: int) -> None:
        self.conn = sql.connect(USERS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"INSERT INTO usuarios VALUES({user_id}, '{username}', '{password}', {points})"
        )
        self.conn.commit()
        self.conn.close()

    def insert_task(self, user_id: int, task: Task) -> None:
        self.conn = sql.connect(TASKS)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            f"INSERT INTO tareas VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (user_id, 
            task.get_name(), task.get_description(),
            task.get_relevance_level(), task.get_creation_date(),
            task.get_due_date(), task.get_state()
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
            meeting.get_name(), meeting.get_description(),
            meeting.get_relevance_level(), meeting.get_creation_date(),
            meeting.get_link(), meeting.get_meeting_date()
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
            note.get_name(), note.get_description(),
            note.get_relevance_level(), note.get_creation_date(),
            note.get_font(), note.get_font_size()
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
        self.cursor.execute(f"SELECT * FROM '{database_name}' WHERE username='{field}'")
        data = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return data
