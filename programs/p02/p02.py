import requests
from protego import Protego
from lxml import etree
from io import StringIO, BytesIO
import urllib
import gzip

# PROGRAM 02

# 1
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'}


def get_rp(robot_txt_url):
    response = requests.get(robot_txt_url, headers=headers)
    rp = Protego.parse(response.text)
    print(rp)

    # url = "https://www.mozilla.org/sitemap.xml"
    # response = requests.get(url)
    # print(response.url)
    # root = etree.fromstring(response.content)
    # print(root)
    # sitemaps = [elem.text for elem in root.xpath("//sitemap/loc")]
    # for url in root.xpath("//url/loc"):
    #     print(url.text)


# TESTING OF PART 1
if __name__ == "__main__":
    rp = get_rp('https://www.mozilla.com/robots.txt')
    # print(rp.can_fetch("https://www.mozilla.org/", "mybot"))
    # print(rp.crawl_delay('*'))
    # print(response.content)
    # print(response.url)
    # print(response.ok)
#
# if __name__ == "__main__":
#     rp2 = get_rp('https://www.amazon.es/robots.txt')
#     print(rp2)
#     print(rp2.crawl_delay('*'))
#     print(rp2.can_fetch("https://www.amazon.es/", "mybot"))
#     sitemaps2 = list(rp2.sitemaps)
#     print(sitemaps2)
#     print(len(sitemaps2))
# 2.1
# amazon.es ZIPPED XML
# mozilla.com NON_ZIPPED XML

# 2.2



def parse_sitemap_index(url):
    response = requests.get(url)
    root = etree.fromstring(response.content)
    sitemaps = [elem.text for elem in root.xpath("//sitemap/loc")]
    return sitemaps


def parse_sitemap(url):
    response = requests.get(url)
    root = etree.fromstring(response.content)
    urls = [elem.text for elem in root.xpath("//url/loc")]
    return urls

sitemap_index_url = "https://www.mozilla.org/sitemap.xml"
sitemap_urls = parse_sitemap_index(sitemap_index_url)

for sitemap_url in sitemap_urls:
    urls = parse_sitemap(sitemap_url)
    print(urls)
# 2.3
