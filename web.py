from bs4 import BeautifulSoup
import requests
import lxml
from time import sleep
base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
"data.do?sortby=publicationDate&page="
books = []
NUM_PAGES = 31 # at the time of writing, probably more by now
for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num, ",", len(books), " found so far")
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text)
    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))
# now be a good citizen and respect the robots.txt!
    sleep(30)
