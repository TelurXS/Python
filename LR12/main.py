import re
from datetime import datetime, timedelta


def bank(x: float, years: int, percent: float = 0.10) -> float:
    for _i in range(years):
        x += x * percent

    return x


def task1() -> None:
    print(f"For 1000 in 2 year(s): {bank(1000, 2)}")
    print(f"For 10000 in 4 year(s): {bank(10000, 4)}")
    print(f"For 2000 in 1 year(s): {bank(2000, 1)}")
    return


def task2() -> None:
    options: dict[str, callable] = {
        "sunny": lambda: print("It is sunny today, good to wear Sneakers"),
        "snowy": lambda: print("Wow! It's snowy today, better to wear Boots"),
        "rainy": lambda: print("Oops! It's raining today, Gumboot would be better tot wear"),
    }

    value: str = input("Input weather: ")

    if value in options:
        options.get(value)()

    else:
        print("Invalid option")

    return


def combine(x: list[int], y: list[int]) -> list[int]:
    result: list[int] = []

    length: int = len(x) if len(x) < len(y) else len(y)

    for i in range(length):
        result.append(x[i])
        result.append(y[i])

    return result


def task3() -> None:
    x: list[int] = [1, 2, 3]
    y: list[int] = [11, 22, 33]

    print(combine(x, y))
    return


def get_next_day_date(day: int, month: int, year: int) -> tuple[int, int, int]:
    date = datetime(day=day, month=month, year=year) + timedelta(days=1)
    return date.day, date.month, date.year


def get_prev_day_date(day: int, month: int, year: int) -> tuple[int, int, int]:
    date = datetime(day=day, month=month, year=year) - timedelta(days=1)
    return date.day, date.month, date.year


def task4() -> None:
    print(get_next_day_date(30, 11, 2023))
    print(get_prev_day_date(30, 11, 2023))
    return


def print_in_frame(text: str, border: str = "*") -> None:
    print(border * (len(text) + 2))
    print(f"*{text}*")
    print(border * (len(text) + 2))


def task5() -> None:
    print_in_frame("Text in frame")
    return


def get_input() -> str:
    return input("Input a value: ")


def test_input(value: str) -> bool:
    try:
        int(value)
        return True

    except ValueError:
        return False


def str_to_int(value: str) -> int:
    return int(value)


def print_int(value: int) -> None:
    print(value)


def task6() -> None:
    value: str = get_input()

    if test_input(value):
        value_as_int: int = str_to_int(value)
        print_int(value_as_int)

    return


def print_words(words: list[str]) -> None:
    print("-".join(words))


def task7() -> None:
    line: str = input("Input a line: ")
    words: list[str] = sorted(line.split("-"))
    print_words(words)
    return


def is_email(value: str) -> bool:
    pattern: str = "^[a-zA-Z0-9][a-zA-Z0-9._%]{0,127}@[a-zA-Z0-9.]{2,64}\\.[a-zA-Z]{2,64}$"
    return bool(re.search(pattern, value))


def task8() -> None:
    value: str = input("Input a email: ")
    print(f"Is email: {is_email(value)}")
    return


def main() -> None:
    task8()
    return


if __name__ == "__main__":
    main()
