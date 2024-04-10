import pandas as pd
import numpy as np


def main() -> None:

    # 1
    data = pd.read_csv("Loan.txt")

    # 2
    print(data.shape)

    # 3
    print(data.isnull().sum())

    # 4
    print(data.columns[(data.isna().sum() > 10)])

    # 5
    print(data[data.isnull().sum(axis=1) > 2])

    # 6
    print(data[(data["Dependents"].isna()) & (data["Married"] == 'No')])

    # 7
    data["Dependents"][(data["Dependents"].isna()) & (data["Married"] == 'No')] = "NA"

    # 8
    print(data["Dependents"].unique())

    # 9
    print(data["Married"].unique())

    # 10
    data["Married"][(data["Married"].isna()) & (data["Dependents"] != 0)] = 'No'


    return


if __name__ == "__main__":
    main()
