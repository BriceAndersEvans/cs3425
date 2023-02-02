import requests
from lxml import etree
from protego import Protego

# Get the robots.txt file for mozilla.com
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'}
robots_url = "https://www.mozilla.org/robots.txt"
robots = requests.get(robots_url, headers=headers)
print(robots)
# Parse the robots.txt file to see if it's okay to scrape the sitemap
okay_to_scrape, _ = Protego.parse(robots.txt)

# If it's okay to scrape the sitemap, continue
if okay_to_scrape:
    # Get the sitemapindex for mozilla.com
    sitemap_index_url = "https://www.mozilla.org/sitemap.xml"
    sitemap_index = requests.get(sitemap_index_url).text

    # Parse the sitemapindex
    sitemap_index_root = etree.fromstring(sitemap_index)

    # Get the list of sitemaps from the sitemapindex
    sitemaps = [loc.text for loc in sitemap_index_root.xpath("//sitemap/loc")]

    # Loop through each sitemap
    for sitemap_url in sitemaps:
        sitemap = requests.get(sitemap_url).text
        sitemap_root = etree.fromstring(sitemap)

        # Get the list of URLs from the sitemap
        urls = [loc.text for loc in sitemap_root.xpath("//url/loc")]

        # Print the URLs
        print(urls)
else:
    print("It is not okay to scrape the sitemap for mozilla.com.")

# import requests
# from lxml import etree
# from robotexclusionrulesparser import RobotExclusionRulesParser
#
# # Get the robots.txt file for mozilla.com
# robots_url = "https://www.mozilla.org/robots.txt"
# robots = requests.get(robots_url).text
# # print(robots)
#
# # Parse the robots.txt file using the robotexclusionrulesparser library
# robots_parser = RobotExclusionRulesParser()
# robots_parser.parse(robots)
# # print(robots_parser.parse(robots))
#
# # Determine if it's okay to scrape the sitemap
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'}
# okay_to_scrape = robots_parser.is_allowed("https://www.mozilla.org/sitemap.xml", "*")
# # print(okay_to_scrape)
#
# # If it's okay to scrape the sitemap, continue
# if okay_to_scrape:
#     # Get the sitemapindex for mozilla.com
#     sitemap_index_url = "https://www.mozilla.org/sitemap.xml"
#     sitemap_index = requests.get(sitemap_index_url).text
#     # print(sitemap_index)
#
#     # Parse the sitemapindex
#     sitemap_index_root = etree.fromstring(sitemap_index.encode("utf-8"))
#     print(sitemap_index_root)
#
#     # Get the list of sitemaps from the sitemapindex
#     sitemaps = [loc.text for loc in sitemap_index_root.xpath("//sitemap/loc")]
#     print("List of sitemaps:", sitemaps)
#
#     # Loop through each sitemap
#     for sitemap_url in sitemaps:
#         sitemap = requests.get(sitemap_url).text
#         sitemap_root = etree.fromstring(sitemap)
#         print(sitemap)
#         print(sitemap_root)
#
#         # Get the list of URLs from the sitemap
#         urls = [loc.text for loc in sitemap_root.xpath("//url/loc")]
#
#         # Print the URLs
#         print(urls)
# else:
#     print("It is not okay to scrape the sitemap for mozilla.com.")