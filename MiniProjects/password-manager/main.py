import tkinter.messagebox
from tkinter import *
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [(random.choice(letters)) for _ in range(random.randint(8, 10))]
    password_symbol = [(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    password_numbers = [(random.choice(numbers)) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbol + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_box.delete(0, END)
    pass_box.insert(0, password)
    pyperclip.copy(password)


# ----------------------------Search Website in data.json------------------- #
def search():
    wesite = website_box.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="OPPS", message="No data file found")
    else:
        if wesite in data:
            data_e_p = data[wesite]
            tkinter.messagebox.showinfo(title=f"{wesite}",
                                        message=f"Email: {data_e_p['email']}\nPassword: {data_e_p['password']}")
        else:
            tkinter.messagebox.showinfo(title="OPPS", message="No detail for this website exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_box.get().title()
    email = email_box.get()
    password = pass_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="OPPS", message="Yow left something empty")
    else:

        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        pass_box.delete(0, END)
        website_box.delete(0, END)
        tkinter.messagebox.showinfo(title="Information", message="Password is successfully saved.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_ing = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_ing)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_box = Entry(width=31)
website_box.focus()
website_box.grid(column=1, row=1)

email_box = Entry(width=51)
email_box.grid(column=1, row=2, columnspan=3)
email_box.insert(0, "shachitanandk@gmail.com")

pass_box = Entry(width=31)
pass_box.grid(column=1, row=3)

pass_generate = Button(text="Generate Password", command=generate_pass)
pass_generate.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", command=save_password)
add_button.config(width=43)
add_button.grid(column=1, row=4, columnspan=3)

search_butoon = Button(text="Search", command=search)
search_butoon.config(width=15)
search_butoon.grid(column=2, row=1)

window.mainloop()
