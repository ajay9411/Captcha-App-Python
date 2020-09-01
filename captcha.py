import random 
from tkinter import *
from tkinter import messagebox

text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
window = Tk()
window.title("Captcha App")
window.geometry("280x100") 
captcha = StringVar()
user_input = StringVar()


def set_captcha():
    s = random.choices(text, k = 6) 
    captcha.set(''.join(s))

def check():
    if captcha.get() == user_input.get(): 
        messagebox.showinfo("Success", "Correct")
    else:
        messagebox.showerror("Error", "Incorrect") 
    set_captcha()

Label(window,textvariable = captcha, font = "Arial 16 ").pack() 

Entry(window, textvariable = user_input,font = "Arial 10 ").pack(ipady = 5)

Button(window, command = check, text = "Check",font = "Arial 10").pack()

set_captcha() 
window.mainloop()