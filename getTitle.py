from bs4 import BeautifulSoup
from urllib import urlopen
from urllib2 import  HTTPError

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html.read(), "html.parser")
        title=bsObj.title
    except AttributeError as e:
        return None
    return title
title=getTitle("http://www.baidu.com")
if title==None:
    print ("Title can not be found.")
else:
    print (title)
