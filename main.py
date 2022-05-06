from user import User
from database import DataBase
import window

user_1 = User(1, "Default", "1234")

user_1.get_container().create_task("Terminar proyecto POO", 
                                "Implementar la parte gráfica y base de datos", 
                                3,
                                "10-05-2022", 
                                False
                            )

db = DataBase()
db.create_users_database()
db.create_users_table()
db.insert_user(user_1.user_id, user_1.get_username(), user_1.get_password(), user_1.get_points())
db.create_tasks_database()
db.create_tasks_table()

db.insert_task(user_1.user_id, user_1.get_container().get_tasks()[0])

print(db.read_rows("tareas"))


#w = window.LogginWindow()
#w.add_user(user_1)
#w.start_window()

