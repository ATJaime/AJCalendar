from ctypes import windll
from datetime import datetime
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

class LoginWindow: 
    def __init__(self) -> None:
        self.login_window = tkinter.Tk()
        self.login_window.geometry("900x600")
        self.login_window.title("AJCalendar")
        self.login_window.resizable(False, False)
        self.login_window.config(bg="#2E2F33")
        
        for i in range(0, 50):
            tkinter.Grid.rowconfigure(self.login_window, i, weight=1)
        
        for i in range(0, 10):
            tkinter.Grid.columnconfigure(self.login_window, i, weight=1)
 
        self.user_label = tkinter.Label(self.login_window, 
                                        text="Usuario:", 
                                        bg="#2E2F33",
                                        font=("Arial", 14),
                                        foreground="white"
                                    )
        self.pass_label = tkinter.Label(self.login_window, 
                                        text="Contraseña:", 
                                        bg="#2E2F33",
                                        font=("Arial", 14),
                                        foreground="white"
                                    )

        self.photo_image = PhotoImage(file="assets/images/register_button.png")

        self.register_button = tkinter.Button(self.login_window,
                                                image=self.photo_image,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=self.register
                                            )
        
        self.photo_image2 = PhotoImage(file="assets/images/login_button.png")
        self.login_button = tkinter.Button(self.login_window,
                                            image=self.photo_image2,
                                            bg="#2E2F33",
                                            activebackground="#2E2F33",
                                            borderwidth=0,
                                            command=self.verify_user_information,
                                        )
        self.user_entry = tkinter.Entry(self.login_window, 
                                        bg="white",
                                        font=("Arial", 14),
                                        foreground="black",
                                        insertbackground="black", 
                                        borderwidth=0)
        self.pass_entry = tkinter.Entry(self.login_window, 
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
        self.login_window.mainloop()
    
    def verify_user_information(self) -> None:
        users = DataBase().read_rows("usuarios")
        if (self.user_entry.get().strip(' ') == ""
            or self.pass_entry.get().strip(' ') == ""):
            print("Por favor, rellene los campos")
        else:
            for user in users:
                if (self.user_entry.get() == user[1] and
                    check_password_hash(user[2], self.pass_entry.get())):
                    self.login_window.destroy()
                    logged_user = User(user[0], user[1], user[2], user[3])
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
                            logged_user.create_note(meeting[1], meeting[2], meeting[3], meeting[4], meeting[5])
                    except:
                        pass
                    ContainerWindow(logged_user)
                    return
            print("Los campos diligenciados no son correctos")
                    
    
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

        register_window = tkinter.Tk()
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


class ContainerWindow():
    def __init__(self, user: User) -> None:
        self.container_window = tkinter.Tk()
        self.user = user
        self.container_window.geometry("900x600")
        self.container_window.title("AJCalendar")
        self.container_window.resizable(False, False)
        self.container_window.config(bg="#2E2F33")
        
        for i in range(0, 50):
            tkinter.Grid.rowconfigure(self.container_window, i, weight=1)
        
        for i in range(0, 10):
            tkinter.Grid.columnconfigure(self.container_window, i, weight=1)
    

        self.photo_image_3 = PhotoImage(file="assets/images/NOTAS.png")

        self.notas_button = tkinter.Button(self.container_window,
                                                image=self.photo_image_3,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0, 
                                                command=self.create_note
                                            )

        
        self.photo_image_5 = PhotoImage(file="assets/images/TAREA.png")

        self.task_button = tkinter.Button(self.container_window,
                                                image=self.photo_image_5,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=self.create_task
                                            )
        self.photo_image_6 = PhotoImage(file="assets/images/MEET.png")

        self.meet_button = tkinter.Button(self.container_window,
                                                image=self.photo_image_6,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0,
                                                command=self.create_meeting,
                                            )
        try:                                
            self.last_note = tkinter.Label(self.container_window, text=user.notes[-1])
        except:
            self.last_note = tkinter.Label(self.container_window, text="NO HAY NOTAS")
        try:
            self.last_task = tkinter.Label(self.container_window, text=user.tasks[-1])
        except:
            self.last_task = tkinter.Label(self.container_window, text="NO HAY TAREAS")

        try:
            self.last_meeting = tkinter.Label(self.container_window, text=user.meetings[-1])
        except:
            self.last_meeting = tkinter.Label(self.container_window, text="NO HAY REUNIONES")

        self.last_note.config(font=("Arial", 18), bg="#2E2F33", fg="white")
        self.last_task.config(font=("Arial", 18), bg="#2E2F33", fg="white")
        self.last_meeting.config(font=("Arial", 18), bg="#2E2F33", fg="white")

        self.last_note.grid(row=10, column=5, sticky="w")
        self.last_task.grid(row=13, column=5, sticky="w")
        self.last_meeting.grid(row=16, column=5, sticky="w")
        self.notas_button.grid(row=10, column=1, sticky="nsew")
        self.task_button.grid(row=13, column=1, sticky="nsew")
        self.meet_button.grid(row=16, column=1, sticky="nsew")
        self.container_window.mainloop()

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

        def verify_fields():
            if name_entry.get().strip(' ') == "":
                print("Ingrese correctamente los campos")
            else:
                data = [name_entry.get(), description_entry.get("1.0", "end"), selection.get()]
                add_note(data)

        note_window = tkinter.Tk()
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
            elif calendar.get_date().day < datetime.now().month:
                print("Ingrese fecha válida")
            else:
                data = [name_entry.get(), description_entry.get("1.0", "end"), selection.get(), calendar.get_date()]
                add_task(data)

        task_window = tkinter.Tk()
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
        def add_task(data):
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
            elif int(hour.get()) < datetime.now().hour:
                print("Ingrese hora válida")
            elif int(minute.get()) < datetime.now().minute:
                print("Ingrese minuto válido")
            else:
                data = [
                    name_entry.get(), 
                    description_entry.get("1.0", "end"), 
                    selection.get(),  
                    link_entry.get(),
                    str(calendar.get_date())+". "+str(hour.get())+":"+str(minute.get())
                ]
                add_task(data)
        meeting_window = tkinter.Tk()
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
        minute.set(minute_options[1])
        hour.set(hour_options[1])

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