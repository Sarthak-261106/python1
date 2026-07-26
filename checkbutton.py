import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
window = tk.Tk()
window.title("my window")
window.minsize(400,300)
custom_font=tkFont.Font(family="Times New Roman",size=20,weight="bold")

label = tk.Label(text="my label",font=custom_font)
label.pack()

def funtion_button():
    input_text=user_input.get()
    label.config(text=input_text)
button = tk.Button(text="click me",command=funtion_button)
button.pack()

user_input=tk.Entry(width=20,font=custom_font)
user_input.pack()

quit_button=ttk.Button(text="Quit",command=window.destroy)
quit_button.pack(pady=25)

sep=ttk.Separator(orient='horizontal')
sep.pack(fill='x')



text=tk.Text(height=5,width=20,font=custom_font)
text.pack(pady=10)
text.focus()
text.insert('1.0','enter your text here')

text_data=text.get('1.0','end')
# print(text_data)

def get_text():
    # label2 = tk.Label(text=text.get('1.0', 'end'), font=custom_font)
    # label2.pack()
    print(text.get('1.0','end'))

# label2=tk.Label(text=text.get('1.0','end'),font=custom_font)
# label2.pack()


get_text_button=tk.Button(text="get text",command=get_text)
get_text_button.pack()
# text['state']='disabled'
#
# def enable_text():
#     text['state']='normal'
#
# enable_button=tk.Button(text="enable",command=enable_text)
# enable_button.pack()

check_option=tk.StringVar()

def check_option_task():
    print(check_option.get())

check_button=ttk.Checkbutton(text='terms and conditions',variable=check_option,command=check_option_task,onvalue='yes',offvalue='no')
check_button.pack()
check_button.pack()





window.mainloop()