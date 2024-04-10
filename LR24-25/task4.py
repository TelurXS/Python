import pandas as pd
import numpy as np
import re


def main() -> None:
    data = pd.read_csv("olymp.csv", header=1)
    print(data.columns)

    to_rename = {
        "Unnamed: 0": "Country",
        "? Summer": "Summer Olympics",
        "01 !": "Gold",
        "02 !": "Silver",
        "03 !": "Bronze",
        "? Winter": "Winter Olympics",
        "01 !.1": "Gold.1",
        "02 !.1": "Silver.1",
        "03 !.1": "Bronze.1",
        "? Games": "# Games",
        "01 !.2": "Gold.2",
        "02 !.2": "Silver.2",
        "03 !.2": "Bronze.2",

    }
    data.rename(columns=to_rename, inplace=True)

    print(data.columns)
    print(data[["Country", "Gold", "Silver", "Bronze"]])
    return


if __name__ == "__main__":
    main()
