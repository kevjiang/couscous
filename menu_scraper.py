from bs4 import BeautifulSoup
import urllib2

needle = "chicken"
found_needle = False

r = urllib2.urlopen('http://phillipsacademy.campusdish.com/Commerce/Catalog/Menus.aspx?LocationId=4236&PeriodId=2056&MenuDate=2016-07-06&UIBuildDateFrom=2016-07-06').read()
soup = BeautifulSoup(r)

menu_item_tags = soup.find_all("span", {"class": "menu-item-name"})
menu_items = []

for elem in menu_item_tags:
	menu_items.append(elem.get_text())

print menu_items

for item in menu_items:
	if needle in item.lower():  # making it lower case is key!
		found_needle = True
		break

print "Today is %s day: %s" % (needle, found_needle)
