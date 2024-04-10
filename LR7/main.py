def task1() -> None:
    numbers: list[int] = [1, 2, 4, 5, 2, 6, 7]
    sum: int = 0

    for number in numbers:
        sum += number

    print(f"Sum is {sum}")
    return


def task2() -> None:
    words: list[str] = ["faw", "daw", "d", "w", "dafa", "ff"]
    count: int = 0

    for word in words:
        if len(word) > 2:
            count += 1

    print(f"Count is {count}")
    return


def task3() -> None:
    numbers: list[int] = [1, 2, 4, 5, 2, 6, 7, 6, 1, 9]
    distinct_numbers: list[int] = []

    for number in numbers:
        if number not in distinct_numbers:
            distinct_numbers.append(number)

    print(f"Distinct numbers: {distinct_numbers}")
    return


def task4() -> None:
    file = open("romeo.txt", "r")
    lines: list[str] = file.readlines()
    words: list[str] = []

    for line in lines:
        words.extend(line.split())

    print(f"All words: {words}")
    return


def task5() -> None:
    file = open("mbox-short.txt", "r")
    lines: list[str] = file.readlines()
    count: int = 0

    for line in lines:
        if line.startswith("From"):
            words: list[str] = line.split()
            print(words[1])
            count += 1

    print(f"Count: {count}")
    return


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    return


if __name__ == "__main__":
    main()