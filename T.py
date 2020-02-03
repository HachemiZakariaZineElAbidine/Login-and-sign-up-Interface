from tkinter import *
import os

def register_user():
    family_name_info = family_name.get()
    first_name_info = first_name.get()
    user_name_info = user_name.get()
    e_mail_info = e_mail.get()
    password_info = password.get()
    confirm_info = confirm_password.get()
    if first_name_info == "":
      Label(screen1, text="Give a First Name", fg = "red").pack()
    elif family_name_info == "":
      Label(screen1, text="Give a Family Name", fg = "red").pack()
    elif user_name_info == "":
      Label(screen1, text="Give a User Name", fg = "red").pack()
    elif e_mail_info == "":
      Label(screen1, text="Give an E-mail", fg = "red").pack()
    elif password_info == "":
      Label(screen1, text="Give a Password", fg = "red").pack()
    elif confirm_password == "":
      Label(screen1, text="Confirm your sassword", fg = "red").pack()
    else:

     if password_info != confirm_info :
      Label(screen1, text="Password error", fg = "red").pack()
     else:
      family_name_Entry.delete(0, END)
      first_name_Entry.delete(0, END)
      user_name_Entry.delete(0, END)
      e_mail_Entry.delete(0, END)
      password_Entry.delete(0, END)
      confirm_password_Entry.delete(0, END)

      with open(user_name_info+".txt", "w") as fic:
        fic.write(family_name_info+"\n")
        fic.write(first_name_info+"\n")
        fic.write(user_name_info+"\n")
        fic.write(e_mail_info+"\n")
        fic.write(password_info)


      Label(screen1,text = "").pack()
      Label(screen1, text = "Regestration Succes", fg = "green").pack()


def register_screen():

    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Sign in")
    screen1.geometry("300x430")
    screen1.maxsize(300, 500)
    screen1.minsize(300, 430)

    global first_name
    global family_name
    global password
    global user_name
    global e_mail
    global confirm_password
    
    first_name = StringVar()
    family_name = StringVar()
    password = StringVar()
    user_name = StringVar()
    e_mail = StringVar()
    confirm_password = StringVar()

    global first_name_Entry
    global family_name_Entry
    global password_Entry
    global user_name_Entry
    global e_mail_Entry
    global confirm_password_Entry


    Label(screen1, text = "Sign in", height = "2", width = "30", font = ("Arial black", 20), fg = "black").pack()
    Label(screen1, text = "First name *", font = ("Arial black", 10)).pack()
    first_name_Entry =  Entry(screen1, textvariable = first_name )
    first_name_Entry.pack()
    Label(screen1, text = "Family name *", font = ("Arial black", 10)).pack()
    family_name_Entry = Entry(screen1, textvariable = family_name)
    family_name_Entry.pack()
    Label(screen1, text = "User name *", font = ("Arial black", 10)).pack()
    user_name_Entry = Entry(screen1, textvariable = user_name)
    user_name_Entry.pack()
    Label(screen1, text = "E-mail*", font = ("Arial black", 10)).pack()
    e_mail_Entry = Entry(screen1, textvariable = e_mail)
    e_mail_Entry.pack()
    Label(screen1, text = "Password *",font = ("Arial black", 10)).pack()
    password_Entry = Entry(screen1, show = "*", textvariable = password)
    password_Entry.pack()
    Label(screen1, text = "Confirm password *", font = ("Arial black", 10)).pack()
    confirm_password_Entry = Entry(screen1, show = "*", textvariable = confirm_password)
    confirm_password_Entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1,text = "Sign in", height = "2", width = "20", command = register_user).pack()


def login_verify():
    username_verify = username1.get()
    password_verify = password1.get()

    username_Entry1.delete(0, END)
    password_Entry1.delete(0, END)

    list = os.listdir()
    username_verify += ".txt"
    if username_verify in list :
     with open(username_verify,"r") as fic:
       verify = fic.read().splitlines()
       if password_verify == verify[4] :
         Label(screen2, text = "Login Succes", fg = "green").pack()
       else:
         Label(screen2, text = "Password Error", fg = "red").pack()
    else:
     Label(screen2, text = "User not found", fg = "red").pack()
         

def login_screen():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x280")
    screen2.maxsize(300, 280)
    screen2.minsize(300, 280)

    global username1
    global password1
    global username_Entry1
    global password_Entry1

    username1 = StringVar()
    password1 = StringVar()

    Label(screen2, text = "Login", height = "2", width = "30",  fg = "black",font=("Arial black", 20)).pack()
    Label(screen2, text = "Username *", fg = "black", font = ("Arial black", 10)).pack()
    username_Entry1 = Entry(screen2, textvariable = username1)
    username_Entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password *", fg = "black", font = ("Arial black", 10)).pack()
    password_Entry1 = Entry(screen2, textvariable = password1, show = "*")
    password_Entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", height = "2", width = "20", command = login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.title("Login and Register")
    screen.geometry("300x250")
    screen.maxsize(300, 250)
    screen.minsize(300, 250)
    Label(screen, text = "Welcome", height = "2", width = "30", font = ("Arial black", 20), fg = "Black").pack()
    Label(screen, text = "").pack()
    Button(screen, text = "Login", height = "2", width = "30", command = login_screen).pack()
    Label(screen, text = "").pack()
    Button(screen, text = "Sign in", height = "2", width = "30", command = register_screen).pack()
    Label(screen, text = "").pack()

    screen.mainloop()

main_screen()