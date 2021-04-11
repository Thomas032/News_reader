import requests #must have
from bs4 import BeautifulSoup #must have
from collections import Counter # module for recognising duplicates (non needed since i found better solution)
import pyttsx3 #module for reading the news

engine = pyttsx3.init()

def get_data():
    URL = "https://www.bbc.com/news"
    page = requests.get(URL)
    lin = []
    news = []
    soup = BeautifulSoup(page.text, 'html.parser')
    h1 = soup.find_all('h3', class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")
    links = soup.find_all('a', class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")
    try:
        banger = soup.find("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")

        banger_link = soup.find("a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor")
        news.append(banger.text)
        lin.append(banger_link.get("href"))
    except:
        print("No banger found ! passing to regular news")
        pass
    
    for new in h1:
        news.append(new.text)
    for link in links:
        lin.append(link.get("href"))
    
    return news , lin


     
def read(news, lin):
    news = list(dict.fromkeys(news))#deleting dupliacates
    news = news[:7] 
    for i in range(len(news)):
        report = news[i]
        odkaz = lin[i]
        if "/news" in odkaz:
            
            print(f"{report} ---> https://www.bbc.com/{odkaz}")
            engine.say(report)
            engine.runAndWait()
            
            
    
    
news, lin = get_data()
read(news, lin)



# debugging:
#report =parse_data(news, lin)
#read_data(report)
# report  = all the news that can be read because there is no dumb or useless titles 
        




