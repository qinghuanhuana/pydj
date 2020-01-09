from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    i = 0
    urls = ['https://movie.douban.com/top250?start=' + str(n) + '&filter=' for n in range(0, 250, 25)]
    for url in urls:
        a = 0
        r = requests.get(url)
        text = r.text
        soup = BeautifulSoup(text, 'html.parser')
        titles = soup.select('div.hd a')
        rates = soup.select('span.rating_num')
        pics = soup.select('img[width="100"]')
        pjs = soup.select('div.star span')
        for title, rate, pic, pj in zip(titles, rates, pics, pjs):
            data = {'title': list(title.stripped_strings),
                  'rate': rate.get_text(),
                  'pic': pic.get('src'),
                 'pj': pjs[3:: 4],
                'link' : title['href']}
            i += 1
            pj = data['pj'][a]
            pj = pj.get_text()
            a += 1
            fileName = str(i) + '_' + data['title'][0] + ' '+data['rate'] + '分' + ' ' + pj + '.jpg'
            pic1 = requests.get(data['pic'])
            with open('F:\\photo\\'+fileName, 'wb') as fp:
                fp.write(pic1.content)




