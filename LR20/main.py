import re


def task1() -> None:
    text: str = "*&%@afw#!}{"
    expression = re.compile("[a-zA-Z0-9]+")
    result = expression.search(text)

    print(bool(result))
    return


def task2() -> None:
    text: str = "abbc"
    expression = re.compile("a(b){2,}")
    result = expression.search(text)

    print(bool(result))
    return


def task3() -> None:
    text: str = "aab_cbbbc"
    expression = re.compile("^[a-z_]+$")
    result = expression.fullmatch(text)

    print(bool(result))
    return


def task4() -> None:
    text: str = ("Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org "
                 "first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net")

    expression = re.compile("[a-zA-Z0-9.-_]+@[a-zA-Z0-9.-_]+")
    result = expression.findall(text)

    print(result)
    return


def task5() -> None:
    text: str = "216.08.094.196"

    result = re.sub("0", "", text)

    print(result)
    return


def task6() -> None:
    text: str = "abcdef9"

    expression = re.compile("^[a-zA-Z]+[0-9]$")
    result = expression.fullmatch(text)

    print(bool(result))
    return


def task7() -> None:
    text: str = "2026-01-02"

    expression = re.compile("^([0-9]{4})-([0-9]{2})-([0-9]{2})$")
    result = expression.search(text)

    print(f'{result.group(3)}-{result.group(2)}-{result.group(1)}')
    return


def task8() -> None:
    text: str = ("Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com "
                 "abc111@test.com.net +380(67)111-777-777+380(67)777-77-787")

    expression = re.compile(r"\+[0-9]{3}\([0-9]{2}\)[0-9]{3}-[0-9]{1,2}-[0-9]{2,3}")

    result = expression.findall(text)

    print(result)
    return


def task9() -> None:
    text: str = "LorEm ipsum dOloR amEn"

    expression = re.compile(r"[a-z]+", re.IGNORECASE)

    result = expression.findall(text)

    print(result)
    return


def sanitize_phone_numbers(numbers: list[str]) -> list[str]:

    result: list[str] = []
    expression = re.compile(r"[-+,() ]+")

    for number in numbers:
        formatted = expression.sub("", number)
        result.append(formatted)

    return result


def task10() -> None:

    numbers: list[str] = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    print(sanitize_phone_numbers(numbers))
    return


def main() -> None:
    task10()
    return


if __name__ == "__main__":
    main()
