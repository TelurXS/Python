import pandas as pd


def task1() -> None:
    populations = {
        "Kyiv": 2_967_360,
        "Kharkiv": 1_443_207,
        "Odesa": 1_017_699,
        "Dnipro": 990_724,
        "Donetsk": 908_456,
        "Zaporishya": 731_922,
        "Lviv": 717_273,
        "Kryvyi Rih": 619_278,
        "Mykolaiv": 480_080,
        "Sevastopol": 449_138
    }
    population = pd.Series(populations)

    print(population)
    print(population.max())
    print(population.min())
    print(population.mean())
    print(population["Kyiv"])
    print(population.head(5))
    population["Poltava"] = 286_649
    print(population[population > 1_000_000])
    print(population[populations.keys()])
    return


def task2() -> None:

    towns = pd.DataFrame({
        "town": ["Шанхай", "Пекін", "Тяньцзінь", "Стамбул", "Лагос", "Ґуанчжоу", "Мумбаї", "Дакка", "Каїр", "Сан-Паулу"],
        "population": [24_150_000, 21_516_000, 14_722_100, 14_377_019, 13_400_000, 12_700_800, 12_655_220, 12_043_977, 11_922_949, 11_895_893],
        "square": [6340.5, 16410.54, 4037, 5461, 999.58, 3843.43, 603.4, 1463.6,	3085.1,	1521.11],
        "country": ["КНР", "КНР", "КНР", "Туреччина", "Нігерія", "КНР", "Індія", "Бангладеш", "Єгипет", "Бразилія"]
    })

    print(towns)
    towns["density"] = towns["population"] / towns["square"]
    print(towns)
    print(towns[["town", "country"]])
    print(towns.head(5))
    towns.set_index("town", inplace=True)
    print(towns.loc["Стамбул"])
    print(towns[towns.population > 12_000_000])
    print(towns[towns.square > 5000])
    print(towns[towns.country == "КНР"])
    return


def main() -> None:
    task2()
    return


if __name__ == "__main__":
    main()
