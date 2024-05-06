import tkinter as tk
import tkinter.ttk as ttk

FONT_FAMILY = "Helvetica"
FONT_SIZE_LG = 14
FONT_SIZE_MD = 12
FONT_SIZE_SM = 10

FONT_LG = (FONT_FAMILY, FONT_SIZE_LG)
FONT_MD = (FONT_FAMILY, FONT_SIZE_MD)
FONT_SM = (FONT_FAMILY, FONT_SIZE_SM)

class InfoWindow():
    def __init__(self) -> None:
        self.__window = tk.Toplevel()
        self.__window.title("Info")
        self.__window.geometry('600x640')
        self.__window.grab_set()
        self.__window.resizable(False, False)

        tk.Label(self.__window, text="""Program Name: Contact Saver""", justify=tk.LEFT, font=FONT_LG).pack(fill=tk.X, pady=5)
        tk.Label(self.__window, text="""The Contact Saver program is a simple application designed to help users manage their contacts efficiently. It allows users to store contact information such as names, phone numbers, emails, and addresses in a structured manner.""", justify=tk.LEFT, font=FONT_MD, wraplength=600).pack(fill=tk.X, pady=5)
        tk.Label(self.__window, text="""Key Features:
Add Contact: Users can easily add new contacts by providing necessary details like name, phone number, email, and address.
View Contacts: Users can view a list of all saved contacts along with their details.
Search Contacts: The program enables users to search for specific contacts by name, phone number, or email, making it easy to find desired contacts quickly.
Edit Contacts: Users can edit existing contact information if there are any changes or updates.
Delete Contacts: Contacts that are no longer needed can be removed from the list.
Save and Load: Contacts are saved automatically to a file/database for future access. Users can also load previously saved contacts when the program starts.""", justify=tk.LEFT, font=FONT_MD, wraplength=600).pack(fill=tk.X, pady=5)
        tk.Label(self.__window, text="""The program provides a simple and intuitive user interface with the following elements:
Menu Bar: Contains options for adding, viewing, searching, editing, and deleting contacts.
Contact List: Displays a list of saved contacts with options to view details, edit, or delete.
Add/Edit Contact Form: Allows users to input or modify contact details.
Search Bar: Enables users to search for specific contacts by name, phone number, or email.""", justify=tk.LEFT, font=FONT_MD, wraplength=600).pack(fill=tk.X, pady=5)
        tk.Label(self.__window, text="""How to Use:
Launch the Contact Saver program.
Use the menu options to add, view, search, edit, or delete contacts.
To add a new contact, select the "Add Contact" option and fill in the required information.
To view or search for existing contacts, use the respective options from the menu.
To edit or delete a contact, select it from the contact list and choose the appropriate option from the menu.""", justify=tk.LEFT, font=FONT_MD, wraplength=600).pack(fill=tk.X, pady=5)

        return