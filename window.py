from container import Container
from user import User
import tkinter
from tkinter import PhotoImage
from tkinter import ttk

class LogginWindow:
    
    def __init__(self) -> None:
        self.loggin_window = tkinter.Tk()
        self.x_size = 500
        self.y_size = 500
        self.loggin_window.geometry(str(self.x_size)
                                    +"x"+str(self.y_size))
        self.loggin_window.title("AJCalendar")
        self.loggin_window.resizable(False, False)
        self.loggin_window.config(bg="#F4F3DD")
        
        self.user_label = tkinter.Label(self.loggin_window, 
                                        text="Usuario:", bg="#F4F3DD")
        self.pass_label = tkinter.Label(self.loggin_window, 
                                        text="Contraseña:", bg="#F4F3DD")
        self.photo = PhotoImage(file="assets/images/login_button.png")
        self.log_in_button = tkinter.Button(self.loggin_window, 
                                            image=self.photo,
                                            bg="#F4F3DD", 
                                            command=self.verify_user_information,
                                            borderwidth=0)
        self.user_entry = tkinter.Entry(self.loggin_window)
        self.pass_entry = tkinter.Entry(self.loggin_window, show="*")

        self.user_label.place(height=20, width=50, x=187, y=200)
        self.user_entry.place(height=20, width=75, x=237, y=200)
        self.pass_label.place(height=20, width=75, x=162, y=225)
        self.pass_entry.place(height=20, width=75, x=237, y=225)
        self.log_in_button.place(x=200, y=260)
        self.user_list = []

    
    def start_window(self) -> None:
        self.loggin_window.mainloop()

    def add_user(self, new_user: User):
        self.user_list.append(new_user)
    
    def verify_user_information(self) -> None:
        if self.user_list:
            for u in self.user_list:
                if (self.user_entry.get() == u.get_username() and 
                    self.pass_entry.get() == u.get_password()
                ):
                    self.open_container(u)
                    return
            print("Usuario inválido")
        else:
            print("No hay usuarios registrados")

    def open_container(self, u: User) -> None:
        self.loggin_window.destroy()
        ContainerWindow(u.get_container())

class ContainerWindow:
    def __init__(self, container: Container) -> None:
        self.container = container
        self.container_window = tkinter.Tk()
        self.x_size = 720
        self.y_size = 500
        self.container_window.geometry(str(self.x_size)+"x"+str(self.y_size))
        self.container_window.title("AJCalendar")
        self.container_window.config(bg="#F4F3DD")

        self.task_labels = []
        self.task_table = ttk.Treeview(self.container_window)
        self.task_table['columns'] =(
            "Descripción", 
            "Relevancia", 
            "Color", 
            "Fecha límite", 
            "Estado"
        )
        self.create_task_button = tkinter.Button(self.container_window, text="Agregar tarea", 
                                                command=self.create_task)
        self.create_task_button.place(height=40, width=100, x=300, y=260)

        self.container_window.mainloop()

    def create_task(self) -> None:
        def show_task() -> None:
            n = len(self.container.get_tasks())
            self.task_labels.append(tkinter.Label(self.container_window, 
                text=(description_entry.get(), relevance_entry.get(),
                color_entry.get(), dued_entry.get(), status_entry.get()))
            )
            self.task_labels[n-1].grid(row=n-1, column=0)
            self.create_task_button.grid(row=n, column=0)

        def add_task() -> None:
            if status_entry == "Por hacer":
                done = False
            else:
                done = True
            self.container.create_task(description=description_entry.get(), 
                relevance_level=int(relevance_entry.get()),
                color=color_entry.get(),
                due_date=dued_entry.get(),
                is_done=done
            )
            show_task()
            addt_window.destroy()    
            

        addt_window = tkinter.Tk()
        addt_window.geometry("350x350")

        description_label = tkinter.Label(addt_window, text="Descripción:")
        relevance_label = tkinter.Label(addt_window, text="Nivel de relevancia:")
        color_label = tkinter.Label(addt_window, text="Color")
        status_label = tkinter.Label(addt_window, text="Estado")
        dued_label = tkinter.Label(addt_window, text="Fecha límite")

        description_entry = tkinter.Entry(addt_window)
        relevance_entry = ttk.Combobox(
            addt_window,
            state="readonly",
            values=[1, 2, 3]
        )
        color_entry = tkinter.Entry(addt_window)
        status_entry = ttk.Combobox(
            addt_window,
            state="readonly",
            values=["Por hacer", "Hecho"]
        )
        dued_entry = tkinter.Entry(addt_window)

        add_task_button = tkinter.Button(addt_window, text="Agregar tarea", command=add_task)
               

        description_label.grid(row=1, column=1)
        description_entry.grid(
            row=1, 
            column=2, 
            padx=20, 
            pady=20, 
            ipadx=30, 
            ipady=30
        )
        relevance_label.grid(row=2, column=1)
        relevance_entry.grid(row=2, column=2)
        color_label.grid(row=3, column=1)
        color_entry.grid(row=3, column=2)
        dued_label.grid(row=4, column=1)
        dued_entry.grid(row=4, column=2)
        status_label.grid(row=5, column=1)
        status_entry.grid(row=5, column=2)
        
        add_task_button.grid(row=6, column=2)

        addt_window.mainloop()