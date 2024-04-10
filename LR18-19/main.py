import tkinter as tk
import random


def task1() -> None:

    def show_name() -> None:
        name: str = entry.get()
        result_label.config(text=f"Your name is: {name}")
        return

    window = tk.Tk()
    window.title("Know Your Name")

    label = tk.Label(window, text="Enter your name:")
    label.pack(pady=5)

    entry = tk.Entry(window)
    entry.pack(pady=5)

    button = tk.Button(window, text="Show name", command=show_name)
    button.pack(pady=5)

    result_label = tk.Label(window, text="")
    result_label.pack(pady=5)

    window.mainloop()
    return


def task2() -> None:

    def show_result() -> None:
        try:
            number: int = int(entry.get())
            expression_range = range(1, number + 1)
            expression_text: str = ' + '.join([str(x) for x in expression_range])
            expression_result = sum(expression_range)

            result_label.config(text=f"{expression_text} = {expression_result}")

        except ValueError:
            result_label.config(text=f"Wrong number provided")

        return

    window = tk.Tk()
    window.title("Calculate number sum")

    label = tk.Label(window, text="Enter N:")
    label.grid(row=0, column=0)

    entry = tk.Entry(window)
    entry.grid(row=0, column=1)

    button = tk.Button(window, text="Calculate", command=show_result)
    button.grid(row=1, column=1)

    result_label = tk.Label(window, text="")
    result_label.grid(row=2, column=1)

    window.mainloop()
    return


def task3() -> None:

    def show_name() -> None:
        name: str = entry.get()
        result_label.config(text=f"Welcome {name}!")
        return

    window = tk.Tk()
    window.title("Welcome program")

    label = tk.Label(window, text="Enter your name:")
    label.grid(row=0, column=0)

    entry = tk.Entry(window)
    entry.grid(row=0, column=1)

    button = tk.Button(window, text="Show name", command=show_name)
    button.grid(row=1, column=1)

    result_label = tk.Label(window, text="")
    result_label.grid(row=2, column=1)

    window.mainloop()
    return


def task4() -> None:

    window = tk.Tk()

    menu = tk.Menu()

    file_menu = tk.Menu(menu)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Exit")
    menu.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    menu.add_cascade(label="Edit", menu=edit_menu)

    help_menu = tk.Menu(menu)
    help_menu.add_command(label="About Python")
    menu.add_cascade(label="Help", menu=help_menu)

    window.config(menu=menu)

    window.mainloop()
    return


count: int = 1


def task5() -> None:

    def remove() -> None:
        global count
        count -= 1
        label_number.config(text=str(count))
        return

    def add() -> None:
        global count
        count += 1
        label_number.config(text=str(count))
        return

    window = tk.Tk()

    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure(0, minsize=50, weight=1)
    window.columnconfigure(1, minsize=50, weight=1)
    window.columnconfigure(2, minsize=50, weight=1)

    global count

    button_remove = tk.Button(window, text="-", command=remove)
    button_remove.grid(row=0, column=0, sticky="nsew")

    label_number = tk.Label(window, text=str(count))
    label_number.grid(row=0, column=1)

    button_add = tk.Button(window, text="+", command=add)
    button_add.grid(row=0, column=2, sticky="nsew")

    window.mainloop()
    return


currencies = {
    "usd": 35,
    "euro": 42
}


def task6() -> None:

    def show_selected() -> None:
        selected = currencies.get(currency.get())

        if selected is None:
            return

        currency_value_label.config(text=str(selected))

        return

    def calculate() -> None:
        selected = currencies.get(currency.get())

        if selected is None:
            return

        try:
            value = int(entry.get())
            result_label.config(text=str(value * selected))

        except ValueError:
            result_label.config(text=f"Wrong number provided")

        return

    window = tk.Tk()

    select_currency_label = tk.Label(window, text="Select Currency")
    select_currency_label.grid(row=0, column=0)

    currency = tk.StringVar()
    currency.set("usd")

    checkbox_usd = tk.Radiobutton(window, variable=currency, text="USD", value="usd", command=show_selected)
    checkbox_usd.grid(row=0, column=1)

    checkbox_euro = tk.Radiobutton(window, variable=currency, text="EURO", value="euro", command=show_selected)
    checkbox_euro.grid(row=1, column=1)

    currency_value_text_label = tk.Label(window, text="Currency value:")
    currency_value_text_label.grid(row=2, column=0)

    currency_value_label = tk.Label(window, text="35")
    currency_value_label.grid(row=2, column=1)

    entry_label = tk.Label(window, text="Input value:")
    entry_label.grid(row=3, column=1)

    entry = tk.Entry(window)
    entry.grid(row=3, column=2)

    button_calculate = tk.Button(window, text="Calculate", command=calculate)
    button_calculate.grid(row=4, column=1)

    result_label = tk.Label(window)
    result_label.grid(row=4, column=2)

    window.mainloop()
    return


