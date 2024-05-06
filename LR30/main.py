import requests as req
from selenium import webdriver
import bs4
import pandas as pd

URL = "https://www.x-rates.com/calculator/?from=GBP&to=USD&amount=1"

def task1() -> None:
    
    amount = float(input("Input amount: "))

    response = req.get(URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    def gbp_to_usd(rate,gbp):
        dollars=gbp * rate
        return dollars

    part1 = soup.find(class_="ccOutputTrail").previous_sibling
    part2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
    rate = float("{}{}".format(part1,part2))
    print("Current rate :", part1)
    print(f"{amount} GBP is equvalent to {gbp_to_usd(rate, amount)}$")
    return

USD = "USD"
EUR = "EUR"
PLN = "PLN"
GBP = "GBP"

CURRENCIES = [USD, EUR, PLN, GBP]

BANK = "Bank"
CURRENCY = "Currency"
TYPE = "Type"
VALUE = "VALUE"

def task2() -> None:

    data = pd.DataFrame(columns=[BANK, TYPE, CURRENCY, VALUE])

    # Minfin
    minfin_res = req.get("https://minfin.com.ua/ua/currency/")
    minfin_soup = bs4.BeautifulSoup(minfin_res.text, "html.parser")

    table = minfin_soup.find("div", class_="sc-1x32wa2-0 dWgyGF bvp3d3-10 bvp3d3-11 kNRLfR cLIHts").table.tbody

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        currency = cells[0].text

        if currency not in CURRENCIES:
            continue

        buy = cells[1].find_all(string=True)[0]
        sell = cells[2].find_all(string=True)[0]

        data.loc[len(data)] = {BANK: "Minfin", TYPE: "Buy", CURRENCY: currency, VALUE: buy}
        data.loc[len(data)] = {BANK: "Minfin", TYPE: "Sell",CURRENCY: currency, VALUE: sell}

    # PrivatBank
    driver = webdriver.Chrome()
    driver.get("https://next.privat24.ua/exchange-rates")
    driver.implicitly_wait(30)
    privat_soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    table = privat_soup.find("div", class_="sc-dlWCHZ bYtdBK").find_all("div", recursive=False)[2]
    rows = table.find_all("div", recursive=False)[1]
    
    for row in rows.find_all("div", class_="root__qLrNeW4jK"):
        currency = row.find("div", class_="currency_b_C9i_wbMZ").find("div", class_="content_w73Ioj4XNI").div.text

        if currency not in CURRENCIES:
            continue

        buy = row.find_all("div", class_="rate_kx9iSqCXBH")[0].text
        sell = row.find_all("div", class_="rate_kx9iSqCXBH")[1].text

        data.loc[len(data)] = {BANK: "Privat", TYPE: "Buy", CURRENCY: currency, VALUE: buy}
        data.loc[len(data)] = {BANK: "Privat", TYPE: "Sell",CURRENCY: currency, VALUE: sell}

    data.to_csv("currencies.csv", index=False)
    return

def main() -> None:
    task2()
    return


if __name__ == "__main__":
    main()
    