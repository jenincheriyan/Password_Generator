import tkinter as tk
from tkinter import Entry, Button,messagebox
import secrets,string
LENGTH =12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    character = string.ascii_letters+string.digits + string.punctuation
    password= ''.join(secrets.choice(character) for _ in range(LENGTH))
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
        website=website_entry.get()
        email=email_entry.get()
        password= password_entry.get()
        is_ok= messagebox.askokcancel(title=website, message="just look bro,"
                                                      "is every thing correct"
                                                      " or not")
        if is_ok:
            with open("password.txt", "a") as data_save:
                data_save.write(f"{website} | {email} | {password}\n")
                password_entry.delete(0, tk.END)
                website_entry.delete(0, tk.END)
# ---------------------------- UI SETUP ------------------------------- #

window= tk.Tk()
window.title("Password Generator")
window.config(padx=40,pady=40, bg="white")
canvas= tk.Canvas(window,width=200, height=200,bg="white",highlightthickness=0)
img= tk.PhotoImage(file="/home/jenin/Desktop/password_generator/logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

#labels
label= tk.Label(window, text="website:",bg="white",highlightthickness=0)
label.grid(row=1,column=0)
label_email= tk.Label(window, text="Email/Username:", bg="white",highlightthickness=0)
label_email.grid(row=2,column=0)
label_password= tk.Label(window, text="Password:",bg="white",highlightthickness=0)
label_password.grid(row=3,column=0)

#entries
website_entry = Entry(width=35,)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"email@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons
generate_button= Button(text="Generator",width=10,command=generate_password,bg="white",highlightthickness=0)
generate_button.grid(row=3,column=2)
add_button= Button(text="add",width=35,command=save_password,bg="white",highlightthickness=0)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()