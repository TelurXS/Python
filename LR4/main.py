import random


def task1() -> None:
    n: int = 2

    while n <= 512:
        print(n)
        n *= 2

    return


def task2() -> None:
    text: str = input("Input number: ")
    numbers: list[int] = [int(x) for x in text]
    result: int = sum(numbers)

    print(f"Result is {result}")
    return


def task3() -> None:
    result: int = 0

    while True:
        number: int = int(input("Input number: "))

        if number <= 0:
            break

        result += number

    print(f"Sum is {result}")
    return


def task4() -> None:
    result: int = 0
    n: int = 0

    while True:
        number: int = int(input("Input number: "))

        if number == 0:
            break

        result += number
        n += 1

    print(f"Avarage is {result / n}")
    return


def task5() -> None:
    word: str = input("Input word: ")

    vowel_letters: list[str] = ['а', 'у', 'о', 'е', 'и', 'і', 'ї', 'є', 'я', 'ю']

    for letter in word:
        if letter.lower() not in vowel_letters:
            print(letter, end="")

    return


def task6() -> None:
    prices: dict[int, float] = {
        12: 80,
        3: 50
    }

    total_price: float = 0

    while True:
        request: str = input("Input customer age: ")

        if request == "exit":
            break

        age: int = int(request)
        price: float = 0

        for required_age in prices:
            if age >= required_age:
                price = prices.get(required_age)
                break

        total_price += price
        print(f"Added {price} to total price. Total: {total_price}")

    print(f"Total: {total_price}")
    return


def task7() -> None:
    number: int = random.randint(0, 10)

    while True:
        request: str = input("Input number (exit - to exit): ")

        if request == "exit":
            break

        if request.isdigit() is False:
            print("Enter a number please")
            continue

        answer: int = int(request)

        if answer == number:
            print("You win")
            break

        print("Wrong number")
    return


def main() -> None:
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    task7()
    return


if __name__ == '__main__':
    main()
