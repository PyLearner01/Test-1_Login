from tkinter import *

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        print("Login successful!")
        # Add code to open the sales app here
    else:
        print("Invalid username or password")


root = Tk()
root.title("Sales App")
root.geometry("300x200")

label_username = Label(root, text="Username:")
label_username.pack()

entry_username = Entry(root)
entry_username.pack()

label_password = Label(root, text="Password:")
label_password.pack()

entry_password = Entry(root, show= "*")
entry_password.pack()

button_login = Button(root, text="Login", command=login)
button_login.pack()

root.mainloop()