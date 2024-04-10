import numpy as np


def task1() -> None:
    vector = np.zeros(10)
    print(vector)
    return


def task2() -> None:
    vector = np.zeros(10)
    vector[3::4] = 5
    print(vector)
    return


def task3() -> None:
    values = np.arange(25, 50)
    print(values)
    return


def task4() -> None:
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])

    print(matrix)
    print(matrix[0, :])
    print(matrix[:, 1])
    print(np.average(matrix[:, 3]))
    print(f"{matrix.min()} at {matrix.argmin()}")
    print(f"{matrix.max()} at {matrix.argmax()}")

    diagonal = np.diagonal(matrix)
    non_zero_values = diagonal[diagonal != 0]
    print(np.prod(non_zero_values))

    matrix[:, [1, 3]] = matrix[:, [3, 1]]
    print(matrix)
    return


def task5() -> None:
    temperatures = np.array([[-8, -14, -19, -18],
                             [25, 28, 26, 20],
                             [11, 18, 20, 25]])

    print(temperatures[1, 3])

    print(temperatures[:, 1])

    print(np.mean(temperatures[2, :]))

    stations, days = np.nonzero((temperatures >= 24) & (temperatures <= 26))
    for station, day in zip(stations, days):
        print(f"Day {day + 1}, Station {station + 1}")
    return


def task6() -> None:
    matrix = np.array([[4, 2],
                       [1, 3]])

    print(np.sort(matrix, axis=0))
    print(np.sort(matrix, axis=1))
    return


def task7() -> None:
    array1 = np.array([[1, 2, np.nan, 4, 5, np.nan, 7]])
    array2 = np.array([[1, 2, 3, 4, 5]])

    mean_value = np.nanmean(array2)

    nan_mask = np.isnan(array1)
    array1[nan_mask] = mean_value
    print(array1)
    return


def task8() -> None:
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16],
                       [17, 18, 19, 20]])

    print(matrix[(matrix > 6) | (matrix % 3 == 0)])
    return


def task9() -> None:
    matrix = np.array([[1, 2, 0, 4],
                       [5, 6, 0, 8],
                       [9, 10, 0, 12],
                       [13, 14, 0, 16]])

    for y in range(matrix.shape[1]):
        if np.all(matrix[:, y] == 0):
            print("Has zero column")
            break
    return


def task10() -> None:
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])

    print(np.sum(np.diagonal(matrix)))
    return


def task11() -> None:
    matrix = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])

    elements_from_10_to_20 = np.where((matrix >= 10) & (matrix <= 20))
    matrix[elements_from_10_to_20] *= -1

    elements_from_0_to_10 = np.where((matrix >= 0) & (matrix < 10))
    matrix[elements_from_0_to_10] *= 3

    print(matrix)
    return


def main() -> None:
    # task1()
    # task2()
    # task3()
    # task5()
    # task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    return


if __name__ == "__main__":
    main()
