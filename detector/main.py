import requests
from detector import detect
from bs4 import BeautifulSoup 

# instagram URL
URL = "https://www.instagram.com/{}/"


# scrape function
def scrape_data(username): 
      
    r = requests.get(URL.format(username)) 
      
    s = BeautifulSoup(r.text, "html.parser") 
      
    meta = s.find("meta")
    print(meta)
    
    return meta.attrs['content'] 


def download_image(url):
    r = requests.get(url)
    file = open("static/sample.png", "wb")
    file.write(r.content)
    file.close()


def run(username):
    d = scrape_data(username)
    download_image(d)
    return detect.detect_face()
