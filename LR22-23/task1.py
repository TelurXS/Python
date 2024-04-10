import pandas as pd


def main() -> None:
    data = pd.read_csv("train.csv")
    df = data.copy()

    # 1
    print(df)

    # 2
    print(df.head(5))

    # 3
    print(df.tail(5))

    # 4
    print(df.shape)

    # 5
    print(df.columns)

    # 6
    print(df.index)

    # 7
    print(df.dtypes)

    # 8
    print(df.isna())

    # 9
    print(df["Pclass"].unique())

    # 10
    print(df["Pclass"].value_counts())

    # 11
    print(df.describe())

    # 12
    print(df["Age"].mean())

    # 13
    print(df["Age"].max())

    # 14
    print(df["Age"].min())

    # 15
    print(df["Fare"].sum())

    # 16
    print(df.isnull().sum())

    # 17
    df["Age"].fillna(df["Age"].mean(), inplace=True)
    print(df["Age"].isnull().sum())

    # 18
    print((df["Sex"] == "male").sum())
    print((df["Sex"] == "female").sum())

    # 19
    df["Sex"] = df["Sex"].map({"male": "0", "female": "1"})

    # 20
    print(df["Name"].info())

    # 21
    df["LastName"] = df["Name"].apply(lambda x: x.split(", ")[0])
    df["FirstName"] = df["Name"].apply(lambda x: ' '.join(x.split(",")[1:]))
    print(df[["LastName", "FirstName"]])

    # 22
    df = df.rename(columns={"Sex": "Gender", "Name": "FullName", "FirstName": "Name", "LastName": "Surname"})
    print(df[["Gender", "FullName", "Name", "Surname"]])

    # 23
    print(df[df["Pclass"] == 3].reset_index(drop=True))

    # 24
    print(df[(df["Age"] > 60) & (df["Gender"] == "1")])

    # 25
    print(df.select_dtypes(include=["int16", "int32", "int64", "float16", "float32", "float64"]))

    # 25
    print(df.select_dtypes(include=["object"]))

    # 26
    print(df["Embarked"].unique())

    # 27
    print(df["Embarked"].fillna("S").value_counts())

    # 28
    male_survived = df[df["Gender"] == "0"]["Survived"]
    female_survived = df[df["Gender"] == "1"]["Survived"]

    print(f"Males: {round(100 * male_survived.mean(), 1)}%, Females: {round(100 * female_survived.mean(), 1)}%")

    # 29
    young_survived = df[df["Age"] < 30]["Survived"]
    old_survived = df[df["Age"] > 60]["Survived"]

    print(f"Young: {round(100 * young_survived.mean(), 1)}%, Old: {round(100 * old_survived.mean(), 1)}%")

    # 30
    print(df["Name"].value_counts().head())
    

if __name__ == "__main__":
    main()
