import tkinter as tk
from json import JSONDecodeError
from tkinter import Entry, Button,messagebox,font
import secrets,string
import json
LENGTH =8

#Search
def search():
    website= website_entry.get()
    with open("password.json",'r') as data_file:
        try:
            data_in=json.load(data_file)
            password= data_in.get(website,f'No {website} found').get('password',"not found")
        except AttributeError:
            messagebox.showinfo("Error", message="Enter The Website Name")
        except JSONDecodeError:
            messagebox.showinfo(title="Error",message='What bro! Nothing here')
        else:
            messagebox.showinfo(title="Information", message=f'Your Password is: {password}')


#Passwordgenerator
def generate_password():
    character = string.ascii_letters+string.digits + string.punctuation
    password= ''.join(secrets.choice(character) for _ in range(LENGTH))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


#SavePassword
def save_password():
        website=website_entry.get()
        email=email_entry.get()
        password= password_entry.get()
        new_data= {website:{"email": email,
                        "password":password
                        }}
        is_ok= messagebox.askokcancel(title=website, message="just look bro,"
                                                      "is every thing correct"
                                                      " or not")
        if is_ok:
            try:
                with open("password.json", "r") as data_file:
                    data= json.load(data_file)
            except FileNotFoundError:
                with open("password.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            except JSONDecodeError:
                with open("password.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("password.json",'w') as data_file:
                    json.dump(data,data_file,indent=4)

            finally:
                password_entry.delete(0, tk.END)
                website_entry.delete(0, tk.END)
#UI
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
website_entry = Entry(width=24)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"Email@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(row=3,column=1)

#buttons
generate_button= Button(text="Generator",width=7,command=generate_password,bg="white",highlightthickness=0)
generate_button.grid(row=3,column=2, pady=0,padx=0)
add_button= Button(text="add",width=32,command=save_password,bg="white",highlightthickness=0)
add_button.grid(row=4,column=1,columnspan=2)
search_button= Button(text="Search",width=7,command=search,bg="white",highlightthickness=0)
search_button.grid(row=1,column=2,padx=0,pady=0)


window.mainloop()