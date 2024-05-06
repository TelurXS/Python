import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from components.MainWindow import MainWindow
from handlers.CsvHandler import CsvHandler

if __name__ == "__main__":
    handler = CsvHandler("contacts.csv")
    app = MainWindow(handler)
    app.mainloop()
