from ctypes import windll
from datetime import datetime
from tkinter.ttk import Treeview
from tkinter.ttk import Scrollbar
from user import User
from note import Note
from meeting import Meeting
from task import Task
from database import DataBase
from werkzeug.security import check_password_hash
import tkinter
from tkinter import PhotoImage
from tkcalendar import DateEntry

windll.shcore.SetProcessDpiAwareness(1)

class LoginWindow(tkinter.Tk): 
    def __init__(self) -> None:
        super().__init__()

        self.geometry("900x600")
        self.title("AJCalendar")
        self.resizable(False, False)
        self.config(bg="#2E2F33")
        
        for i in range(0, 50):
            tkinter.Grid.rowconfigure(self, i, weight=1)
        
        for i in range(0, 10):
            tkinter.Grid.columnconfigure(self, i, weight=1)
 
        self.user_label = tkinter.Label(self, 
                                        text="Usuario:", 
                                        bg="#2E2F33",
                                        font=("Arial", 14),
                                        foreground="white"
                                    )
        self.pass_label = tkinter.Label(self, 
                                        text="Contraseña:", 
                                        bg="#2E2F33",
                                        font=("Arial", 14),
                                        foreground="white"
                                    )

        self.photo_image = PhotoImage(master=self, file="assets/images/register_button.png")

        self.register_button = tkinter.Button(self,
                                                image=self.photo_image,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=self.register
                                            )
        
        self.photo_image2 = PhotoImage(master=self, file="assets/images/login_button.png")
        self.login_button = tkinter.Button(self,
                                            image=self.photo_image2,
                                            bg="#2E2F33",
                                            activebackground="#2E2F33",
                                            borderwidth=0,
                                            command=self.verify_user_information,
                                        )
        self.user_entry = tkinter.Entry(self, 
                                        bg="white",
                                        font=("Arial", 14),
                                        foreground="black",
                                        insertbackground="black", 
                                        borderwidth=0)
        self.pass_entry = tkinter.Entry(self, 
                                        show="*", 
                                        bg="white",
                                        insertbackground="black",
                                        font=("Arial", 14),
                                        foreground="black", 
                                        borderwidth=0
                                    )

        self.user_label.grid(row=25, column=3, sticky="nsew")
        self.pass_label.grid(row=28, column=3, sticky="nsew")
        self.user_entry.grid(row=25, column=4, sticky="nsew")
        self.pass_entry.grid(row=28, column=4, sticky="nsew")
        self.login_button.grid(row=33, column=4, sticky="nsew")
        self.register_button.grid(row=35, column=4, sticky="nsew")
        
    
    def start_window(self) -> None:
        self.mainloop()
    
    def verify_user_information(self) -> None:
        try:
            users = DataBase().read_rows("usuarios")
            if (self.user_entry.get().strip(' ') == ""
                or self.pass_entry.get().strip(' ') == ""):
                print("Por favor, rellene los campos")
            else:
                for user in users:
                    if (self.user_entry.get() == user[1] and
                        check_password_hash(user[2], self.pass_entry.get())):
                        self.destroy()
                        logged_user = User(user[0], user[1], user[2], user[3])
                        DataBase().create_notes_table
                        DataBase().create_tasks_table
                        DataBase().create_meetings_table
                        try:
                            notes_user = DataBase().search("notas", user[0])
                            for note in notes_user:
                                logged_user.create_note(note[1], note[2], note[3], note[4], note[5])
                        except:
                            pass

                        try:
                            tasks_user = DataBase().search("tareas", user[0])
                            for task in tasks_user:
                                logged_user.create_task(task[1], task[2], task[3], task[4], task[5])
                        except:
                            pass

                        try:
                            meetings_user = DataBase().search("reuniones", user[0])
                            for meeting in meetings_user:
                                logged_user.create_meeting(meeting[1], meeting[2], meeting[3], meeting[4], meeting[5])
                        except:
                            pass
                        ContainerWindow(logged_user)
                        return
                print("Los campos diligenciados no son correctos")
        except:
            print("No hay usuarios registrados")
                
    def register(self) -> None:
        def add_user(id: int) -> None:
            new_user = User(id, 
                            user_register_entry.get(),
                            password_register_entry.get()
                        )
            DataBase().insert_user(new_user)
            register_window.destroy()

        def verify_user() -> None:
            if (password_confirmation_entry.get().strip(' ') == "" 
                or password_register_entry.get().strip(' ') == ""
                or user_register_entry.get().strip(' ') == ""):
                print("Ingrese valores en los campos")

            elif password_confirmation_entry.get() != password_register_entry.get():
                print("Las contraseñas no coinciden")

            else:
                id = 0
                DataBase().create_users_database()
                DataBase().create_users_table()
                users = DataBase().read_rows("usuarios")
                for user in users:
                    if user[1] == user_register_entry.get():
                        print("Este nombre de usuario ya está siendo usado")
                        return
                    id += 1
                add_user(id)

        register_window = tkinter.Toplevel(self)
        register_window.geometry("900x600")
        register_window.title("AJCalendar")
        register_window.resizable(False, False)
        register_window.config(bg="#2E2F33")

        for i in range(0, 50):
            tkinter.Grid.rowconfigure(register_window, i, weight=1)
        
        for i in range(0, 10):
            tkinter.Grid.columnconfigure(register_window, i, weight=1)


        user_register_label = tkinter.Label(register_window, text="Usuario:",bg="#2E2F33",font=("Arial", 14),
                                        foreground="white")
        password_register_label = tkinter.Label(register_window, text="Contraseña:",bg="#2E2F33",font=("Arial", 14),
                                        foreground="white")
        password_confirmation_label = tkinter.Label(register_window, text="Confirmar contraseña:",bg="#2E2F33",font=("Arial", 14),
                                        foreground="white")
        user_register_entry = tkinter.Entry(register_window,bg="white",
                                        font=("Arial", 14),
                                        foreground="black",
                                        insertbackground="black", 
                                        borderwidth=0)
        password_register_entry = tkinter.Entry(register_window, show="*",bg="white",
                                        insertbackground="black",
                                        font=("Arial", 14),
                                        foreground="black", 
                                        borderwidth=0)
        password_confirmation_entry = tkinter.Entry(register_window, show="*",bg="white",
                                        insertbackground="black",
                                        font=("Arial", 14),
                                        foreground="black", 
                                        borderwidth=0)
        
        photo_imageR = PhotoImage(master=register_window, file="assets/images/register1_button.png")
        r_button = tkinter.Button(register_window,
                                image=photo_imageR,
                                bg="#2E2F33",
                                activebackground="#2E2F33",
                                borderwidth=0,
                                command=verify_user
                            )
        user_register_label.grid(row=25, column=3, sticky="nsew")
        user_register_entry.grid(row=25, column=4, sticky="nsew")
        password_register_label.grid(row=28, column=3, sticky="nsew")
        password_register_entry.grid(row=28, column=4, sticky="nsew")
        password_confirmation_label.grid(row=33, column=3, sticky="nsew")
        password_confirmation_entry.grid(row=33, column=4, sticky="nsew")
        r_button.grid(row=38, column=4, sticky ="nsew")

        register_window.mainloop()


