def task1() -> None:
    for x in range(1, 20):
        print(x)

    return


def task2() -> None:
    a: int = int(input("Input A: "))
    b: int = int(input("Input B: "))

    step: int = 1 if a < b else -1

    for x in range(a, b, step):
        print(x)

    return


def task3() -> None:
    numbers_as_text: list[str] = input("Input numbers: ").split()
    numbers: list[int] = [int(x) for x in numbers_as_text]

    print(f"Sum is {sum(numbers)}")
    return


def task4() -> None:
    numbers_as_text: list[str] = input("Input numbers: ").split()
    numbers: list[int] = [int(x) for x in numbers_as_text]

    print("Even numbers: ")

    for number in numbers:
        if number % 2 == 0:
            print(number, end=" ")

    print()
    return


def task5() -> None:
    numbers_as_text: list[str] = input("Input numbers: ").split()
    numbers: list[int] = [int(x) for x in numbers_as_text]

    print(f"Max is {max(numbers)}")
    return


def task6() -> None:
    value: str = input("Input text: ")

    for i in range(len(value)):
        if i % 2 == 0:
            print(value[i], end=" ")

    print()
    return


def task7() -> None:
    cols: int = int(input("Input columns count: "))

    for x in range(cols):
        for y in range(x):
            print("*", end=" ")
        print()

    for x in range(cols, 0, -1):
        for y in range(x):
            print("*", end=" ")
        print()

    return


def task8() -> None:
    amount: float = float(input("Input amount(>0): "))
    percent: float = float(input("Input percent(0-1): "))
    period: int = int(input("Input period(>0): "))

    if amount <= 0:
        raise Exception("Amount must be greater than 0")

    if percent <= 0 or percent > 1:
        raise Exception("Percent must be greater than 0")

    if period <= 0:
        raise Exception("Period must be greater than 0")

    result: float = amount

    for i in range(period):
        result *= 1 + percent

    profit: float = result - amount

    print(f"Result is {result:.2f}")
    print(f"Profit is {profit:.2f}")
    return


def task9() -> None:
    result: float | None = None
    operand: float | None = None
    operator: str | None = None
    wait_for_number: bool = True

    operators: dict[str, callable(float)] ={
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y,
        "%": lambda x, y: x % y,
    }

    while True:
        try:
            value: str = input()

            if value == "=":
                print(f"Result is {result}")
                break

            if wait_for_number:

                if value.isdigit() is False:
                    raise Exception(f"{value} is not a number")

                if result is None:
                    result = float(value)
                    wait_for_number = False
                    continue

                operand = float(value)
                wait_for_number = False

            else:
                if value in operators:
                    operator = value
                    wait_for_number = True

                else:
                    raise Exception("Operator expected")

            if operator is not None and operand is not None:
                result = operators.get(operator)(result, operand)
                operator = None
                operand = None

        except Exception as exception:
            print(exception.args[0])

    return


def main() -> None:
    task9()
    return


if __name__ == "__main__":
    main()
