import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from components.VerticalScrolledFrame import VerticalScrolledFrame
from components.AddWindow import AddWindow
from components.EditWindow import EditWindow
from components.InfoWindow import InfoWindow
from components.ViewWindow import ViewWindow
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

class MainWindow():
    def __init__(self, handler: CsvHandler) -> None:
        self.handler = handler
        self.data = self.handler.read()
        self.__window = tk.Tk()
        
        self.__window.title("Contacts")
        self.__window.geometry('600x400')

        self.__window.rowconfigure(0, weight=1)
        self.__window.rowconfigure(1, weight=3)
        self.__window.rowconfigure(2, weight=1)

        self.search = tk.StringVar()

        # Header
        header_frame = tk.Frame(self.__window, bg=BACKGROUND_COLOR, pady=5)
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(header_frame, text="Contacts", font=FONT_LG, bg=BACKGROUND_COLOR)
        header_label.pack(side=tk.LEFT, padx=10)
        
        add_button = ttk.Button(header_frame, text="➕", width=3, command=self.open_add_window)
        add_button.pack(side=tk.RIGHT, padx=2)

        search_button = ttk.Button(header_frame, text="🔍", width=3, command=self.redraw_contacts)
        search_button.pack(side=tk.RIGHT)

        search_entry = ttk.Entry(header_frame, width=30, font=FONT_SM, textvariable=self.search)
        search_entry.pack(side=tk.RIGHT, padx=2)

        info_button = ttk.Button(header_frame, text="ⓘ", width=3, command=self.open_info_window)
        info_button.pack(side=tk.RIGHT, padx=2)

        # Content
        self.frame = VerticalScrolledFrame(self.__window)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Footer
        footer_frame = tk.Frame(self.__window, bg=BACKGROUND_COLOR, pady=5)
        footer_frame.pack(fill=tk.X)
        
        footer_label = tk.Label(footer_frame, text="© 2024 Contacts App", font=FONT_SM, bg=BACKGROUND_COLOR)
        footer_label.pack()

        self.redraw_contacts()

        return

    def mainloop(self) -> None:
        self.__window.mainloop()
        return

    def open_add_window(self) -> None:
        add_window = AddWindow(self.handler, self.data)
        add_window.wait_closed()
        self.redraw_contacts()
        return
    
    def open_info_window(self) -> None:
        info_window = InfoWindow()
        return
    
    def open_view_window(self, index, name, address, email, numbers) -> None:
        info_window = ViewWindow(index, name, address, email, numbers)
        return
    
    def open_edit_window(self, index, name, address, email, numbers) -> None:
        edit_window = EditWindow(self.handler, self.data, index, name, address, email, numbers)
        edit_window.wait_closed()
        self.redraw_contacts()
        return

    def add_panel(self, index, name, address, email, numbers) -> None:
        frame = tk.Frame(self.frame.interior, height=40)
        frame.pack(fill="x", pady=3, padx=2)

        frame.bind("<Button-1>", lambda x: self.open_view_window(index, name, address, email, numbers))

        delete_button = ttk.Button(frame, text="🗑", width=3, command=lambda: self.remove_record(frame, index))
        delete_button.pack(side=tk.RIGHT)

        edit_button = ttk.Button(frame, text="✎", width=3, command=lambda: self.open_edit_window(index, name, address, email, numbers))
        edit_button.pack(side=tk.RIGHT)

        label = ttk.Label(frame, text=f"{name} ({email})", font=FONT_MD)
        label.pack(side=tk.LEFT)

        label.bind("<Button-1>", lambda x: self.open_view_window(index, name, address, email, numbers))
        return

    def remove_record(self, frame: tk.Frame, index) -> None:
        frame.destroy()
        self.data.drop(index, inplace=True)
        self.handler.write(self.data)
        return
    
    def search_dataframe(self, df: pd.DataFrame, query: str) -> pd.DataFrame:
        results = []
        for index, row in df.iterrows():
            if query.lower() in row['name'].lower():
                results.append(row)
            else:
                for phone in row['numbers']:
                    if query in phone:
                        results.append(row)
                        break
        return pd.DataFrame(results)
    
    def redraw_contacts(self) -> None:
        for widget in self.frame.interior.winfo_children():
            widget.destroy()

        data = self.data
        search = self.search.get()

        if len(search) > 0:
            data = self.search_dataframe(data, search)

        for index, row in data.sort_values(by="name").iterrows():
            self.add_panel(index, row["name"], row["address"], row["email"], row["numbers"])

        return
