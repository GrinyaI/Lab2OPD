from bs4 import BeautifulSoup
import requests

def parse(name):
    url = 'https://farmakopeika.ru/search?query='+str(name)

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.example'
    }
    page = requests.get(url, headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('div', class_='product__body')

    namoflec = []
    pricoflec = []
    haveornot = []
    urs = []

    for data in block:
        nam = data.find(class_='product__title')
        have = data.find(class_='product__spec-value')
        price = data.find(class_='product__price-text')
        ul = data.find(class_='product__link')['href']

        if nam is not None:
            namoflec.append(nam.text.replace("\n",""))
        else:
            namoflec.append('-')

        if price is not None:
            pricoflec.append(price.text.replace("\n","") + ' р.')
        else:
            pricoflec.append('-')

        if have is not None:
            haveornot.append(have.text.replace("\n",""))
        else:
            haveornot.append('-')

        if ul is not None:
            urs.append(ul)
        else:
            urs.append('-')

    print(namoflec, pricoflec, haveornot, urs)
    return [namoflec, pricoflec,haveornot,urs]