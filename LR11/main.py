
def task1() -> None:
    set1: set[int] = {10, 20, 30, 40, 50}
    set2: set[int] = {30, 40, 50, 60, 70}

    repetitions: set[int] = set()

    for value in set1:
        if value in set2 and value not in repetitions:
            repetitions.add(value)

    print(repetitions)
    return


def task1_short() -> None:
    set1: set[int] = {10, 20, 30, 40, 50}
    set2: set[int] = {30, 40, 50, 60, 70}

    print(set1.intersection(set2))
    return


def task2() -> None:
    set1: set[int] = {10, 20, 30, 40, 50}
    set2: set[int] = {30, 40, 50, 60, 70}

    unique: set[int] = set()

    for value in set1.union(set2):
        if value not in unique:
            unique.add(value)

    print(unique)
    return


def task2_short() -> None:
    set1: set[int] = {10, 20, 30, 40, 50}
    set2: set[int] = {30, 40, 50, 60, 70}

    intersects: set[int] = set1.intersection(set2)
    unique: set[int] = set1.union(set2).difference(intersects)

    print(unique)
    return


def task3() -> None:
    a: set[int] = {10, 20, 30, 40, 50}
    b: set[int] = {30, 40, 50, 60, 70}

    result = a.difference(b).union(b.difference(a))

    print(result)
    return


def get_difference(list1: list[int], list2: list[int]) -> list[int]:
    return list(set(list1).difference(set(list2)))


def task4() -> None:
    list1: list[int] = [1, 2, 3, 4, 5, 6]
    list2: list[int] = [4, 5, 6, 7, 8]

    print(f"Missing values in list1 = {get_difference(list2, list1)}")
    print(f"Additional values in list1 = {get_difference(list1, list2)}")
    print(f"Missing values in list2 = {get_difference(list1, list2)}")
    print(f"Additional values in list2 = {get_difference(list2, list1)}")
    return


def compare_sets(set1: set[int], set2: set[int]) -> bool:
    return len(set1.intersection(set2)) == 0


def task5() -> None:
    a: set[int] = {23, 8, 56, 45, 78}
    b: set[int] = {42, 26, 55, 87}
    z: set[int] = {46, 87}

    print(f"Compare A and B : {compare_sets(a, b)}")
    print(f"Compare B and Z : {compare_sets(b, z)}")
    print(f"Compare A and Z : {compare_sets(a, z)}")
    return


def task6() -> None:
    values: set[int] = set(range(1, 50))

    while True:
        text: str = input("Input number: ")

        if text == "exit":
            break

        number: int = int(text)

        if number < min(values):
            print("The number is Low")
            continue

        if number > max(values):
            print("The number is High")
            continue

        if number in values:
            print("The number within Range")
            continue

    return


def task7() -> None:
    text: str = input("Input text: ")
    chars: set[str] = set(text)
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}

    count: int = len(chars.intersection(vowels))

    print(f"Count: {count}")
    return


def main() -> None:
    task1()
    task1_short()
    task2()
    task2_short()
    task3()
    task4()
    task5()
    task6()
    task7()
    return


if __name__ == "__main__":
    main()
