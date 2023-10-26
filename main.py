from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                messagebox.showinfo(title=f"{website} info",
                                    message=f"Email: {data[website]['Email']}\nPassword: {data[website]['Password']}")
            else:
                messagebox.showinfo(title="Oops", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "atiogpx@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search",command=find_password, width=14)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password, width=14)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

window.mainloop()
