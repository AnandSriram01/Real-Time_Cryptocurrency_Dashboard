import requests
import pprint
from bs4 import BeautifulSoup as soup

# keyword = input("Enter keyword : ")
# print(keyword)

baseURL = 'https://cryptonews.net'
URL = 'https://cryptonews.net/en/search/?q=btc'

page = requests.get(URL)

bsobj = soup(page.content, 'html.parser')

# print(bsobj.prettify())

# News Snippets

# for item in bsobj.find_all("p", class_="sc-1eb5slv-0 hdUmWM"):
#     print(item)

# Headlines

# for item in bsobj.find_all("a", class_="sc-1eb5slv-0 kUvkfN cmc-link"):
#     print(item.text)

# for item in bsobj.find_all("a", class_="title"):
#     print("Headline : ", item.text.strip())
#     # print("URL : ", item['href'])

divTag = bsobj.find_all("div", class_="row news-item start-xs")

# print(divTag)

dictobj = []
count = 1

for i in range(5) :
    print(i)
    tag = divTag[i]
    span = tag.find("span", class_="datetime flex middle-xs")
    time = span.text.strip()
    a = tag.find("a", class_="title")
    headline = a.text.strip()
    snippetURL = a['href']
    sourceURL = tag['data-link']

    newsURL = baseURL + snippetURL
    page2 = requests.get(newsURL)
    bsobj2 = soup(page2.content, 'html.parser')
    divTag2 = bsobj2.find("div", class_="news-item detail content_text")
    p = divTag2.find("p")
    snippet = p.text.strip()

    dictobj.append({"headline":headline, "time":time, "snippet":snippet, "snippetURL":snippetURL, "sourceURL":sourceURL})
    # print(dictobj)
    # print("Headline :- ")
    # print(headline)
    # print(time)
    # print(snippetURL)
    # print(sourceURL)

pprint.pprint(dictobj)
