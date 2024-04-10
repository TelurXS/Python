def task1() -> None:
    password: str = input("Input password: ")

    if password == "12345":
        print("You successfully login into account")
    else:
        print("Wrong password")

    return


def task2() -> None:
    text_pass: list[str] = "12345 11111 4444 8989".split()

    password: str = input("Input password: ")

    if password in text_pass:
        print("You successfully login into account")
    else:
        print("Wrong password")

    return


def task3() -> None:
    input_score: int = int(input("Enter your score: "))

    scores: dict[int, str] = {
        90: "A",
        82: "B",
        74: "C",
        64: "D",
        60: "E",
        35: "FX",
        0: "F",
    }

    result: str = "-"

    for score in scores:
        if input_score >= score:
            result = scores.get(score)
            break

    print(f"Your score is {result}")
    return


def task4() -> None:
    a, b = input("Input two values: ").split()

    if a > b:
        print("B is lower")
        return

    if a < b:
        print("A is lower")
        return

    print("They are equals")
    return


def task5() -> None:
    values: list[int] = [int(x) for x in input("Input values: ").split()]

    value: int = max(values)

    print(f"Max values is {value}")
    return


def task6() -> None:
    x: int = int(input("Input x value: "))

    if x > 0:
        print("x > 0")
        return

    if x < 0:
        print("x < 0")
        return

    print("x == 0")
    return


def task7() -> None:
    x: int = int(input("Input x value: "))

    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")

    return


def task7_crime_version() -> None:
    x: int = int(input("Input x value: "))

    print("x is " + "eovdedn"[x % 2::2])
    return


def task8() -> None:
    days: dict[int, str] = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    day_as_number: int = int(input("Input today's day number: "))

    day: str = days.get(day_as_number)

    if day is None:
        raise Exception("Day must be from 1 to 7")

    print(f"Today is {day}")
    return


def task9() -> None:

    currencies: dict[str, float] = {
        "usd": 36,
        "eur": 40
    }

    try:
        currency: str = input("Input currency to convert: ")
        value: float = float(input("Input value: "))

        currency_value = currencies.get(currency)

        if currency_value is None:
            raise Exception(f"Currency {currency} is not exists")

        print(f"In {currency} it's: {value / currency_value}")

    except:
        print("Something went wrong")

    return


def main() -> None:
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task7_crime_version()
    # task8()
    task9()
    return


if __name__ == '__main__':
    main()
