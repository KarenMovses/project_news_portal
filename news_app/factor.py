from requests_html import HTMLSession
from datetime import datetime


def get_news_factor():
    url = "https://factor.am/"

    session = HTMLSession()

    r = session.get(url=url)

    news_list = list()

    news_feed = r.html.find('#newsfeed', first=True)

    for news in news_feed.find('.item-post'):
        single_news_dict = {
            'news_site_name': news.base_url.split('/')[2].title(),
            'news_url': list(news.absolute_links)[0],
            'news_date': news.text.split('\n')[0].replace('|', ''),
            'news_text': news.text.split('\n')[1],
            'update_time': datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        }

        news_list.append(single_news_dict)
        
    return news_list



