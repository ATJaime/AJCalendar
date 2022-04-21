import user
import window

user_1 = user.User("Default", "1234")
w = window.LogginWindow()
w.add_user(user_1)
w.start_window()

