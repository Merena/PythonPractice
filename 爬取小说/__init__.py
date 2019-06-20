import requests
import parsel
import urllib.parse
import re


def get_one_chapter(chapter_url, book_name):
    sel = parsel.Selector(get_html(chapter_url))
    chapter_title = sel.css('div.content > h1::text').get()
    content = sel.css('#content::text').getall()
    print(chapter_title)

    with open(book_name + '.txt', 'a', encoding='utf-8') as f:
        f.write(chapter_title)

        for con in content[:-3]:
            # print(con)
            f.write(con)


def get_html(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    return response.text


def get_one_book(bookUrl):
    sel = parsel.Selector(get_html(bookUrl))
    content = sel.xpath('//div[5]/dl/dd/a/@href').getall()
    book_name = sel.css('body > div.book > div.info > h2::text').get()

    for chapterUrl in content:
        get_one_chapter(re.sub('index.html', chapterUrl, bookUrl), book_name)


if __name__ == '__main__':
    get_one_book('http://www.shuquge.com/txt/8072/index.html')


