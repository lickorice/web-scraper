import urllib.request
from bs4 import BeautifulSoup

def simple_get(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    return con.read()


def fetch_data(url_str, i):
    html = BeautifulSoup(simple_get(url_str), 'html.parser')
    _name = ' '.join(html.findAll("span", {"itemprop": "name"})[4].text.split())
    _show = ' '.join(html.findAll("td", {"class": "name anime"})[0].text.split())
    _gender = ' '.join(html.findAll("span", {"itemprop": "gender"})[0].text.split())
    print(i, '|', _name, '|', _show, '|', _gender)


def main():
    i = 1
    while True:
        try:
            fetch_data("https://anidb.net/perl-bin/animedb.pl?show=character&charid={}".format(i), i)
        except IndexError:
            pass
        i += 1


if __name__ == "__main__":
    main()