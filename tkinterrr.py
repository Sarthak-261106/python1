import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
window = tk.Tk()
window.title("my window")
window.minsize(400,300)
custom_font=tkFont.Font(family="Times New Roman",size=20,weight="bold")

label = ttk.Label(text="my label",font=custom_font)
label.pack()
#label.config(font=("Courier New",25,"underline"))

# counter=0
def funtion_button():
    # global counter
    # counter+=1
    input_text=user_input.get()
    label.config(text=input_text)
button = ttk.Button(text="click me",command=funtion_button)
button.pack()

user_input=ttk.Entry(width=20,font=custom_font)
user_input.pack()

window.mainloop()

