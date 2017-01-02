from bs4 import BeautifulSoup
from urllib import urlopen

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html,"html.parser")
namelist=bsObj.findAll(text="the prince")
print(namelist)
