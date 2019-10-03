from bs4 import BeautifulSoup
import requests

news_url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen'

def data():
    page = requests.get(news_url)
    soup = BeautifulSoup(page.content, 'html5lib')
    out = soup.find_all('h3', class_ = 'ipQwMb ekueJc RD0gLb')
    news = []
    for i in out:
        news.append(i.string)
    with open("news.csv","w",encoding='utf-8') as f:
        for i in news:
            f.write(i)
            f.write('\n')