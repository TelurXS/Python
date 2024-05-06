import bs4
import requests


def task1() -> None:

    URL_TEMPLATE = " https://www.work.ua/jobs-poltava/?setlp=ua"

    # 2
    r = requests.get(URL_TEMPLATE)
    print(r.status_code)

    # 3
    print(r.text)

    # 4
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())

    # 6
    vacancies_names = soup.find_all('h2', class_='cut-top cut-bottom')

    for name in vacancies_names:
        print(name.a["title"])  

    # 7
    for name in vacancies_names:
        print(name.a['title'].split(', вакансія')[0])

    # 8
    for name in vacancies_names:
        print(name.a['title'].split(', вакансія')[0]+": "+ 'https://www.work.ua'+name.a['href'])

    # 9
    vacancies_info = soup.find_all('p', class_='ellipsis ellipsis-line ellipsis-line-3 text-default-7 cut-bottom')

    for info in vacancies_info:
        print(info.text.strip())

    # 10
    salary_info = soup.find_all('span', class_='strong-600')

    for info in salary_info:
        print(info.text.strip())
    return


def task2() -> None:

    URL_TEMPLATE = "https://jobs.ua/city/poltava_jobs"

    r = requests.get(URL_TEMPLATE)
    
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    vacancies_info = soup.find_all("div", class_="b-vacancy__top")

    for info in vacancies_info:
        vacancy = info.find("div", class_="b-vacancy__top-inner").h3.a.text
        salary = ''.join(info.span.find_all(text=True))
        company = info.find("div", class_="b-vacancy__tech").span.span.text
        print(f"{vacancy} ({company}): {salary}")
    return


def main() -> None:
    task2()
    return


if __name__ == "__main__":
    main()