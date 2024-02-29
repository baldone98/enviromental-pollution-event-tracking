from GoogleNews import GoogleNews
import xml.etree.ElementTree as ET
googlenews = GoogleNews()

#googlenews.search("climate change")

#the search query
query = "air pollution breath Tennessee"

# Get 10 first qrticles
articles_number = 200
all_articles = []
all_links = []
page_num = 1
while len(all_articles) <= articles_number:
  googlenews.search(query)
  articles = googlenews.get_texts()
  links = googlenews.get_links()
  all_articles.extend(articles)
  all_links.extend(links)
  googlenews.clear()
  page_num += 1
  articles_curr_page = googlenews.get_page(page_num)
print(len(all_articles))
f = open("articles.csv", "w")
for i in range(articles_number):
  f.write('"'+all_articles[i] +'"'+ "," + all_links[i] + "\n")
f.close()
