from bs4 import BeautifulSoup
import requests
import pandas as pd


def bbc_scrap():
    bbc_headlines = []
    bbc_urls = []
    bbc_images = []
    bbc_summary = []

    source_page = 'https://www.bbc.com/news/live/world-asia-india-47640058/page/'

    for page in range(1, 51):
        web_page = source_page + str(page)
        response = requests.get(web_page).text
        soup = BeautifulSoup(response, 'lxml')

        for news in soup.find_all('li', class_='lx-stream__post-container'):
            try:
                headlines = news.article.h3.text
                links = news.article.header.h3.a['href']
                urls = f'https://www.bbc.com{links}'
                images = news.img['src']
                summary = news.article.find('p', class_='lx-stream-related-story--summary').text
            except Exception as e:
                headlines = None
                urls = None
                images = None
                summary = None
            bbc_headlines.append(headlines)
            bbc_urls.append(urls)
            bbc_images.append(images)
            bbc_summary.append(summary)

    data = {'headlines': bbc_headlines, 'urls': bbc_urls, 'images': bbc_images, 'summary': bbc_summary}

    bbc_df = pd.DataFrame(data, columns=data.keys())
    bbc_df.dropna(axis=0, how='any', inplace=True)

    return bbc_df


def toi_scrap():
    toi_news_hints = []
    toi_urls = []

    toi_source_page = 'https://timesofindia.indiatimes.com/india'

    for page in range(1, 13):
        if page == 1:
            toi_web_page = toi_source_page
        else:
            toi_web_page = toi_source_page + '/' + str(page)
        response = requests.get(toi_web_page).text
        toi_soup = BeautifulSoup(response, 'lxml')

        toi_news_list = toi_soup.find_all('ul', class_=['top-newslist clearfix', 'list5 clearfix'])

        for separation in toi_news_list:
            for summary in separation.find_all('li'):
                news_hint = summary.find('span', class_='w_tle').a.text
                links = summary.find('span', class_='w_tle').a['href']
                urls = f'https://timesofindia.indiatimes.com{links}'

                toi_news_hints.append(news_hint)
                toi_urls.append(urls)

    data = {'toi_news': toi_news_hints, 'toi_urls': toi_urls}

    toi_df = pd.DataFrame(data, columns=data.keys())
    toi_df.dropna(axis=0, how='any', inplace=True)

    return toi_df
