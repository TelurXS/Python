from components.MainWindow import MainWindow
from handlers.CsvHandler import CsvHandler


def main() -> None:
    handler = CsvHandler("contacts.csv")
    app = MainWindow(handler)
    app.mainloop()
    return


if __name__ == "__main__":
    main()
