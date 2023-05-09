import requests
from bs4 import BeautifulSoup
import chardet
import re

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def get_links(url):

    response = requests.get(url, headers=headers)
    encoding = chardet.detect(response.content)['encoding']
    response.encoding = encoding
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    pairs = []

    for link in links:
        href = link.get('href')
        text = re.sub(r"[\n\t]","",link.text)
        pairs.append((text, href))

    return pairs


print(get_links("https://www.qq.com/"))