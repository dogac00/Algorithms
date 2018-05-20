import requests
from bs4 import BeautifulSoup
import operator

def start(url):
  word_list = []
  source_code = requests.get(url).text
  soup = BeautifulSoup(source_code) # we care about only text
  for post_text in soup.findAll('a', {'class': 'index_singleListingTitles''}):
    content = post_text.string
    words = content.lower().split() # we just want words
    for each_word in words:
      print(each_word)
      words_list.append(each_word)

def clean_up_list(word_list):
  clean_word_list = []
  for word in word_list:
    symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='"
    for i in range(0, len(symbols)):
      word = word.replace(symbols[i], "")
    if len(word) > 0:
      print(word)
      clean_word_list.append(word)
      
start(url) # fill this with your url
