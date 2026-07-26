import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My window")

my_frame = ttk.Frame()
my_frame.pack(side='left',fill='both',expand=True)

label1 = tk.Label(my_frame,text="My label1",bg="red")
label1.pack(side="left",fill='both',expand=True)

label2 = tk.Label(text="My label2",bg="blue")
label2.pack(side="right",expand=True,fill='both')

label3 = tk.Label(text="My label3")
label3.pack(expand=True,fill='both')

window.mainloop()