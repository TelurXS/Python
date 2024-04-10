def task1() -> None:
    name: str = input("Enter your name: ")
    print(f"Hello {name}!")
    return


def task2() -> None:
    name: str = input("What is your name? ")
    age: int = int(input("How old are you? "))
    address: str = input("Where do you live? ")

    print(f"This is {name}")
    print(f"It is {age}")
    print(f"(S)he lives in {address}")
    return


def task3() -> None:
    a, b = input("Input two values: ").split()
    print(f"a is {a}")
    print(f"b is {b}")
    return


def task4() -> None:
    a, b, c, d = input("Input four values (separate with ';'): ").split(";")
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print(f"d is {d}")
    return


def task5() -> None:
    age: int = int(input("What is your age? "))
    print(f"Your age after 50 years is {age + 50}")
    return


def task6() -> None:
    text: list[str] = input("Enter your birth date in format dd:MM:yyyy: ").split(":")
    day = int(text[0])
    month = int(text[1])
    year = int(text[2])

    print(f"Ви народилися: {day} числа {month} місяця {year} року!")
    return


def task7() -> None:
    a: int = int(input("Enter a value: "))
    operation: str = input("Enter operation: ")
    b: int = int(input("Enter b value: "))

    print(f"Result is {eval(f'{a}{operation}{b}')}")
    return


def task8() -> None:
    a: int = int(input("Enter a value: "))
    b: int = int(input("Enter b value: "))
    c: int = int(input("Enter c value: "))
    d: int = int(input("Enter d value: "))
    sum1: int = a + b
    sum2: int = c + d
    result: float = sum1 / sum2

    print(f"Result is {result:.2f}")
    return


def task9() -> None:
    q: float = 21
    w: float = 8

    print(f"Result is {q // w} with remainder {q % w}")
    return


def task10() -> None:
    n: int = 53
    result: int = 0

    for symbol in str(n):
        result += int(symbol)

    print(f"Summa is {result}")
    return


def task11() -> None:
    n: int = 168
    as_str: str = str(n)
    print(f"Last symbol is {as_str[len(as_str) - 1]}")
    return


def main() -> None:
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    task8()
    task9()
    task10()
    task11()
    return


if __name__ == '__main__':
    main()
