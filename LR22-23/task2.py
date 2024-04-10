import pandas as pd


def main() -> None:
    data = pd.read_excel("WHO POP TB.xls")
    data["TB deaths (per 100,000)"] = data["TB deaths"] * 100 / data["Population (1000s)"]

    total = data["TB deaths"].sum()
    mean = data["TB deaths"].mean()
    median = data["TB deaths"].median()

    most_affected = data.sort_values(by=["TB deaths"], ascending=False)
    first_affected_country = most_affected['Country'].values[0]
    second_affected_country = most_affected['Country'].values[1]
    first_affected_deaths = most_affected['TB deaths'].values[0]
    second_affected_deaths = most_affected['TB deaths'].values[1]

    less_affected = data.sort_values(by=["TB deaths"], ascending=True)
    first_less_affected_country = less_affected['Country'].values[0]
    second_less_affected_country = less_affected['Country'].values[1]
    first_less_affected_deaths = less_affected['TB deaths'].values[0]
    second_less_affected_deaths = less_affected['TB deaths'].values[1]

    most_affected_by_100_hundred = data.sort_values(by=["TB deaths (per 100,000)"], ascending=False)
    first_affected_country_by_100_hundred = most_affected_by_100_hundred['Country'].values[0]
    second_affected_country_by_100_hundred = most_affected_by_100_hundred['Country'].values[1]
    first_affected_deaths_by_100_hundred = most_affected_by_100_hundred['TB deaths (per 100,000)'].values[0]

    less_affected_by_100_hundred = data.sort_values(by=["TB deaths (per 100,000)"], ascending=True)
    first_less_affected_country_by_100_hundred = less_affected_by_100_hundred['Country'].values[0]
    second_less_affected_country_by_100_hundred = less_affected_by_100_hundred['Country'].values[1]

    print(f"У всіх країнах світу було загинуто близько {round(total)} чоловік від туберкульозу у 2013 році. "
          f"Медіана показує, що половина цих країн мала менше {round(median)} смертей. Значно більша за "
          f"медіану середня величина ({round(mean)}) "
          "вказує на те, що деякі країни мали дуже велику кількість померлих від туберкульозу. Найменш постраждалими "
          f"{first_less_affected_country} і {second_less_affected_country},  що мають {first_less_affected_deaths} "
          f"і {second_less_affected_deaths} померлих відповідно, а найбільше постраждали {first_affected_country} і "
          f"{second_affected_country}, що мали {round(first_affected_deaths)}  і {round(second_affected_deaths)}  "
          f"померлих за один рік. Проте, беручи до уваги величину населення,"
          f" найменш постраждалими є {first_less_affected_country_by_100_hundred} "
          f"та {second_less_affected_country_by_100_hundred} з близькими до нуля смертністю на 100 тисяч жителів, а "
          f"найбільше постраждали {first_affected_country_by_100_hundred} та {second_affected_country_by_100_hundred} "
          f"з понад {round(first_affected_deaths_by_100_hundred)} смертельними випадками на 100 000 жителів. ")

    return


if __name__ == "__main__":
    main()