
import pyperclip
from tkinter import *
from tkinter import messagebox # since this is not a class, we need to be import that module seperately
from random import choice, randint, shuffle

# Password Generator
def generate_password():
    letters = [
        'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Save Password
def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing info", message="Please fill out all of the fields.")
    else:
        message_result = messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {email}"
                            f"\nPassword: {password}\nIs it ok to save?")  
        if message_result:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# UI setup

window = Tk()
window.title("Password Manager")
window.config(padx= 40, pady= 40)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0, columnspan=2, sticky='w')

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=45)
website_entry.grid(column=1 , row=1, columnspan=2, sticky='w')
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(column=1 ,row=2, columnspan=2)
email_entry.insert(END, "myemail@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky='w')

#Buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky='e')

save_btn = Button(text="Save", width=38,command= save_password)
save_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()