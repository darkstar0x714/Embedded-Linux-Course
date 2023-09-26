#!/usr/bin/python3
"""
   Author        :     Amir W. Fathy
   Date          :     24 sep 2023
   Description   :     simple GUI for changing the color of element on the GUI
"""
import customtkinter
import tkinter as tk


def ledOnBtn():
    canvas.itemconfigure(fill="blue", tagOrId="ci")
    label_1.configure(text="led is on")


def ledOffBtn():
    canvas.itemconfigure(fill="grey", tagOrId="ci")
    label_1.configure(text="led is off")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.geometry("300x300")

app.title("simple LED controller")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


canvas = customtkinter.CTkCanvas(
    frame_1, width=50, height=50)

led = canvas.create_aa_circle(tags="ci", x_pos=25, y_pos=25, radius=20,
                              fill='grey')
canvas.pack(anchor=tk.CENTER, expand=True)

label_1 = customtkinter.CTkLabel(
    master=frame_1, justify=customtkinter.LEFT, text="led is off")

button_1 = customtkinter.CTkButton(
    master=frame_1, command=ledOnBtn, text="led on")

button_2 = customtkinter.CTkButton(
    master=frame_1, command=ledOffBtn, text="led off")\


label_1.pack(pady=10, padx=10)

button_1.pack(pady=10, padx=10)
button_2.pack(pady=10, padx=10)


app.mainloop()