attempt: int = 1
number: int = random.randint(0, 100)


def task7() -> None:

    def submit() -> None:
        try:
            selected: int = int(entry.get())
            global attempt
            global number

            result_label.config(text=f"{number} number, {selected}")

            if selected == number:
                result_label.config(text=f"Congratulations: {attempt} attempts")
                return

            if selected < number:
                result_label.config(text=f"Bigger")

            if selected > number:
                result_label.config(text=f"Lower")

            attempt += 1

        except ValueError:
            result_label.config(text=f"Wrong number provided")

        return

    window = tk.Tk()
    window.title("Game")

    label = tk.Label(window, text="Enter Number: ")
    label.pack(pady=5)

    entry = tk.Entry(window)
    entry.pack(pady=5)

    button = tk.Button(window, text="Submit", command=submit)
    button.pack(pady=5)

    result_label = tk.Label(window, text="")
    result_label.pack(pady=5)

    window.mainloop()
    return

def task8() -> None:

    def add_to_expression(value: str) -> None:
        expression.set(expression.get() + value)
        return

    def calculate() -> None:
        expression.set(eval(expression.get()))
        return

    def clear_expression() -> None:
        expression.set("")
        return

    window = tk.Tk()

    window.rowconfigure(0, minsize=10, weight=1)
    window.rowconfigure(1, minsize=10, weight=1)
    window.rowconfigure(2, minsize=10, weight=1)
    window.rowconfigure(3, minsize=10, weight=1)
    window.rowconfigure(4, minsize=10, weight=1)
    window.rowconfigure(5, minsize=10, weight=1)
    window.columnconfigure(0, minsize=10, weight=1)
    window.columnconfigure(1, minsize=10, weight=1)
    window.columnconfigure(2, minsize=10, weight=1)
    window.columnconfigure(3, minsize=10, weight=1)

    expression = tk.StringVar()

    entry = tk.Entry(window, textvariable=expression)
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

    button_1 = tk.Button(window, text="1", command=lambda: add_to_expression("1"))
    button_1.grid(row=1, column=0, sticky="nsew")

    button_2 = tk.Button(window, text="2", command=lambda: add_to_expression("2"))
    button_2.grid(row=1, column=1, sticky="nsew")

    button_3 = tk.Button(window, text="3", command=lambda: add_to_expression("3"))
    button_3.grid(row=1, column=2, sticky="nsew")

    button_plus = tk.Button(window, text="+", command=lambda: add_to_expression("+"))
    button_plus.grid(row=1, column=3, sticky="nsew")

    button_4 = tk.Button(window, text="4", command=lambda: add_to_expression("4"))
    button_4.grid(row=2, column=0, sticky="nsew")

    button_5 = tk.Button(window, text="5", command=lambda: add_to_expression("5"))
    button_5.grid(row=2, column=1, sticky="nsew")

    button_4 = tk.Button(window, text="6", command=lambda: add_to_expression("6"))
    button_4.grid(row=2, column=2, sticky="nsew")

    button_minus = tk.Button(window, text="-", command=lambda: add_to_expression("-"))
    button_minus.grid(row=2, column=3, sticky="nsew")

    button_7 = tk.Button(window, text="7", command=lambda: add_to_expression("7"))
    button_7.grid(row=3, column=0, sticky="nsew")

    button_8 = tk.Button(window, text="8", command=lambda: add_to_expression("8"))
    button_8.grid(row=3, column=1, sticky="nsew")

    button_9 = tk.Button(window, text="9", command=lambda: add_to_expression("9"))
    button_9.grid(row=3, column=2, sticky="nsew")

    button_multiply = tk.Button(window, text="*", command=lambda: add_to_expression("*"))
    button_multiply.grid(row=3, column=3, sticky="nsew")

    button_0 = tk.Button(window, text="0", command=lambda: add_to_expression("0"))
    button_0.grid(row=4, column=0, sticky="nsew")

    button_ld = tk.Button(window, text="(", command=lambda: add_to_expression("("))
    button_ld.grid(row=4, column=1, sticky="nsew")

    button_rd = tk.Button(window, text=")", command=lambda: add_to_expression(")"))
    button_rd.grid(row=4, column=2, sticky="nsew")

    button_divide = tk.Button(window, text="/", command=lambda: add_to_expression("/"))
    button_divide.grid(row=4, column=3, sticky="nsew")

    button_calculate = tk.Button(window, text="=", command=calculate)
    button_calculate.grid(row=5, column=0, sticky="nsew", columnspan=2)

    button_clear = tk.Button(window, text="Clear", command=clear_expression)
    button_clear.grid(row=5, column=2, sticky="nsew", columnspan=2)

    window.mainloop()
    return


def main() -> None:
    task8()
    return


if __name__ == "__main__":
    main()
