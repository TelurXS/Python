import pandas as pd
import numpy as np


def main() -> None:
    # 1
    data = pd.read_csv("Book.csv")

    # 2
    print(data.head(5))

    # 3
    data.drop(columns=['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner',
                       'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks'], inplace=True)

    # 4
    print(data.head(5))

    # 5
    print(data["Identifier"].is_unique)

    # 6
    data.set_index("Identifier", inplace=True)

    # 7
    print(data.loc[206])

    # 8
    print(data.dtypes)

    # 9
    print(data.loc[1905:, "Date of Publication"].head(10))

    # 10
    extr = data['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

    # 11
    data['Date of Publication'] = pd.to_numeric(extr)

    # 12
    print(data['Date of Publication'].isnull().sum() / len(data))

    # 13
    print(data["Place of Publication"])

    # 14
    print(data["Place of Publication"].str.contains("London").head(5))
    print(data["Place of Publication"].str.contains("Oxford").head(5))

    # 15
    london = data["Place of Publication"].str.contains("London")
    oxford = data["Place of Publication"].str.contains("Oxford")

    data['Place of Publication'] = np.where(london, ' London ',
                                            np.where(oxford, 'Oxford',
                                                     data['Place of Publication'].str.replace('-', ' ')))

    data.loc[data["Place of Publication"] == " London ", "Place of Publication"] = "London"

    # 16
    print(data.loc[data["Place of Publication"] == "London", "Place of Publication"].value_counts())

    # 17
    print(data[(data["Date of Publication"] > 1860) & (data["Date of Publication"] < 1870)])

    # 18
    print(data[data["Date of Publication"] == data["Date of Publication"].max()])

    # 19
    print(data[data["Date of Publication"] == data["Date of Publication"].min()])
    return


if __name__ == "__main__":
    main()
