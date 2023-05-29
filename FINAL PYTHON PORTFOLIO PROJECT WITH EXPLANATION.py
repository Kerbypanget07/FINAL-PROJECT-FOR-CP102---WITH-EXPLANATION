#These lines import the necessary modules and libraries for creating a graphical user interface (GUI),
# performing message box operations, and handling time, regular expressions, and hashing.

import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Label, Button, Entry
import time
import re
import hashlib

#This code defines a class called KcashApp that represents the main application window.
#The __init__ method initializes the application by setting up the window title, background color,
#and size. It also initializes the balance to 0 and creates a label (self.bl) to display the current balance.

class KcashApp:
    def __init__(self, master):
        self.master = master
        master.title("KCash")
        master.configure(bg="#FFE1E6")
        master.geometry("800x500")

        self.balance = 0.0

        self.bl = Label(master, text="Balance: PHP {:.2f}".format(self.balance), bg="#FFE1E6", fg="#FF4081")
        self.bl.pack()

        self.d_label = Label(master, text="Deposit Amount:", bg="#FFE1E6", fg="#FF4081")
        self.d_label.pack()

        self.d_entry = Entry(master)
        self.d_entry.pack()

        self.d_button = Button(master, text="Deposit", command=self.deposit, bg="#FF4081", fg="white")
        self.d_button.pack()

        self.w_label = Label(master, text="Withdraw Amount:", bg="#FFE1E6", fg="#FF4081")
        self.w_label.pack()

        self.w_entry = Entry(master)
        self.w_entry.pack()

        self.w_button = Button(master, text="Withdraw", command=self.withdraw, bg="#FF4081", fg="white")
        self.w_button.pack()

        self.t_label = Label(master, text="Transfer Amount:", bg="#FFE1E6", fg="#FF4081")
        self.t_label.pack()

        self.t_entry = Entry(master)
        self.t_entry.pack()

        self.t_button = Button(master, text="Transfer", command=self.transfer, bg="#FF4081", fg="white")
        self.t_button.pack()

        self.q_button = Button(master, text="Quit", command=self.quit_program, bg="#FF4081", fg="white")
        self.q_button.pack()

    def deposit(self):
        amount = float(self.d_entry.get())
        self.balance += amount
        self.update_balance()
        messagebox.showinfo("Deposit", "Successfully deposited PHP {:.2f}".format(amount))
        self.d_entry.delete(0, 'end')

    def withdraw(self):
        amount = float(self.w_entry.get())
        if self.balance >= amount:
            self.balance -= amount
            self.update_balance()
            messagebox.showinfo("Withdraw", "Successfully withdrew PHP {:.2f}".format(amount))
        else:
            messagebox.showerror("Withdraw", "Insufficient balance")
        self.w_entry.delete(0, 'end')

    def transfer(self):
        amount = float(self.t_entry.get())
        if self.balance >= amount:
            self.balance -= amount
            self.update_balance()
            messagebox.showinfo("Transfer", "Successfully transferred PHP {:.2f}".format(amount))
        else:
            messagebox.showerror("Transfer", "Insufficient balance")
        self.t_entry.delete(0, 'end')

# These methods are responsible for handling the deposit, withdrawal, and transfer operations in the application.
# They retrieve the amount entered by the user, update the balance accordingly,
# display a message box with the transaction details, and clear the input field.

    def update_balance(self):
        self.bl.config(text="Balance: PHP {:.2f}".format(self.balance))

    def quit_program(self):
        self.master.destroy()


def show_kcash_app():
    root = Tk()
    app = KcashApp(root)
    root.mainloop()


def loading():
    c = "Now Loading Your Program"
    loading_label.config(text=c)
    loading_label.update()
    for a in "...":
        time.sleep(0.5)
        loading_label.config(text=loading_label.cget("text") + a)
        loading_label.update()