class ContainerWindow(tkinter.Tk):
    def __init__(self, user: User) -> None:
        super().__init__()
        self.user = user
        self.geometry("900x600")
        self.title("AJCalendar")
        self.resizable(False, False)
        self.config(bg="#2E2F33")
        
        self.config_grid(self)

        self.photo_image_3 = PhotoImage(file="assets/images/NOTAS.png")
        self.score_label = tkinter.Label(self, 
                                        text= f"Puntos: {self.user.points}", 
                                        fg="white", 
                                        bg="#2E2F33",
                                        font=("Arial", 14))
        self.notas_button = tkinter.Button(self,
                                                image=self.photo_image_3,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0, 
                                                command=self.create_note
                                            )

        
        self.photo_image_5 = PhotoImage(file="assets/images/TAREA.png")

        self.task_button = tkinter.Button(self,
                                                image=self.photo_image_5,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=self.create_task
                                            )
        self.photo_image_6 = PhotoImage(file="assets/images/MEET.png")

        self.meet_button = tkinter.Button(self,
                                                image=self.photo_image_6,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=self.create_meeting,
                                            )

        self.config_button = tkinter.Button(self,
                                            text="O",
                                            command=self.config_window
                                        )

        self.log_out_button = tkinter.Button(self,
                                            text="Salir",
                                            command=self.log_out,
                                        )

        try:                                
            self.last_note = tkinter.Button(self, text=self.user.notes[-1])
        except:
            self.last_note = tkinter.Button(self, text="NO HAY NOTAS")
        try:
            self.last_task = tkinter.Button(self, text=self.user.tasks[-1])
        except:
            self.last_task = tkinter.Button(self, text="NO HAY TAREAS")

        try:
            self.last_meeting = tkinter.Button(self, text=self.user.meetings[-1])
        except:
            self.last_meeting = tkinter.Button(self, text="NO HAY REUNIONES")

        self.last_note.config(font=("Arial", 18), bg="#2E2F33", fg="white", borderwidth=0, command=self.note_window)
        self.last_task.config(font=("Arial", 18), bg="#2E2F33", fg="white", borderwidth=0, command=self.task_window)
        self.last_meeting.config(font=("Arial", 18), bg="#2E2F33", fg="white", borderwidth=0, command=self.meeting_window)

        self.last_note.grid(row=10, column=5, sticky="ew")
        self.last_task.grid(row=13, column=5, sticky="ew")
        self.last_meeting.grid(row=16, column=5, sticky="ew")

        self.log_out_button.grid(row=2, column=0, sticky="nsew")
        self.config_button.grid(row=2, column=9, sticky="nsew")
        self.notas_button.grid(row=10, column=1, sticky="nsew")
        self.task_button.grid(row=13, column=1, sticky="nsew")
        self.meet_button.grid(row=16, column=1, sticky="nsew")
        self.score_label.grid(row=20, column=7, sticky="nsew")
        self.mainloop()
    
    def config_grid(self, root: tkinter.Tk) -> None:
        for i in range(0, 40):
            tkinter.Grid.rowconfigure(root, i, weight=1)
        for i in range(0, 10):
            tkinter.Grid.columnconfigure(root, i, weight=1)

    def log_out(self) -> None:
        self.destroy()
        w = LoginWindow()
        w.start_window()

    def config_window(self) -> None:
        def delete_account():
            for task in self.user.tasks:
                DataBase().delete_item("tareas", self.user.user_id, task.name)
            for note in self.user.notes:
                DataBase().delete_item("notas", self.user.user_id, note.name)
            for meeting in self.user.meetings:
                DataBase().delete_item("reuniones", self.user.user_id, meeting.name)
            DataBase().delete_user(self.user.user_id)
            self.log_out()

        def change_password():
            if password_entry.get().strip(' ') == "":
                print("Ingrese una contraseña")
            elif password_entry.get() != confirm_password_entry.get():
                print("Las contraseñas no coinciden")
            else:
                self.user.password = password_entry.get()
                DataBase().update(self.user.user_id, "contraseña", self.user.password)
            
        def change_name():
            if name_entry.get().strip(' ') == "":
                print("Ingrese un nombre de usuario")
            else:
                data = DataBase().read_rows("usuarios")
                for dat in data:
                    if name_entry.get() in dat:
                        print("Este nombre de usuario ya está siendo usado")
                        return
                self.user.username = name_entry.get()
                DataBase().update(self.user.user_id, "usuario", self.user.username)

        config_window = tkinter.Toplevel(self)
        config_window.geometry("600x700")
        config_window.title("Configuración de la cuenta")
        config_window.resizable(False, False)
        config_window.config(bg="#2E2F33")

        self.config_grid(config_window)

        name_label = tkinter.Label(config_window, text="Nombre de usuario:", bg="#2E2F33", fg="white")
        password_label = tkinter.Label(config_window, text="Contraseña:", bg="#2E2F33", fg="white")
        confirm_password_label = tkinter.Label(config_window, text="Confirmar contraseña:", bg="#2E2F33", fg="white")

        name_entry = tkinter.Entry(config_window, font=("Arial", 12))
        password_entry = tkinter.Entry(config_window, show="*", font=("Arial", 12))
        confirm_password_entry = tkinter.Entry(config_window, show="*", font=("Arial", 12))
        name_entry.insert("end", self.user.username)

        delete_button = tkinter.Button(config_window, text="Eliminar cuenta", command=delete_account)
        change_password_button = tkinter.Button(config_window, text="Cambiar contraseña", command=change_password)
        change_name_button = tkinter.Button(config_window, text="Cambiar nombre", command=change_name)

        

        name_label.grid(row=20, column=2, sticky="nsw")
        password_label.grid(row=22, column=2, sticky="nsw")
        confirm_password_label.grid(row=24, column=2, sticky="nsw")

        name_entry.grid(row=20, column=3, sticky="nsew")
        password_entry.grid(row=22, column=3, sticky="nsew")
        confirm_password_entry.grid(row=24, column=3, sticky="nsew")

        change_name_button.grid(row=20, column=5, sticky="nsew")
        change_password_button.grid(row=22, column=5, sticky="nsew")
        delete_button.grid(row=26, column=3, sticky="nsew")


    def create_note(self) -> None:
        def add_note(data):
            self.user.create_note(data[0], data[1], data[2], "Arial", 11)
            db = DataBase()
            try:
                db.insert_note(self.user.user_id, Note(data[0], data[1], data[2], "Arial", 11))
                note_window.destroy()
            except:
                db.create_notes_database()
                db.create_notes_table()
                db.insert_note(self.user.user_id, Note(data[0], data[1], data[2], "Arial", 11))
                note_window.destroy()
            finally:
                self.last_note.config(text=data[0])
                self.user.earn_points(5)
                self.score_label.config(text=f"Puntos: {self.user.points}")
                DataBase().update(self.user.user_id, "puntaje", self.user.points)

        def verify_fields():
            if name_entry.get().strip(' ') == "":
                print("Ingrese correctamente los campos")
            else:
                data = [name_entry.get(), description_entry.get("1.0", "end"), selection.get()]
                add_note(data)

        note_window = tkinter.Toplevel(self)
        note_window.geometry("600x700")
        note_window.title("AJCalendar")
        note_window.resizable(False, False)
        note_window.config(bg="#2E2F33")
        selection = tkinter.StringVar()
        selection.set("Baja")
        name_entry = tkinter.Entry(note_window,
                                bg="white",
                                font=("Arial", 11),
                                foreground="black",
                                insertbackground="black", 
                                borderwidth=0
                            )

        relevance_menu = tkinter.OptionMenu(note_window, selection, *["Baja", "Media", "Alta"])
        
        description_entry = tkinter.Text(note_window,
                                        bg="white", 
                                        width=25, 
                                        height=4,
                                        insertbackground="black",
                                        foreground="black",
                                        borderwidth=0
                                    )

        self.create_item(note_window, name_entry,
                        relevance_menu,
                        description_entry)
        
        title_label = tkinter.Label(note_window, text="Nota",bg="#2E2F33",font=("Arial", 20),
                                        foreground="white")
        
        photo_image_7 = PhotoImage(master=note_window, 
                                    file="assets/images/CreNota.png"
                                    )

        create_note_button = tkinter.Button(note_window,
                                                image=photo_image_7,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=verify_fields
                                            )
        
        title_label.place(width=150, height=100, x=225, y=20)
        create_note_button.place(width=250, height=100, x=125, y=450)
        note_window.mainloop()
    
    def create_task(self) -> None:
        def add_task(data):
            self.user.create_task(data[0], data[1], data[2], data[3], False)
            db = DataBase()
            try:
                db.insert_task(self.user.user_id, Task(data[0], data[1], data[2], data[3], False))
                task_window.destroy()
            except:
                db.create_tasks_database()
                db.create_tasks_table()
                db.insert_task(self.user.user_id, Task(data[0], data[1], data[2], data[3], False))
                task_window.destroy()
            finally:
                self.last_task.config(text=data[0])

        def verify_fields():
            if name_entry.get().strip(' ') == "":
                print("Rellene los campos, por favor")
            elif calendar.get_date().year < datetime.now().year:
                print("Ingrese fecha válida")
            elif calendar.get_date().month < datetime.now().month:
                print("Ingrese fecha válida")
            elif calendar.get_date().day < datetime.now().day:
                print("Ingrese fecha válida")
            else:
                data = [name_entry.get(), description_entry.get("1.0", "end"), selection.get(), calendar.get_date()]
                add_task(data)

        task_window = tkinter.Toplevel(self)
        task_window.geometry("600x720")
        task_window.title("AJCalendar")
        task_window.resizable(False, False)
        task_window.config(bg="#2E2F33")

        selection = tkinter.StringVar()
        selection.set("Baja")
        name_entry = tkinter.Entry(task_window,
                                bg="white",
                                font=("Arial", 11),
                                foreground="black",
                                insertbackground="black", 
                                borderwidth=0
                            )

        relevance_menu = tkinter.OptionMenu(task_window, selection, *["Baja", "Media", "Alta"])
        
        description_entry = tkinter.Text(task_window,
                                        bg="white", 
                                        width=25, 
                                        height=4,
                                        insertbackground="black",
                                        foreground="black",
                                        borderwidth=0
                                    )

        self.create_item(task_window, name_entry,
                        relevance_menu,
                        description_entry)

        title_label = tkinter.Label(task_window, 
                                    text="Tarea",
                                    bg="#2E2F33",
                                    font=("Arial", 20),
                                    foreground="white"
                                )
        due_date_label = tkinter.Label(task_window,
                                        text="Fecha límite:",
                                        bg="#2E2F33",
                                        font=("Arial", 11),
                                        foreground="white"
                                    )

        calendar = DateEntry(task_window)

        photo_image_7 = PhotoImage(master=task_window, 
                                    file="assets/images/CreNota.png"
                                    )

        create_task_button = tkinter.Button(task_window,
                                                image=photo_image_7,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=verify_fields
                                            )
        title_label.place(width=150, height=100, x=225, y=20)
        due_date_label.place(width=150, height=30, x=0, y=400)
        calendar.place(width=100, height=30, x=170, y=400)
        create_task_button.place(width=250, height=100, x=125, y=500)
        task_window.mainloop()
    
    def create_meeting(self) -> None:
        def add_meeting(data):
            self.user.create_meeting(data[0], data[1], data[2], data[3], data[4])
            db = DataBase()
            try:
                db.insert_meeting(self.user.user_id, Meeting(data[0], data[1], data[2], data[3], data[4]))
                meeting_window.destroy()
            except:
                db.create_meetings_database()
                db.create_meetings_table()
                db.insert_meeting(self.user.user_id, Meeting(data[0], data[1], data[2], data[3], data[4]))
                meeting_window.destroy()
            finally:
                self.last_meeting.config(text=data[0])

        def verify_fields():
            if (name_entry.get().strip(' ') == ""
                or link_entry.get().strip(' ') == ""):
                print("Rellene los campos, por favor")
            elif calendar.get_date().year < datetime.now().year:
                print("Ingrese fecha válida")
            elif calendar.get_date().month < datetime.now().month:
                print("Ingrese fecha válida")
            elif calendar.get_date().day < datetime.now().day:
                print("Ingrese fecha válida")
            elif (calendar.get_date().day == datetime.now().day and int(hour.get()) < datetime.now().hour):
                print("Ingrese hora válida")
            elif (int(hour.get()) == datetime.now().hour and int(minute.get()) < datetime.now().minute):
                print("Ingrese minuto válido")
            else:
                data = [
                    name_entry.get(), 
                    description_entry.get("1.0", "end"), 
                    selection.get(),  
                    link_entry.get(),
                    str(calendar.get_date())+". "+str(hour.get())+":"+str(minute.get())
                ]
                add_meeting(data)
        meeting_window = tkinter.Toplevel(self)
        meeting_window.geometry("600x700")
        meeting_window.title("AJCalendar")
        meeting_window.resizable(False, False)
        meeting_window.config(bg="#2E2F33")

        selection = tkinter.StringVar()
        selection.set("Baja")

        name_entry = tkinter.Entry(meeting_window,
                                bg="white",
                                font=("Arial", 11),
                                foreground="black",
                                insertbackground="black", 
                                borderwidth=0
                            )

        relevance_menu = tkinter.OptionMenu(meeting_window, selection, *["Baja", "Media", "Alta"])
        description_entry = tkinter.Text(meeting_window,
                                        bg="white", 
                                        width=25, 
                                        height=4,
                                        insertbackground="black",
                                        foreground="black",
                                        borderwidth=0
                                    )

        self.create_item(meeting_window, name_entry,
                        relevance_menu,
                        description_entry)

        minute = tkinter.StringVar()
        hour = tkinter.StringVar()
        minute_options = [int(i) for i in range(0, 60)]
        hour_options = [int(i) for i in range(0, 24)]
        minute.set(minute_options[0])
        hour.set(hour_options[0])

        title_label = tkinter.Label(meeting_window, 
                                    text="Reunión",
                                    bg="#2E2F33",
                                    font=("Arial", 20),
                                    foreground="white"
                                )

        due_date_label = tkinter.Label(meeting_window,
                                        text="Fecha:",
                                        bg="#2E2F33",
                                        font=("Arial", 11),
                                        foreground="white"
                                    )
        time_label = tkinter.Label(meeting_window,
                                    text="Hora:Minuto",
                                    bg="#2E2F33",
                                    font=("Arial", 11),
                                    fg="white")

        calendar = DateEntry(meeting_window)

        hour_selection = tkinter.OptionMenu(meeting_window, hour, *hour_options)
        minutes_selection = tkinter.OptionMenu(meeting_window, minute, *minute_options)

        hour_selection.config(bd=0)
        minutes_selection.config(bd=0)

        link_label = tkinter.Label(meeting_window,
                                    text="Link:",
                                    bg="#2E2F33",
                                    font=("Arial", 11),
                                    fg="white")

        link_entry = tkinter.Entry(meeting_window,
                                    bg="white",
                                    font=("Arial", 11),
                                    foreground="black",
                                    insertbackground="black", 
                                    borderwidth=0
                                )

        photo_image_7 = PhotoImage(master=meeting_window, 
                                file="assets/images/CreNota.png"
                                )

        create_meeting_button = tkinter.Button(meeting_window,
                                                image=photo_image_7,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=verify_fields
                                            )
        
        title_label.place(width=150, height=100, x=225, y=20)
        due_date_label.place(width=150, height=30, x=0, y=400)
        calendar.place(width=100, height=30, x=170, y=400)
        time_label.place(width=100, height=30, x=30, y=450)
        hour_selection.place(width=100, height=30, x=150, y=450)
        minutes_selection.place(width=100, height=30, x=270, y=450)
        link_label.place(width=100, height=30, x=30, y=500)
        link_entry.place(width=320, height=30, x=150, y=500)
        create_meeting_button.place(width=250, height=100, x=125, y=550)
        meeting_window.mainloop()
    
    def create_item(self, root: tkinter.Tk, name_entry: tkinter.Entry,
                    relevance_menu: tkinter.OptionMenu,
                    description_entry: tkinter.Entry):
        
        name_label = tkinter.Label(root, text="Nombre:", bg="#2E2F33",font=("Arial", 11),
                                        foreground="white")
    
        relevance_label = tkinter.Label(root, 
                                        text="Relevancia:", bg="#2E2F33",font=("Arial", 11),
                                        foreground="white")

        description_label = tkinter.Label(root, 
                                        text="Descripción:",
                                        bg="#2E2F33",
                                        font=("Arial", 11),
                                        foreground="white")    
        
        name_label.place(width=75, height=30, x=20, y=120)
        name_entry.place(width=320, height=30, x=130, y = 120)
        relevance_label.place(width=95, height=20, x=25, y=190)
        relevance_menu.place(width=100, height=30, x=150, y=190)
        description_label.place(width=100, height=30, x=20, y=300)
        description_entry.place(width=320, height=100, x=130, y=275)

    def note_window(self) -> None:
        def remove_note():
            try:
                index = self.get_index_tree(note_tree, self.user.notes)
                note_tree.delete(note_tree.selection())
                DataBase().delete_item("tareas", self.user.user_id, self.user.notes[index].name)
                self.user.remove_note(self.user.notes[index])
            except:
                print("Por favor, seleccione el elemento a eliminar")
        note_window = tkinter.Toplevel(self)
        note_window.title("AJCalendar")
        note_window.geometry("800x400")
        note_window.resizable(False, False)

        columns = ("name", "description", "relevance", "creation_date")

        note_tree = Treeview(note_window, columns=columns, show="headings")

        note_tree.heading("name", text="Nombre")
        note_tree.heading("description", text="Descripción")
        note_tree.heading("relevance", text="Relevancia")
        note_tree.heading("creation_date", text="Fecha de creación")

        note_tree.column("name", width=150, anchor="center")
        note_tree.column("description", width=250, anchor="center")
        note_tree.column("relevance", width=100, anchor="center")
        note_tree.column("creation_date", width=150, anchor="center")

        for note in self.user.notes:
            values = (note.name, note.description, 
                    note.relevance_level, note.creation_date)
            note_tree.insert('', 0, values=values)
        note_tree.grid(row=0, column=0, sticky="nsew")
        delete_button = tkinter.Button(note_window, text="Eliminar nota", bg="#C42B1C", fg="white", command=remove_note)
        
        delete_button.place(width=125, height=50, x=150, y=300)
        self.scrollbar(note_window, note_tree)

        note_window.mainloop()

    def task_window(self) -> None:
        def complete_task():
            try:
                self.user.earn_points(10)
                self.score_label.config(text=f"Puntos: {self.user.points}")
                DataBase().update(self.user.user_id, "puntaje", self.user.points)
                remove_task()
            except:
                pass  
        def remove_task():
            try:
                index = self.get_index_tree(task_tree, self.user.tasks)
                task_tree.delete(task_tree.selection())
                DataBase().delete_item("tareas", self.user.user_id, self.user.tasks[index].name)
                self.user.remove_task(self.user.tasks[index])
            except:
                print("Por favor, seleccione el elemento a eliminar")
        task_window = tkinter.Toplevel(self)
        task_window.title("AJCalendar")
        task_window.geometry("850x400")
        task_window.resizable(False, False)

        columns = ("name", "description", "relevance", "creation_date", "due_date")

        task_tree = Treeview(task_window, columns=columns, show="headings")

        task_tree.heading("name", text="Nombre")
        task_tree.heading("description", text="Descripción")
        task_tree.heading("relevance", text="Relevancia")
        task_tree.heading("creation_date", text="Fecha de creación")
        task_tree.heading("due_date", text="Fecha límite")

        task_tree.column("name", width=150, anchor="center")
        task_tree.column("description", width=250, anchor="center")
        task_tree.column("relevance", width=100, anchor="center")
        task_tree.column("creation_date", width=150, anchor="center")
        task_tree.column("due_date", width=150, anchor="center")

        for task in self.user.tasks:
            values = (task.name, task.description, 
                    task.relevance_level, task.creation_date,
                    task.due_date)
            task_tree.insert('', 0, values=values)
        task_tree.grid(row=0, column=0, sticky="nsew")
        delete_button = tkinter.Button(task_window, text="Eliminar tarea", bg="#C42B1C", fg="white", command=remove_task)
        complete_button = tkinter.Button(task_window, text="Marcar hecho", bg="#1ED760", fg="white", command=complete_task)
        
        delete_button.place(width=125, height=50, x=150, y=300)
        complete_button.place(width=125, height=50, x=450, y=300)
        self.scrollbar(task_window, task_tree)

        task_window.mainloop()

    def meeting_window(self) -> None:
        def complete_meeting():
            try:
                self.user.earn_points(10)
                self.score_label.config(text=f"Puntos: {self.user.points}")
                DataBase().update(self.user.user_id, "puntaje", self.user.points)
                remove_meeting()
            except:
                pass  
        def remove_meeting():
            try:
                index = self.get_index_tree(meeting_tree, self.user.meetings)
                meeting_tree.delete(meeting_tree.selection())
                DataBase().delete_item("reuniones", self.user.user_id, self.user.meetings[index].name)
                self.user.remove_meeting(self.user.meetings[index])
            except:
                print("Por favor, seleccione el elemento a eliminar")
        meeting_window = tkinter.Toplevel(self)
        meeting_window.title("AJCalendar")
        meeting_window.geometry("1050x400")
        meeting_window.resizable(False, False)

        columns = ("name", "description", "relevance", "creation_date", "link", "meeting_date")

        meeting_tree = Treeview(meeting_window, columns=columns, show="headings")

        meeting_tree.heading("name", text="Nombre")
        meeting_tree.heading("description", text="Descripción")
        meeting_tree.heading("relevance", text="Relevancia")
        meeting_tree.heading("creation_date", text="Fecha de creación")
        meeting_tree.heading("link", text="Link")
        meeting_tree.heading("meeting_date", text="Fecha")

        meeting_tree.column("name", width=150, anchor="center")
        meeting_tree.column("description", width=200, anchor="center")
        meeting_tree.column("relevance", width=100, anchor="center")
        meeting_tree.column("creation_date", width=150, anchor="center")
        meeting_tree.column("creation_date", width=150, anchor="center")
        meeting_tree.column("creation_date", width=150, anchor="center")

        for meeting in self.user.meetings:
            values = (meeting.name, meeting.description, 
                    meeting.relevance_level, meeting.creation_date,
                    meeting.link, meeting.meeting_date)
            meeting_tree.insert('', 0, values=values)
        meeting_tree.grid(row=0, column=0, sticky="nsew")
        delete_button = tkinter.Button(meeting_window, text="Eliminar reunión", bg="#C42B1C", fg="white", command=remove_meeting)
        complete_button = tkinter.Button(meeting_window, text="Marcar asistido", bg="#1ED760", fg="white", command=complete_meeting)

        delete_button.place(width=125, height=50, x=150, y=300)
        complete_button.place(width=125, height=50, x=450, y=300)
        self.scrollbar(meeting_window, meeting_tree)

        meeting_window.mainloop()

    def get_index_tree(self, tree: Treeview, item_list: list) -> int:
        for item in item_list:
            if tree.item(tree.selection())["values"][0] == item.name:
                return item_list.index(item)

    def scrollbar(self, root: tkinter.Tk, tree: Treeview) -> None:
        y_scrollbar = Scrollbar(root, orient="vertical", command=tree.yview)
        x_scrollbar = Scrollbar(root, orient="horizontal", command=tree.xview)
        tree.configure(yscroll=y_scrollbar.set, xscroll=x_scrollbar.set)
        y_scrollbar.grid(row=0, column=1, sticky="ns")
        x_scrollbar.grid(row=1, column=0, sticky="ew")