import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing
from requests.auth import HTTPProxyAuth


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    
    # proxies = {"http":"95.216.1.195:80"}
    # auth = HTTPProxyAuth("lsbsyotq-1", "na52i8iu1f54")
    headers = {
        'user-agent': 'Mozilla/5.0',
    }

    try:
        with closing(requests.get(url, stream=True, headers=headers)) as resp:
                return resp.content

    except RequestException as e:
        print(e)
        return None


def fetch_data(url_str, i):
    html = BeautifulSoup(simple_get(url_str), 'html.parser')
    # print(html.prettify())
    placeholder = html.select("p")[2].text.split()
    _type = placeholder[placeholder.index("character")+3]
    _name = ' '.join(html.select("h1 > a")[0].text.split())
    _show = ' '.join(html.select('p > a[href^="source.php"]')[0].text.split())
    _gender = html.findAll("span", {"style": "text-transform: lowercase;"})[0].text.split()[0].lower()
    print(i, '|', _name, '|', _show, '|', _gender, '|', _type)
    # print(_name)


def main():
    i = 1
    while True:
        try:
            fetch_data("http://www.animecharactersdatabase.com/characters.php?id=57067", i)
            break;
        except IndexError:
            pass
        i += 1


if __name__ == "__main__":
    main()