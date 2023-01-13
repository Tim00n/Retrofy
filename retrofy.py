import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

root = tk.Tk()
root.config(bg='grey')
root.title("Retrofy")
welcome_label = tk.Label(font=("Roboto", 20))
welcome_label.pack()

# Set the icon of the main window
root.iconbitmap("Retrofy.ico")

# Create a PhotoImage object for the new image
image = PhotoImage(file="Retrofy.png")

# Create a Label widget to display the image
image_label = tk.Label(root, image=image)
image_label.pack()
image_label.config(bg='grey')


def check_credentials():
    # Get the values of the username and password fields
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password match
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Welcome!")
    else:
        messagebox.showerror("Login", "Invalid username or password")


# Create a Frame widget for the login form
form_frame = tk.Frame(root, bd=5, relief='sunken', bg='#D3D3D3')
form_frame.place(relx=0.5, rely=0.5, y=150, anchor='center', width=300, height=150)

# Create a Label widget for the "Username" label
username_label = tk.Label(form_frame, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)

# Create an Entry widget for the username field
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a Label widget for the "Password" label
password_label = tk.Label(form_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

# Create an Entry widget for the password field
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a Button widget to submit the login form
login_button = tk.Button(form_frame, text="Login", command=check_credentials, activebackground='#87CEFA')
login_button.grid(row=2)

root.mainloop()