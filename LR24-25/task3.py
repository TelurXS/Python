import pandas as pd
import numpy as np
import re


def main() -> None:
    expression = re.compile(r"([a-zA-Z ]+) \(([a-zA-Z ]+)\)")

    towns: list[str] = []
    universities: list[str] = []

    with open("towns.txt") as file:
        for line in file.readlines():
            line = line.rstrip("\n")

            result = expression.search(line)

            if not result:
                continue

            towns.append(result.group(1))
            universities.append(result.group(2))

    data = pd.DataFrame({"Towns": towns, "Universities": universities})

    print(data)
    return


if __name__ == "__main__":
    main()
