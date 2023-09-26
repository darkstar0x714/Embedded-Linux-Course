#!/usr/bin/python3
"""
   Author        :     Amir W. Fathy
   Date          :     24 sep 2023
   Description   :     simple GUI for calculator using custom tkinter
"""
import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.geometry("500x500")

app.title("simple calculator")


def button_callback():
    try:
        label_2.configure(
            text=eval(f"{entry_1.get()}{radiobutton_var.get()}{entry_2.get()}"))
    except (SyntaxError):
        label_2.configure(
            text="write some numbers first")
    except (NameError):
        label_2.configure(
            text="not valid numbers")
    except:
        label_2.configure(
            text="unknown error")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(
    master=frame_1, justify=customtkinter.LEFT, text="choose operation")

label_2 = customtkinter.CTkLabel(
    master=frame_1, justify=customtkinter.LEFT, text="make operation first")

entry_1 = customtkinter.CTkEntry(
    master=frame_1, placeholder_text="number 1")

entry_2 = customtkinter.CTkEntry(
    master=frame_1, placeholder_text="number 2",)


radiobutton_var = customtkinter.StringVar(value='')

radiobutton_1 = customtkinter.CTkRadioButton(
    master=frame_1, variable=radiobutton_var, value='+', text="+", command=button_callback)

radiobutton_2 = customtkinter.CTkRadioButton(
    master=frame_1, variable=radiobutton_var, value='-', text="-", command=button_callback)

radiobutton_3 = customtkinter.CTkRadioButton(
    master=frame_1, variable=radiobutton_var, value='*', text="*", command=button_callback)

radiobutton_4 = customtkinter.CTkRadioButton(
    master=frame_1, variable=radiobutton_var, value='/', text="/", command=button_callback)

label_1.pack(pady=10, padx=10)

entry_1.pack(pady=10, padx=10)
entry_2.pack(pady=10, padx=10)

radiobutton_1.pack(pady=10, padx=10)
radiobutton_2.pack(pady=10, padx=10)
radiobutton_3.pack(pady=10, padx=10)
radiobutton_4.pack(pady=10, padx=10)

label_2.pack(pady=10, padx=10)

app.mainloop()
