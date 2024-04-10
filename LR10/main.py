def get_tuple() -> tuple:
    return tuple([int(x) for x in input("Input tuple: ").split(", ")])


def task1() -> None:
    values = get_tuple()

    repetitions: dict[int, int] = {}

    for value in values:
        if value not in repetitions:
            repetitions[value] = 1

        else:
            repetitions[value] += 1

    print(repetitions)
    return


def task2() -> None:
    values = get_tuple()
    print(values)

    query: int = int(input("Input a number to find: "))

    if query in values:
        index: int = values.index(query)
        print(f"Index is {index}")

    else:
        print("Value is not exist")

    return


def task3() -> None:
    values = get_tuple()

    first_and_last = (values[0], values[-1])

    print(first_and_last)
    return


def task4() -> None:
    values = get_tuple()

    if len(values) <= 1:
        print("Values are empty")
        return

    first = values[0]

    for value in values:
        if value != first:
            print("Values are not the same")
            return

    print("Values are the same")
    return


def task5() -> None:
    values = (3, 4, '3', "a", "faf")
    summa: int = 0

    for value in values:
        try:
            int_value = int(value)
            summa += int_value
        except:
            pass

    print(summa)
    return


def task6() -> None:
    tuples = [(1, 2, 3), (3, 4, 5), (6, 7, 8)]

    new_tuples = []
    for values in tuples:
        *midle_values, last_value = values
        new_tuples.append((*midle_values, 100))

    print(new_tuples)

    return


def task7() -> None:
    with open("mbox-short.txt") as file:
        lines: list[str] = file.readlines()
        repetitions: dict[str, int] = {}

        for line in lines:
            if line.startswith("From "):
                hour = line.split(" ")[6].split(":")[0]

                if hour not in repetitions:
                    repetitions[hour] = 1
                else:
                    repetitions[hour] += 1

        print(repetitions)
    return


def calculate_distance(points, coordinates):
    if not coordinates or len(coordinates) == 1:
        return 0

    distance: float = 0

    for i in range(len(coordinates) - 1):
        point1 = coordinates[i]
        point2 = coordinates[i + 1]

        if point2 < point1:
            point1, point2 = point2, point1

        distance += points[(point1, point2)]

    return distance


def task8() -> None:
    points: dict[tuple[int, int], int] = {
        (0, 1): 2,
        (0, 2): 3.8,
        (0, 3): 2.7,
        (1, 2): 2.5,
        (1, 3): 4.1,
        (2, 3): 3.9,
    }

    coordinates: list[int] = [0, 1, 3, 2, 0]

    print(f"Distance: {calculate_distance(points, coordinates)}")
    return


def main() -> None:
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    return


if __name__ == "__main__":
    main()
