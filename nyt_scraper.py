from bs4 import BeautifulSoup
import urllib2

needle = "trump"
needle_count = 0
found_needle = False

r = urllib2.urlopen('http://www.nytimes.com/').read()
soup = BeautifulSoup(r)

news_item_tags = soup.find_all("h2", {"class": "story-heading"})
news_items = []

for elem in news_item_tags:
	news_items.append(elem.get_text())

print news_items

for item in news_items:
	if needle in item.lower():  # making it lower case is key!
		found_needle = True
		needle_count += 1

print "How many %s's in the news today? %d" % (needle, needle_count)
