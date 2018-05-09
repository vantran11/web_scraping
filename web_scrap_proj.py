
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 

url =      "https://www.yelp.com/search?find_loc=60607"

soup = BeautifulSoup(requests.get(url).text, 'lxml')

links = soup.find_all("a")

rating_links=  [a_tag.get('title') for a_tag in soup.find_all('div')]

reviews_links=soup.find_all('span')

type_links=[a_tag.get('href') for a_tag in soup.find_all('a')]

review_links_2 = [span_tag.getText() for span_tag in reviews_links]
