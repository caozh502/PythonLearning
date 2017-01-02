import urllib


def read_text():
    quotes = open(r"C:\Users\Pi\Desktop\abc.txt")
    contents=quotes.read()
    print(contents)
    quotes.close()
    check(contents)

def check(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    print (output)
    connection.close()


read_text()