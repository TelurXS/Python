
def f(x: float, y: float) -> float:
    return 3*x + 3*y*y


def fy(x: float, y_prev: float, dx: float) -> float:
    return y_prev + dx * f(x, y_prev)


def main() -> None:
    dx: float = 0.08
    x: float = 0
    y: float = 0

    y_prev: float = y

    for i in range(0, 20):
        x += dx

        if x >= 1.9:
            break

        y_prev = y
        y = fy(x, y_prev, dx)

        print(f"{i+1}) x={x:0.2f}: y_prev={y_prev:0.2f}, y={y:0.2f}")
    return


while True:
    text = input("Input text: ")

    if text == "exit":
        break


try:
    as_number = int(text)
except ValueError:
    print("Text is not a number")

if __name__ == '__main__':
    main()