def program(answer):
    if answer == "Y" or answer == "y":
        root.deiconify()  # Show the main window
        loading_label.destroy()  # Destroy the loading label
    elif answer == "N" or answer == "n":
        messagebox.showinfo("Exit", "Goodbye.")
        root.destroy()  # Close the application
    else:
        messagebox.showerror("Error", "Please input Y or N only.")


def loading3():
    loading_label.config(text="")
    c = "GREETINGS, COME IN"
    loading_label.config(text=c)
    loading_label.update()

    for a in "...":
        time.sleep(0.5)
        loading_label.config(text=loading_label.cget("text") + a)
        loading_label.update()


users = {}


def signup():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_password
        messagebox.showinfo("Sign Up", "Sign up successful!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter username and password.")


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in users and users[username] == hashed_password:
            messagebox.showinfo("Login", "Login successful!")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            root.withdraw()  # Hide the login window
            show_kcash_app()
        else:
            messagebox.showerror("Login", "Invalid username or password.")
    else:
        messagebox.showerror("Error", "Please enter username and password.")


def handle_choice():
    choice = choice_var.get()
    if choice == 1:
        loading3()
        time.sleep(1)
        messagebox.showinfo("Choice", "Sign up")
        signup()
    elif choice == 2:
        loading3()
        time.sleep(1)
        messagebox.showinfo("Choice", "Login")
        login()
    elif choice == 3:
        program("N")  # Exit the program


root = tk.Tk()
root.geometry("800x500")
root.title("KCash")
root.configure(bg="#FFE1E6")  # Set the background color to light pink

loading_label = tk.Label(root, text="Now Loading", font=("Arial", 12), bg="#FFE1E6", fg="#FF4081")
loading_label.pack(pady=10)

choice_var = tk.IntVar()
choice_label = tk.Label(root, text="Choose an option:", bg="#FFE1E6", fg="#FF4081")
choice_label.pack(pady=10)
signup_radio = tk.Radiobutton(root, text="Sign up", variable=choice_var, value=1, bg="#FFE1E6", fg="#FF4081")
signup_radio.pack()
login_radio = tk.Radiobutton(root, text="Login", variable=choice_var, value=2, bg="#FFE1E6", fg="#FF4081")
login_radio.pack()
exit_radio = tk.Radiobutton(root, text="Exit", variable=choice_var, value=3, bg="#FFE1E6", fg="#FF4081")
exit_radio.pack()

choice_button = tk.Button(root, text="Submit", command=handle_choice, bg="#FF4081", fg="white")
choice_button.pack(pady=10)

username_label = tk.Label(root, text="Enter your username:", bg="#FFE1E6", fg="#FF4081")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Enter your password:", bg="#FFE1E6", fg="#FF4081")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login, bg="#FF4081", fg="white")
login_button.pack(pady=10)

root.mainloop()

# Add tkdesigner to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
try:
    from tkdesigner.designer import Designer
except ModuleNotFoundError:
    raise RuntimeError("Couldn't add tkdesigner to the PATH.")


# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

# Required in order to add data files to Windows executable
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

output_path = ""


def btn_clicked():
    token = token_entry.get()
    URL = URL_entry.get()
    output_path = path_entry.get()
    output_path = output_path.strip()

    if not token:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Token.")
        return
    if not URL:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter URL.")
        return
    if not output_path:
        tk.messagebox.showerror(
            title="Invalid Path!", message="Enter a valid output path.")
        return

    match = re.search(
        r'https://www.figma.com/file/([0-9A-Za-z]+)', URL.strip())
    if match is None:
        tk.messagebox.showerror(
            "Invalid URL!", "Please enter a valid file URL.")
        return

    file_key = match.group(1).strip()
    token = token.strip()
    output = Path(output_path + "/build").expanduser().resolve()

    if output.exists() and not output.is_dir():
        tk1.showerror(
            "Exists!",
            f"{output} already exists and is not a directory.\n"
            "Enter a valid output directory.")
    elif output.exists() and output.is_dir() and tuple(output.glob('*')):
        response = tk1.askyesno(
            "Continue?",
            f"Directory {output} is not empty.\n"
            "Do you want to continue and overwrite?")
        if not response:
            return

    designer = Designer(token, file_key, output)
    designer.design()

    tk.messagebox.showinfo(
        "Success!", f"Project successfully generated at {output}.")


