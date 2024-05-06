import bs4
import requests
from collections import Counter

html_doc = """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;
        charset=iso-8859-1">
        <title>An example of HTML page</title>
    </head>
    <body>
        <h2>This is an example HTML page</h2>
        <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
        aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
        habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
        sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
        Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
        adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
        elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
        imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
        euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
        euismod porta.</p>
        <p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
        w3resource.com</a></p>
        <p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
        w3resource.com</a>
        </p>
    </body>
</html>
"""

def task2() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(soup.find("title"))
    return


def task3() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(soup.find_all("p"))
    return


def task4() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(len(soup.find_all("p")))
    return


def task5() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(soup.find_all("p")[0].text)
    return


def task6() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(soup.find_all("a")[0].text)
    return


def task7() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(soup.find_all("a")[0].attrs["href"])
    return


def task8() -> None:
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    print(soup.select(".sister"))
    return


def task9() -> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    print(reqs)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for h in soup.find_all('li'):
        a = h.find('a')
        urls.append(a.attrs['href'])
    print(urls)
    return


def task10()-> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    print(reqs)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    headers = soup.find_all('h2')
    print(headers[:10])
    return


def task11()-> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    headers = soup.find_all(['h1', 'h2', 'h3'])
    for header in headers:
        print(f"{header.name.strip()} {header.text.strip()}")
    return


def task12()-> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')
    print(soup.get_text())
    return


def task13()-> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    elements = []
    for child in soup.recursiveChildGenerator():
        if child.name:
            elements.append(child.name)
            print(child.name)

    print(set(elements))
    print(Counter(elements))
    return


def task14()-> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    root = soup.html    
    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)


def task15() -> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    items = soup.find_all('li')

    for item in items:
        print(f"{item.name} {item.text.strip()}")
    return


def task16() -> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    items = soup.find_all(string="Python")

    for item in items:
        print(item)
    return

def task17() -> None:
    url = 'https://www.python.org/'
    reqs = requests.get(url)
    soup = bs4.BeautifulSoup(reqs.text, 'html.parser')

    print(soup.prettify())
    return



def main() -> None:
    task17()
    return


if __name__ == "__main__":
    main()