from ctypes import windll
from turtle import title
from container import Container
from user import User
from database import DataBase
from werkzeug.security import check_password_hash
import tkinter
from tkinter import PhotoImage

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
                                        font=("FO", 14),
                                        foreground="white"
                                    )
        self.pass_label = tkinter.Label(self.login_window, 
                                        text="Contraseña:", 
                                        bg="#2E2F33",
                                        font=("FO", 14),
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
                                        font=("FO", 14),
                                        foreground="black",
                                        insertbackground="black", 
                                        borderwidth=0)
        self.pass_entry = tkinter.Entry(self.login_window, 
                                        show="*", 
                                        bg="white",
                                        insertbackground="black",
                                        font=("FO", 14),
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
    
    def move_window(self, event):
        self.login_window.geometry('+{}+{}'.format(event.x_root, event.y_root))
    
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
                    ContainerWindow(User(user[0], user[1], user[2], user[3]))
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


        user_register_label = tkinter.Label(register_window, text="Usuario:",bg="#2E2F33",font=("FO", 14),
                                        foreground="white")
        password_register_label = tkinter.Label(register_window, text="Contraseña:",bg="#2E2F33",font=("FO", 14),
                                        foreground="white")
        password_confirmation_label = tkinter.Label(register_window, text="Confirmar contraseña:",bg="#2E2F33",font=("FO", 14),
                                        foreground="white")
        user_register_entry = tkinter.Entry(register_window,bg="white",
                                        font=("FO", 14),
                                        foreground="black",
                                        insertbackground="black", 
                                        borderwidth=0)
        password_register_entry = tkinter.Entry(register_window, show="*",bg="white",
                                        insertbackground="black",
                                        font=("FO", 14),
                                        foreground="black", 
                                        borderwidth=0)
        password_confirmation_entry = tkinter.Entry(register_window, show="*",bg="white",
                                        insertbackground="black",
                                        font=("FO", 14),
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
        #regis_button = tkinter.Button(register_window, text="Registrar", command=verify_user)

        user_register_label.grid(row=25, column=3,sticky="nsew")
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
                                                command=self.click_note)

        
        self.photo_image_5 = PhotoImage(file="assets/images/TAREA.png")

        self.task_button = tkinter.Button(self.container_window,
                                                image=self.photo_image_5,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0
                                            )
        self.photo_image_6 = PhotoImage(file="assets/images/MEET.png")

        self.meet_button = tkinter.Button(self.container_window,
                                                image=self.photo_image_6,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0
                                            )
        #notas_button = tkinter.Button(self.container_window, text="Notas")
        #task_button = tkinter.Button(self.container_window, text="Tareas")
        #meet_button = tkinter.Button(self.container_window, text="Reuniones")
        
        self.notas_button.grid(row=10, column=1,sticky="nsew")
        self.task_button.grid(row=13, column=1,sticky="nsew")
        self.meet_button.grid(row=16, column=1,sticky="nsew")
        self.container_window.mainloop()

       
    def click_note(self) -> None:
        note_window = tkinter.Tk()
        note_window.geometry("600x400")
        note_window.title("AJCalendar")
        note_window.resizable(False, False)
        note_window.config(bg="#2E2F33")

        for i in range(0, 50):
            tkinter.Grid.rowconfigure(note_window, i, weight=1)
        
        for i in range(0, 20):
            tkinter.Grid.columnconfigure(note_window, i, weight=1)
        
        title_label = tkinter.Label(note_window, text="Crear nota",bg="#2E2F33",font=("FO", 20),
                                        foreground="white")
        name_note_label = tkinter.Label(note_window, text="Nombre:",bg="#2E2F33",font=("FO", 12),
                                        foreground="white")
       
        relevancia_note_label = tkinter.Label(note_window, text="Relevancia:",bg="#2E2F33",font=("FO", 12),
                                        foreground="white")
        descripcion_note_label = tkinter.Label(note_window, 
                                        text="Descripcion:",
                                        bg="#2E2F33",
                                        font=("FO", 12),
                                        foreground="white")                                
        name_note_entry = tkinter.Entry(note_window,bg="white",
                                        font=("FO", 12),
                                        foreground="black",
                                        insertbackground="black", 
                                        borderwidth=0)
        
        

        relevancia_note_entry_1 = tkinter.Checkbutton(note_window,bg="#2E2F33", text="Alta",activebackground="#2E2F33",foreground="white")
                                        
        relevancia_note_entry_2 = tkinter.Checkbutton(note_window, bg="#2E2F33", text="Media",activebackground="#2E2F33",foreground="white")

        relevancia_note_entry_3 = tkinter.Checkbutton(note_window,bg="#2E2F33", text="Baja",activebackground="#2E2F33",foreground="white")
        
        descripcion_note_entry = tkinter.Text (note_window,bg="white", width=30, height=4,
                                        insertbackground="black",
                                        foreground="black",
                                        borderwidth=0)
        
        
        photo_image_7 = PhotoImage(master=note_window, file="assets/images/CreNota.png")

        create_note_button = tkinter.Button(note_window,
                                                image=photo_image_7,
                                                bg="#2E2F33",
                                                activebackground="#2E2F33",
                                                borderwidth=0
                                            )
        
        title_label.grid(row=8, column=3,sticky="nsew")
        name_note_label.grid(row=10, column=2,sticky="nsew")
        name_note_entry.grid(row=10, column=3, sticky="nsew")
        
        relevancia_note_label.grid(row=14, column=2, sticky="nsew")
        relevancia_note_entry_1.grid(row=14, column=3, sticky="nsew")
        relevancia_note_entry_2.grid(row=14, column=4, sticky="nsew")
        relevancia_note_entry_3.grid(row=14, column=5, sticky="nsew")
        descripcion_note_label.grid(row=16, column=2, sticky="nsew")
        descripcion_note_entry.grid(row=16, column=3, sticky="nsew")
        create_note_button.grid(row=19, column=3, sticky ="nsew")

        note_window.mainloop()
    
           

    
        
   
    
