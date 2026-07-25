import tkinter as tk
import tkinter.font as tkFont
window = tk.Tk()
window.title("my window")
window.minsize(400,300)
#custom_font=tkFont.Font(family="Times New Roman",size=20,weight="bold")

label = tk.Label(text="my label")

label.pack(expand=True)
label.config(font=("Courier New",25,"underline"))
window.mainloop()

