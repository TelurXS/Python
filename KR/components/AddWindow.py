import tkinter as tk
import re
import tkinter.ttk as ttk
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

class AddWindow():
    def __init__(self, handler: CsvHandler, data: pd.DataFrame) -> None:
        self.handler = handler
        self.data = data
        self.__window = tk.Toplevel()
        self.__window.title("Add Record")
        self.__window.geometry('300x460')
        self.__window.grab_set()
        self.__window.resizable(True, False)

        self.__window.grid_columnconfigure(0, weight=1, minsize=80)
        self.__window.grid_columnconfigure(1, weight=2)

        self.__number_pattern = re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")

        self.name = tk.StringVar()
        self.address = tk.StringVar()
        self.email = tk.StringVar()
        self.number = tk.StringVar()
        self.numbers: list[str] = []

        header_label = tk.Label(self.__window, text="Contact", font=FONT_LG)
        header_label.grid(row=0, column=0, columnspan=2)

        name_label = tk.Label(self.__window, text="Name:", font=FONT_MD, anchor=tk.W)
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        name_entry = tk.Entry(self.__window, font=FONT_MD, textvariable=self.name)
        name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        address_label = tk.Label(self.__window, text="Address:", font=FONT_MD, anchor=tk.W)
        address_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        address_entry = tk.Entry(self.__window, font=FONT_MD, textvariable=self.address)
        address_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        email_label = tk.Label(self.__window, text="Email:", font=FONT_MD, anchor=tk.W)
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        email_entry = tk.Entry(self.__window, font=FONT_MD, textvariable=self.email)
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        phone_number_frame = tk.Frame(self.__window)
        phone_number_frame.grid(row=4, column=0, columnspan=2)

        phone_entry = tk.Entry(phone_number_frame, font=FONT_MD, textvariable=self.number)
        phone_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        add_phone_button = ttk.Button(phone_number_frame, text="➕", width=3, command=self.add_number) 
        add_phone_button.pack(side=tk.LEFT, padx=5, pady=5)

        phone_list_frame = tk.Frame(self.__window, bg="red")
        phone_list_frame.grid(row=5, column=0, columnspan=2, padx=5, sticky=tk.EW)

        self.__phones_frame = VerticalScrolledFrame(phone_list_frame)
        self.__phones_frame.pack(fill=tk.BOTH)

        save_button = ttk.Button(self.__window, text="Save", command=self.save) 
        save_button.grid(row=6, column=0, columnspan=2)

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

        delete_button = ttk.Button(frame, text="🗑", width=3, command=lambda: self.remove_number(number, frame))
        delete_button.pack(side=tk.RIGHT)

        label = ttk.Label(frame, text=number, font=FONT_MD)
        label.pack(side=tk.LEFT)
        return
    
    def remove_number(self, number: str, panel: tk.Frame) -> None:
        panel.destroy()
        self.numbers.remove(number)
        return
    
    def save(self) -> None:
        self.data.loc[len(self.data)] = {
            "name": self.name.get(),
            "address": self.address.get(),
            "email": self.email.get(),
            "numbers": self.numbers
        }
        self.handler.write(self.data)
        self.__window.destroy()
        return