def select_path():
    global output_path

    output_path = tk.filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)


def know_more_clicked(event):
    instructions = (
        "https://github.com/ParthJadhav/Tkinter-Designer/"
        "blob/master/docs/instructions.md")
    webbrowser.open_new_tab(instructions)


def make_label(master, x, y, h, w, *args, **kwargs):
    f = tk.Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)

    label = tk.Label(f, *args, **kwargs)
    label.pack(fill=tk.BOTH, expand=1)

    return label


window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Tkinter Designer")

window.geometry("862x519")
window.configure(bg="#3A7FF6")
canvas = tk.Canvas(
    window, bg="#3A7FF6", height=519, width=862,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")

text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
token_entry_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
URL_entry_img = canvas.create_image(650.5, 248.5, image=text_box_bg)
filePath_entry_img = canvas.create_image(650.5, 329.5, image=text_box_bg)

token_entry = tk.Entry(bd=0, bg="#F6F7F9",fg="#000716",  highlightthickness=0)
token_entry.place(x=490.0, y=137+25, width=321.0, height=35)
token_entry.focus()

URL_entry = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716",  highlightthickness=0)
URL_entry.place(x=490.0, y=218+25, width=321.0, height=35)

path_entry = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0)
path_entry.place(x=490.0, y=299+25, width=321.0, height=35)

path_picker_img = tk.PhotoImage(file = ASSETS_PATH / "path_picker.png")
path_picker_button = tk.Button(
    image = path_picker_img,
    text = '',
    compound = 'center',
    fg = 'white',
    borderwidth = 0,
    highlightthickness = 0,
    command = select_path,
    relief = 'flat')

path_picker_button.place(
    x = 783, y = 319,
    width = 24,
    height = 22)

canvas.create_text(
    490.0, 156.0, text="Token ID", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")
canvas.create_text(
    490.0, 234.5, text="File URL", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")
canvas.create_text(
    490.0, 315.5, text="Output Path",
    fill="#515486", font=("Arial-BoldMT", int(13.0)), anchor="w")
canvas.create_text(
    646.5, 428.5, text="Generate",
    fill="#FFFFFF", font=("Arial-BoldMT", int(13.0)))
canvas.create_text(
    573.5, 88.0, text="Enter the details.",
    fill="#515486", font=("Arial-BoldMT", int(22.0)))

title = tk.Label(
    text="Welcome to Tkinter Designer", bg="#3A7FF6",
    fg="white",justify="left", font=("Arial-BoldMT", int(20.0)))
title.place(x=20.0, y=120.0)
canvas.create_rectangle(25, 160, 33 + 60, 160 + 5, fill="#FCFCFC", outline="")

info_text = tk.Label(
    text="Tkinter Designer uses the Figma API\n"
    "to analyse a design file, then creates\n"
    "the respective code and files needed\n"
    "for your GUI.\n\n"

    "Even this GUI was created\n"
    "using Tkinter Designer.",
    bg="#3A7FF6", fg="white", justify="left",
    font=("Georgia", int(16.0)))

info_text.place(x=20.0, y=200.0)

know_more = tk.Label(
    text="Click here for instructions",
    bg="#3A7FF6", fg="white",justify="left", cursor="hand2")
know_more.place(x=20, y=400)
know_more.bind('<Button-1>', know_more_clicked)

generate_btn_img = tk.PhotoImage(file=ASSETS_PATH / "generate.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=0, highlightthickness=0,
    command=btn_clicked, relief="flat")
generate_btn.place(x=557, y=401, width=180, height=55)

window.resizable(False, False)
window.mainloop()
