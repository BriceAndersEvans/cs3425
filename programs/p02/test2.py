import requests
from protego import Protego
from lxml import etree

# PART 1
#########

def get_rp(robots_url):
    headers = {'User-Agent': 'my-user-agent'}
    response = requests.get(robots_url, headers=headers)
    parsed = Protego.parse(response.text)
    return parsed

# Test Case #1 for Part One
rp = get_rp('https://www.hockey-reference.com/robots.txt')
rp.crawl_delay('*')
rp.can_fetch('https://www.hockey-reference.com/boxscores/index', '*')
rp.can_fetch('https://www.hockey-reference.com/boxscores/202210260ANA.html', '*')
print(rp)

# Test Case #2 for Part One
rp1 = get_rp("http://mozilla.com")
print(rp1)

# Test Case #3 for Part One
rp2 = get_rp("http://amazon.es")
print(rp2)


# PART 2.1
##########
# Non-gz = mozilla.com
# gz = amazon.com

# PART 2.2
############
def get_xml_sitemap_urls(robots_url, website):
    rp = get_rp(robots_url)
    sitemaps = rp.sitemaps()
    urls = []
    while sitemaps:
        sitemap = sitemaps.pop()
        if rp.can_fetch(sitemap, '*'):
            response = requests.get(sitemap)
            if response.headers['Content-Type'].startswith('application/xml'):
                tree = etree.fromstring(response.content)
                if tree.tag == 'sitemapindex':
                    for child in tree:
                        sitemaps.append(child.findtext('loc'))
                elif tree.tag == 'urlset':
                    for child in tree:
                        loc = child.findtext('loc')
                        urls.append(loc)
    with open(f'{website}.urls.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')



# TEST CASE #1 for PART 2.2
get_xml_sitemap_urls('https://www.mozilla.com/robots.txt', 'mozilla.com')

