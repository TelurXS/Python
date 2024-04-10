import matplotlib.pyplot as plt
import pandas as pd


def get_sales_data():
    return pd.read_csv("sales_data.csv")


def task1() -> None:
    data = get_sales_data()

    plt.plot(data["month_number"], data["total_profit"], "r--", linewidth=3, marker="o", mfc="black", mec="red")
    plt.title("y=x", fontsize=10)
    plt.xlabel("month_number", fontsize=10)
    plt.legend("Profit data of last year", loc="lower right", fontsize=12, title="pfa")
    plt.grid()

    plt.show()
    return


def main() -> None:
    task1()
    return


if __name__ == "__main__":
    main()