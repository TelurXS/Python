
def task1() -> None:

    dictionary: dict[str, int] = {
        "key3": 3,
        "key1": 1,
        "key2": 2,
    }

    print(sorted(dictionary.values()))
    return


def task2() -> None:
    dictionary: dict[str, int] = {
        'a': 500,
        'b': 5874,
        'c': 560,
        'd': 400,
        'e': 5874,
        'f': 20
    }

    values: list[int] = list(dictionary.values())

    biggest: list[int] = (
        sorted(values, reverse=True)[:3])

    for key, value in dictionary.items():
        if value in biggest:
            print(key)

    return


def task3() -> None:

    rivers: dict[str, str] = {
        "Nile River": "North-East Africa",
        "Amazon River": "South America",
        "Yangtze River": "China",
    }

    for key, value in rivers.items():
        print(f"{key} is flows in {value}")

    return


def task4() -> None:
    dictionary: dict[int, int] = {}
    n: int = int(input("Input N: "))

    for i in range(1, n + 1):
        dictionary[i] = i * i

    print(dictionary)
    return


def task5() -> None:

    file = open("mbox-short.txt", "r")
    emails: dict[str, int] = {}

    for line in file.readlines():
        if line.startswith("From: "):
            words: list[str] = line.split()
            email: str = words[1]

            if email not in emails.keys():
                emails[email] = 1

            else:
                emails[email] += 1

    max_count: int = 0
    max_email: str = ""

    for email, count in emails.items():
        if count > max_count:
            max_count = count
            max_email = email

    print(f"Email with max appearance count: {max_email} with count: {max_count}")
    return


def task6() -> None:

    inventory: dict[str, int] = {
        "Rope": 1,
        "Bomb": 2,
        "Rupy": 43,
        "Hero's Bow": 1,
        "Arrows": 21
    }

    total: int = 0

    print("=================")
    print("Inventory:")

    for item, count in inventory.items():
        print(f"{item}: {count}")
        total += count

    print(f"Total: {total}")
    print("=================")
    return


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    return


if __name__ == "__main__":
    main()
