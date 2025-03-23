
import pyperclip 
import json
from tkinter import *
from tkinter import messagebox # Since this is not a class, we need to be import that module seperately
from random import choice, randint, shuffle

def main():
    # Function to generate a random password
    def generate_password():
        # Define character sets
        letters = [
            'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        ]
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # Randomly select characters from each set
        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_list = password_letters + password_symbols + password_numbers

        shuffle(password_list) # Shuffle the password characters

        password = ''.join(password_list)
        password_entry.delete(0, END) # Clear previous password before inserting new one
        password_entry.insert(0, password) # Insert new password into entry field
        pyperclip.copy(password) # Copy password to clipboard

    # Function to save password details
    def save_password():

        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        # Ensure no fields are left empty
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Missing info", message="Please fill out all of the fields.")
        
        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file) # Read old data

            except FileNotFoundError: # If there is no data.json file, we create one
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data) # Update old data with new data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4) # Save updated data
                    
            finally:  
                website_entry.delete(0, END) # Clear website entry after saving
                password_entry.delete(0, END)  # Clear password entry after saving

    # Function to search for saved password
    def search_password():
        website = website_entry.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Credentials not found!")

        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="Credentials not found!")

    # UI setup
    window = Tk()
    window.title("Password Manager")
    window.config(padx= 40, pady= 40) # Add padding to the window

    # Canvas for displaying the logo
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

    # Entry fields
    website_entry = Entry(width=25)
    website_entry.grid(column=1 , row=1, sticky='w')
    website_entry.focus() # Focus on website entry when program starts

    email_entry = Entry(width=45)
    email_entry.grid(column=1 ,row=2, columnspan=2)
    email_entry.insert(END, "myemail@gmail.com") # Pre-fill with default email (you can change that with your email)

    password_entry = Entry(width=25)
    password_entry.grid(column=1, row=3, sticky='w')

    #Buttons
    generate_password_btn = Button(text="Generate Password", command=generate_password)
    generate_password_btn.grid(column=2, row=3, sticky='e')

    save_btn = Button(text="Save", width=38,command= save_password)
    save_btn.grid(column=1, row=4, columnspan=2)

    search_btn = Button(text="Search", width=14, command=search_password)
    search_btn.grid(column=2, row=1, sticky="e")

    window.mainloop() # Run the Tkinter main event loop

if __name__ == "__main__":
    main() # Start the app