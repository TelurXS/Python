from datetime import datetime

import pandas as pd


def main() -> None:

    # 1
    data = pd.read_csv("London_2014.csv", skipinitialspace=True)

    # 2
    print(data["WindDirDegrees<br />"])

    # 3
    data = data.rename(columns={"WindDirDegrees<br />": "WindDirDegrees"})

    # 4
    data["WindDirDegrees"] = data["WindDirDegrees"].str.rstrip("<br />")

    # 5
    data.info()

    # 6
    data["Events"].info()

    # 7
    print(data["Events"].isna())

    # 8
    print(data["Events"].isna().sum())

    # 9
    data = data.dropna()

    # 10
    print(data.dtypes)

    # 11
    data["WindDirDegrees"] = data["WindDirDegrees"].astype("int64")

    # 12
    data["GMT"] = pd.to_datetime(data["GMT"])

    # 13
    print(data["WindDirDegrees"].dtypes)

    # 14
    print(data[data["GMT"] == datetime(2014, 6, 4)])

    # 15
    start = datetime(2014, 12, 8)
    end = datetime(2014, 12, 12)
    print(data[(data["GMT"] >= start) & (data["GMT"] <= end)])

    # 16
    start = 10
    end = 350
    print(data[(data["WindDirDegrees"] <= start) | (data["WindDirDegrees"] >= end)])

    # 17
    start = datetime(2014, 4, 1)
    end = datetime(2014, 4, 14)
    print(data[(data["GMT"] >= start) & (data["GMT"] <= end)])

    return


if __name__ == "__main__":
    main()
