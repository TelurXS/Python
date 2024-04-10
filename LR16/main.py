import matplotlib.pyplot as plt
import numpy as np


def get_dots(frm=0, to=100, step=1) -> list[float]:
    return list(np.arange(frm, to, step))


def x() -> list[float]:
    return get_dots()


def y() -> list[float]:
    return [i * 2 for i in get_dots()]


def z() -> list[float]:
    return [i ** 2 for i in get_dots()]


def task1() -> None:
    plt.subplot(221)
    plt.plot(x(), x(), "r--")
    plt.legend("x")
    plt.title("Graph", fontsize=10)
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.subplot(222)
    plt.plot(x(), y(), "b")
    plt.legend("y")
    plt.title("Graph")
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.subplot(223)
    plt.plot(x(), z(), "g:")
    plt.legend("z")
    plt.title("Graph", fontsize=10)
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.text(25, 4000, "z=x^2")
    plt.grid()

    #plt.subplot(224)
    #plt.plot(x(), x(), "r--")
    #plt.plot(x(), y(), "b")
    #plt.plot(x(), z(), "g:")
    #plt.title("Graph", fontsize=10)
    #plt.xlabel("X", fontsize=10, loc="right")
    #plt.ylabel("Y", fontsize=10, loc="top")
    #plt.grid()

    plt.show()
    return


def get_dots_from_file() -> tuple[list[float], list[float]]:
    x: list[float] = []
    y: list[float] = []

    with open("test.txt") as file:
        lines = file.readlines()

        for line in lines:
            line = line.rstrip()
            x_str, y_str = line.split(" ")
            x.append(float(x_str))
            y.append(float(y_str))

    return x, y


def task2() -> None:
    x, y = get_dots_from_file()

    plt.plot(x, y, "r--")
    plt.title("Graph", fontsize=10)
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.show()
    return


def task3() -> None:
    x = np.arange(0, 100)

    plt.subplot(221)
    plt.plot(x, x**2, "r--")
    plt.legend("x")
    plt.title("x^2", fontsize=10)
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.subplot(222)
    plt.plot(x, np.sin(x), "b")
    plt.legend("y")
    plt.title("sin(x)")
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.subplot(223)
    plt.plot(x, np.cos(x), "g:")
    plt.legend("z")
    plt.title("cos(x)", fontsize=10)
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.subplot(224)
    plt.plot(x, x, "m+")
    plt.title("y=x", fontsize=10)
    plt.xlabel("X", fontsize=10, loc="right")
    plt.ylabel("Y", fontsize=10, loc="top")
    plt.grid()

    plt.show()
    return


def main() -> None:
    task3()
    return


if __name__ == "__main__":
    main()
