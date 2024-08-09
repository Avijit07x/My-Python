import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def button_click():
    print("button clicked")


def on_option_selected(value):
    lebel.config(text="Selected option: " + value)


# window
window = ttk.Window(themename='darkly')
window.title("My Project")
window.geometry("1080x720")
# window.maxsize(width=500, height=700)
# window.minsize(width=500, height=300)


# icon
window.iconbitmap("Tkinter Projects/Normal window/3.ico")
# logo= PhotoImage(file="c:\Users\deyav\Desktop\youtube_logo_icon_167938.png")
# logo_lebel= ttk.Label(window,image=logo)
# logo_lebel.pack

# title
title_label = ttk.Label(master=window,
                        text="Test App",
                        font="Lato 24 bold")
title_label.pack(side="top", pady=10)

# box
# text1 = ttk.Text(master=window)
# text1.pack(side="top")

# scrollbar
# scroll = ttk.Scrollbar(master=window , bootstyle="light-round")
# scroll.pack(side="right", ipady=1000)

# entry1
entry1 = ttk.Entry(master=window,)
entry1.pack(side="top")

# button
button_1 = ttk.Button(window, text="Click Me", command=button_click)
button_1.pack(side="top", pady=10)

# optionmenu
options = ["Chose Option", "Option 1 ", "Option 2", "Option 3", "Option 4"]
selected_option = ttk.StringVar()
selected_option.set(options[0])
lebel = ttk.Label(window, text="")
lebel.pack()
option_menu = ttk.OptionMenu(window,
                              selected_option, 
                              *options, 
                              command=on_option_selected)
option_menu.pack(pady=10)


# creator
crt = ttk.Label(window,
                text="Made By Avijit Dey", font="roboto 7", anchor="se")
crt.pack(side="bottom", fill="both")

# run
window.mainloop()
