import requests
from bs4 import BeautifulSoup


#print (len(soup('p')))
#print (soup('p', {'align' : 'center'}))
# About us
def about_us():
	url_to_scrape ="https://www.docnme.com/about/"
	r = requests.get(url_to_scrape)
	soup = BeautifulSoup(r.text,"lxml")
	tags=soup.find_all(id='content')
	text = [t.get_text() for t in tags]
	#print (str(len(text))+' posts were found')
	print (text[0])
	



#main
url_to_scrape ="https://www.docnme.com/"
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text,"lxml")
titleTag = soup.html.head.title
#print (titleTag)
#title name
print ("Company Title"+titleTag.string)
lettes=soup.find_all(class_="menu-item menu-item-type-post_type menu-item-object-page")
print ("href to About features ,Contact") 
print(lettes)
#Call about us
about_us()