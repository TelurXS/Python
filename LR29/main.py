import requests as req
import pandas as pd
import re
import bs4

URL = "https://www.holidify.com/explore/"


def main() -> None:

    # 1-3
    response = req.get(URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 4
    containers = soup.find_all("div", {"class" : "col-12"})
    print(len(containers))

    # 5
    country = []
    p_name = soup.find_all("h3", class_="card-heading")

    for name in p_name:
        p_nameN = name.text[4:].strip().split("-")
        nameN=p_nameN[0].strip().split(",")
        country.append(nameN[0])

    print(country)

    # 6
    ratings = []
    p_ratings = soup.find_all("span", class_="rating-badge")

    for p_rating in p_ratings:
        raiting = float(p_rating.b.text)
        ratings.append(raiting)

    print(ratings)

    # 7
    abouts = []
    p_abouts = soup.find_all("p", class_="card-text")

    for p_about in p_abouts:
        abouts.append(p_about.text.strip())

    print(abouts)

    # 8
    attractions = [] 
    p_attractions = soup.find_all("p", class_="collection-cta")

    for p_attraction in p_attractions:
        attraction = int(p_attraction.a.text.strip().split()[0])
        attractions.append(attraction)

    print(attractions)

    # 9
    column = ['Place', 'Ratings','About','Attraction']
    data = pd.DataFrame(list(zip(country, ratings, abouts, attractions)), columns = column)

    # 10
    data.to_csv("Places.csv", index = None)

    # 11
    print(data.sort_values(by="Ratings", ascending=False).head(10))

    # 12
    print(data.sort_values(by="Attraction", ascending=False).head(10))

    return


if __name__ == "__main__":
    main()