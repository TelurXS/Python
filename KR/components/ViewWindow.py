import tkinter as tk
import tkinter.ttk as ttk
import re
import tkinter.messagebox as messagebox
from components.VerticalScrolledFrame import VerticalScrolledFrame
from handlers.CsvHandler import CsvHandler
import pandas as pd

BACKGROUND_COLOR = "gray92"
FONT_FAMILY = "Helvetica"
FONT_SIZE_LG = 14
FONT_SIZE_MD = 12
FONT_SIZE_SM = 10

FONT_LG = (FONT_FAMILY, FONT_SIZE_LG)
FONT_MD = (FONT_FAMILY, FONT_SIZE_MD)
FONT_SM = (FONT_FAMILY, FONT_SIZE_SM)

class ViewWindow():
    def __init__(self, index, name, address, email, numbers) -> None:
        self.__window = tk.Toplevel()
        self.__window.title("View Record")
        self.__window.geometry('300x430')
        self.__window.grab_set()
        self.__window.resizable(False, False)

        self.__window.columnconfigure(0, minsize=70)
        self.__window.columnconfigure(1, minsize=210)

        self.__number_pattern = re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")

        self.index = index
        self.name = tk.StringVar(self.__window, name)
        self.address = tk.StringVar(self.__window, address)
        self.email = tk.StringVar(self.__window, email)
        self.number = tk.StringVar(self.__window)
        self.numbers: list[str] = numbers

        header_label = tk.Label(self.__window, text="Contact", font=FONT_LG)
        header_label.grid(row=0, column=0, columnspan=2)

        name_label = tk.Label(self.__window, text="Name:", font=FONT_MD, anchor=tk.W)
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        name_entry = tk.Entry(self.__window, font=FONT_MD, textvariable=self.name, state="readonly")
        name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        address_label = tk.Label(self.__window, text="Address:", font=FONT_MD, anchor=tk.W)
        address_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        address_entry = tk.Entry(self.__window, font=FONT_MD, textvariable=self.address, state="readonly")
        address_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        email_label = tk.Label(self.__window, text="Email:", font=FONT_MD, anchor=tk.W)
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        email_entry = tk.Entry(self.__window, font=FONT_MD, textvariable=self.email, state="readonly")
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        phone_number_frame = tk.Frame(self.__window)
        phone_number_frame.grid(row=4, column=0, columnspan=2)

        phone_list_frame = tk.Frame(self.__window, bg="red")
        phone_list_frame.grid(row=5, column=0, columnspan=2, padx=5, sticky=tk.EW)

        self.__phones_frame = VerticalScrolledFrame(phone_list_frame)
        self.__phones_frame.pack(fill=tk.BOTH)

        save_button = ttk.Button(self.__window, text="Save", command=self.save) 
        save_button.grid(row=6, column=0, columnspan=2)

        for number in numbers:
            self.add_panel(number)

        return

    def wait_closed(self) -> None:
        self.__window.wait_window()
        return
    
    def add_number(self) -> None:
        number = self.number.get()

        if not self.__number_pattern.fullmatch(number):
            messagebox.showerror("Wrong phone", "Entered phone number was not in correct format")
            return
        
        self.numbers.append(number)
        self.add_panel(number)
        return
    
    def add_panel(self, number: str) -> None:
        frame = tk.Frame(self.__phones_frame.interior, height=40)
        frame.pack(fill=tk.X, pady=3, padx=2)

        label = ttk.Label(frame, text=number, font=FONT_MD)
        label.pack(side=tk.LEFT)
        return
    
    def remove_number(self, number: str, panel: tk.Frame) -> None:
        panel.destroy()
        self.numbers.remove(number)
        return
    
    def save(self) -> None:
        self.data.loc[self.index] = {
            "name": self.name.get(),
            "address": self.address.get(),
            "email": self.email.get(),
            "numbers": self.numbers
        }
        self.handler.write(self.data)
        self.__window.destroy()
        return