# headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'}
# response = requests.get('https://www.pinterest.com/robots.txt', headers=headers)
# response.text
# response.ok
# response.json()

# sitemap = sitemaps[0]
# print(response.text)
# root = etree.XML(bytes(response.text, 'UTF-8'))
#
# for child in root:
#     print(child.tag)
#
# rp = Protego.parse(response.text)
# rp
#
# list(rp.sitemaps)
# rp.can_fetch('https://www.pinterest.com/pin/create/', '*')
#
# rp.crawl_delay('*')
#
# root = etree.XML(requests.content)

import requests
from protego import Protego
from lxml import etree

# headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'}
# def get_rp('https://www.mozilla.com/robots.txt'):
#     r = requests.get('https://www.mozilla.com/robots.txt', headers=headers)
#     rp = Protego.parse(r.text)
#     print("hi")
#     rp.crawl_delay('*')
#     print(rp.sitemaps)
#     return rp


# responses = requests.get('https://www.mozilla.com/robots.txt', headers=headers)
# print(responses.text)
# r = requests.get('https://www.mozilla.com/robots.txt', headers=headers)
# rp = Protego.parse(r.text)
# print(rp)
# rp.crawl_delay('*')
# print(rp.sitemaps)



# THIS IS THE WEBSITE PORTION

# def my_hash(username):
#     import hashlib
#     m = hashlib.sha256()
#     m.update(bytes(username, 'utf-8'))
#     return int(m.hexdigest()[:16], 16)

# websites = [
# 'addthis.com', 'ea.com', 'fandom.com', 'harvard.edu', 'jimdo.com',
# 'lexpress.fr', 'mozilla.com', 'nih.gov', 'opera.com', 'plos.org',
# 'sedo.com', 'thenai.org', 'translate.google.com', 'usnews.com',
# 'whitehouse.gov', 'wp.com', 'wsj.com', 'www.google.com', 'zendesk.com',
# ]

# websites = [
# 'amazon.es', 'engadget.com', 'news.yahoo.com', 'themeforest.net',
# 'www.gov.br', 'youtube.com', 'picasa.google.com', 'who.int',
# ]

# username = 'evansba2'
# index = my_hash(username) % len(websites)
# url = websites[index]
# print(f'The website for user "{username}" is {url}')

# amazon.es ZIPPED XML
# mozzila.com NON_ZIPPED XML


# USER-AGENT *
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.119 Safari/537.36
# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0