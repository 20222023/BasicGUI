import tkinter as tk
from tkinter import messagebox, Label, Entry, Canvas
import random
import string

# Create a new window
root = tk.Tk()
root.title("Modern UI")
root.geometry("600x400")

# Create a frame for left half
left_frame = tk.Frame(root, bg='red')
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

# Create a label for "Project X"
project_label = tk.Label(left_frame, text="Project X", font=('Arial', 20, 'bold'), fg='black', bg = 'red')
project_label.place(relx=0.5, rely=0.5, anchor='center')

# Create a frame for right half
right_frame = tk.Frame(root)
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

# Create a label for Authentication text
authentication_label = tk.Label(right_frame, text = "Authentication", font = ('Arial', 20, 'bold'))
authentication_label.place(relx=0.5, rely=0.1, anchor='center')

# Create a label for username
username_label = tk.Label(right_frame, text = "Username:")
username_label.place(relx=0.2, rely=0.2)

# Create a Entry box for username
username_entry = Entry(right_frame)
username_entry.place(relx=0.4, rely=0.2)

# Create a label for Password
password_label = tk.Label(right_frame, text = "Password:")
password_label.place(relx=0.2, rely=0.3)

# Create a Entry box for password
password_entry = Entry(right_frame)
password_entry.place(relx=0.4, rely=0.3)

# Create a button
def check_text():
    text_username = username_entry.get()
    text_password = password_entry.get()
    if text_username != "Person" or text_password != password:
        messagebox.showerror("Error", "Incorrect username or password")
    else:
        new_root = tk.Tk()
        new_root.geometry("600x400")
        new_root.configure(bg = 'sky blue')
        canvas = Canvas(new_root, bg='gray',highlightthickness=0)
        canvas.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)
        welcome_label = tk.Label(new_root, text = f"Welcome {text_username} \U0001F600", font = ('Arial', 20, 'bold'), bg = 'sky blue')
        welcome_label.place(relx=0.5, rely=0.1, anchor='center')
        back_button = tk.Button(new_root, text="Back", command=new_root.destroy)
        back_button.place(relx=0.01, rely=0.01, anchor='nw')
        new_root.mainloop()

password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
print(password)
button = tk.Button(right_frame, text="Login", command=check_text)
button.place(relx=0.4, rely=0.4)

root.mainloop()
