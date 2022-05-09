from ctypes import windll
from pyglet.font import add_file
from container import Container
from user import User
from database import DataBase
from werkzeug.security import check_password_hash
import tkinter
from tkinter import PhotoImage
from tkinter import font

add_file("assets/fonts/Francois_One/FO.ttf")
windll.shcore.SetProcessDpiAwareness(1)

class LoginWindow:
    
    def __init__(self) -> None:
        self.login_window = tkinter.Tk()
        self.login_window.geometry("900x600")
        self.login_window.eval('tk::PlaceWindow . center ')
        self.login_window.title("AJCalendar")
        self.login_window.resizable(False, False)
        self.login_window.config(bg="#2E2F33")
        self.login_window.overrideredirect(1)
        self.title_bar = tkinter.Frame(self.login_window, bg='#2E2F33', bd=0)
        self.close_button = tkinter.Button(self.title_bar, 
                                            foreground="white", 
                                            text="×",
                                            font=("Arial", 20),
                                            borderwidth=0,
                                            bg="#2E2F33",
                                            activebackground="#FF605C",
                                            activeforeground="white",
                                            command=self.login_window.destroy
                                        )
        self.title_bar.place(height=50, width=900, x=0, y=0)
        self.close_button.pack(side='right', ipadx=20)
        self.title_bar.bind('<B1-Motion>', self.move_window)
        for i in range(0, 50):
            tkinter.Grid.rowconfigure(self.login_window, i, weight=1)
        
        for i in range(0, 10):
            tkinter.Grid.columnconfigure(self.login_window, i, weight=1)
        
        self.logo = PhotoImage(file="assets/images/logo.png")
        self.logo_label = tkinter.Label(self.title_bar, image=self.logo, bg="#2E2F33")
        self.logo_label.bind('<B1-Motion>', self.move_window)
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

        self.logo_label.pack(side="left", padx=10)
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
        register_window.geometry("300x500")
        register_window.resizable(False, False)

        user_register_label = tkinter.Label(register_window, text="Usuario:")
        password_register_label = tkinter.Label(register_window, text="Contraseña:")
        password_confirmation_label = tkinter.Label(register_window, text="Confirmar contraseña:")
        user_register_entry = tkinter.Entry(register_window)
        password_register_entry = tkinter.Entry(register_window, show="*")
        password_confirmation_entry = tkinter.Entry(register_window, show="*")
        regis_button = tkinter.Button(register_window, text="Registrar", command=verify_user)

        user_register_label.place(height=20, width=75, x= 82, y=200)
        user_register_entry.place(height=20, width=75, x= 162, y=200)
        password_register_label.place(height=20, width=100, x= 67, y=225)
        password_register_entry.place(height=20, width=75, x= 162, y=225)
        password_confirmation_label.place(height=20, width=150, x= 17, y=250)
        password_confirmation_entry.place(height=20, width=75, x= 162, y=250)
        regis_button.place(height=25, width=75, x=125, y=300)

        register_window.mainloop()

class ContainerWindow():
    def __init__(self, user: User) -> None:
        self.container_window = tkinter.Tk()
        self.user = user
        self.container_window.geometry("1000x600")
        self.container_window.title("AJCalendar")
        self.container_window.resizable(False, False)
        self.container_window.config(bg="#F4F3DD")

        self.container_window.mainloop()
