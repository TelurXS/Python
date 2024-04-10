import re
import locale
locale.setlocale(locale.LC_ALL, "ukr")


def task1() -> None:
    translate: dict[str, str] = {}

    with open("dict.txt") as file:
        lines: list[str] = file.readlines()

        for line in lines:
            line = line.replace("\n", "")

            if line == "":
                continue

            key, value = line.split("\t-\t")
            translate[key] = value

    with open("translate.txt") as file:
        lines: list[str] = file.readlines()

        for line in lines:
            words: list[str] = re.split(r"(\W+)", line)

            for word in words:
                if word.lower() in translate:
                    print(translate[word.lower()], end="")
                else:
                    print(word, end="")

    return


def task2() -> None:
    countries: dict[str, list[str]] = {}

    with open("input_countries.txt") as file:
        lines: list[str] = file.readlines()

        for line in lines:
            line = line.replace("\n", "")

            if line == "":
                continue

            splited: list[str] = line.split(": ")

            if len(splited) < 2:
                continue

            country, languages = splited

            key: str = country.replace(" ", "")
            value: list[str] = languages.split(" ")

            countries[key] = value

    print(countries)

    language: str = input("Input language: ")

    for key, value in countries.items():
        if language in value:
            print(key)

    return


def is_all_seats_free(compartment: dict[int, str | None]) -> bool:
    for seat in compartment.values():
        if seat is not None:
            return False

    return True


def print_free_seats(compartment: dict[int, str | None]) -> None:
    for number, seat in compartment.items():
        if seat is None:
            print(number, end=" ")
    return


def print_free_bottom_seats(compartment: dict[int, str | None]) -> None:
    bottom_left: int = 1
    bottom_right: int = 2

    for number, seat in compartment.items():
        if number != bottom_left and number != bottom_right:
            continue

        if seat is None:
            print(number, end=" ")
    return


def print_free_top_seats(compartment: dict[int, str | None]) -> None:
    top_left: int = 3
    top_right: int = 4

    for number, seat in compartment.items():
        if number is not top_left and number is not top_right:
            continue

        if seat is None:
            print(number, end=" ")
    return


def is_compartment_with_men_only(compartment: dict[int, str | None]) -> bool:
    is_found: bool = False

    for number, seat in compartment.items():
        if seat == "w":
            return False

        if seat == "m" and not is_found:
            is_found = True

    return is_found


def is_compartment_with_women_only(compartment: dict[int, str | None]) -> bool:
    is_found: bool = False

    for number, seat in compartment.items():
        if seat == "m":
            return False

        if seat == "w" and not is_found:
            is_found = True

    return is_found


def task3() -> None:
    bottom_left: int = 1
    bottom_right: int = 2
    top_left: int = 3
    top_right: int = 4

    compartments: dict[int, dict[int, str | None]] = {
        1: {bottom_left: "m", bottom_right: None, top_left: "w", top_right: None},
        2: {bottom_left: None, bottom_right: None, top_left: None, top_right: None},
        3: {bottom_left: None, bottom_right: None, top_left: None, top_right: "w"},
        4: {bottom_left: "w", bottom_right: None, top_left: None, top_right: None},
        5: {bottom_left: "m", bottom_right: "m", top_left: "m", top_right: None},
        6: {bottom_left: None, bottom_right: None, top_left: None, top_right: None},
    }

    print("Free compartments: ( ", end="")

    for key, value in compartments.items():
        if is_all_seats_free(value):
            print(key, end=" ")

    print(")")

    print("Free seats: ")

    for key, value in compartments.items():
        print(f"{key} compartment: ( ", end="")
        print_free_seats(value)
        print(")")

    print()

    print("Free bottom seats: ")

    for key, value in compartments.items():
        print(f"{key} compartment: ( ", end="")
        print_free_bottom_seats(value)
        print(")")

    print()

    print("Free top seats: ")

    for key, value in compartments.items():
        print(f"{key} compartment: ( ", end="")
        print_free_top_seats(value)
        print(")")

    print()
    print("Free seats only with men: ")

    for key, value in compartments.items():
        if is_compartment_with_men_only(value):
            print(f"{key} compartment: ( ", end="")
            print_free_seats(value)
            print(")")

    print()

    print("Free seats only with women: ")

    for key, value in compartments.items():
        if is_compartment_with_women_only(value):
            print(f"{key} compartment: ( ", end="")
            print_free_seats(value)
            print(")")

    print()
    return


def main() -> None:
    task2()
    return


if __name__ == "__main__":
    main()
