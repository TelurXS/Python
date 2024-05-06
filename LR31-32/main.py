import bs4
import pandas as pd
import requests as req
import re
import datetime

URL = "https://books.toscrape.com/catalogue"

def strip_to(string: str, ch: str):
    found = string.find(ch)

    if found > 0: 
        return string[0:found].strip()
    
    return string

CLEAN_EXPRESSION = re.compile(r'[-_0-9]+')

def clean_string(input_string: str) -> str:
    result = CLEAN_EXPRESSION.sub(' ', input_string)
    result = result.title()
    return result.strip()

EXTRACT_EXPRESSION = re.compile(r'\d+')

def extract_numbers(input_string: str) -> int:
    numbers = EXTRACT_EXPRESSION.findall(input_string)
    
    try:
        return int(numbers[0])
    except:
        return 0

RATINGS = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

def main() -> None:

    count = 1
    
    while True:
        res = req.get(f"https://books.toscrape.com/catalogue/page-{count}.html")
        print(f"{count}: {res.status_code}")
    
        if res.status_code != 200:
            break
    
        count += 1
    
    print(count)

    scraping_date = datetime.date.today()    
    all_books = []

    for i in range(1, count):
        print(f"Parsing page: {i}")

        res = req.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        all_articles = soup.find_all('article')

        for article in all_articles:
  
            b_title = article.find("h3").a.text
            b_title = strip_to(b_title, '(')
            b_title = strip_to(b_title, ':')

            b_href  = URL + "/" + article.find("a")["href"]

            price_info = article.find("div", class_="product_price")

            b_rtg = article.find("p", class_="star-rating")["class"][1]
            rating = RATINGS[b_rtg]

            b_stock = price_info.find("p", class_="availability").text.strip().replace(" ", "")
            b_price = price_info.find("p", class_="price_color").text.replace("Â£", "$")

            res = req.get(b_href)
            book_soup = bs4.BeautifulSoup(res.text, 'html.parser')

            p_categ = book_soup.find("a", href=re.compile("../category/books/")).get("href").split("/")[3]
            p_categ = clean_string(p_categ)

            p_count = book_soup.find("p", class_="instock availability").text.strip()
            p_count = extract_numbers(p_count)

            all_books.append([b_title, b_href, rating, b_stock, b_price, p_categ, p_count])

    data = pd.DataFrame(all_books, columns=["Title", "Href", "Rating", "Stock", "Price", "Category", "Count"])
    print(data.head(5))
    data.to_csv(f"books-{scraping_date}.csv", index=False)

    return


if __name__ == "__main__":
    main()