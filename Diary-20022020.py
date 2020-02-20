Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> CREATE TABLE User()
SyntaxError: invalid syntax
>>> 
>>> 
KeyboardInterrupt
>>> CREATE TABLE Users(name VARCHAR(128),email VARCHAR(128))
SyntaxError: invalid syntax
>>> 
>>> 
	
KeyboardInterrupt
>>> import urllib2

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    import urllib2
ModuleNotFoundError: No module named 'urllib2'
>>> import requests
>>> 
KeyboardInterrupt
>>> import re
>>> import time
>>> def webCrawl(link):
    L = [(link,["start page"])]
    stack = [link]
    while len(stack) > 0 :
        templink = stack.pop(0)
        try:
            temp  = str(requests.get(templink).content)
        except:
            print("Eror for {}".format(templink))
            pass
        templist = re.findall("<a href=\"(https?:[^ ]+)\">",temp)
        for newlink in templist:
            found = False
            for pastlink in L:
                if(pastlink[0] == newlink):
                    pastlink[1].append(templink)
                    found = True
                    break
            if(not found and  not newlink in stack):
                stack.append(newlink)
                L.append((newlink,[templink]))
        print("Crawling {} got : {}".format(templink,templist))
    return L

>>> def printCrawl(crawl):
    change = True
    while(change):
        change = False
        for i in range(len(crawl)-1):
            if (len(crawl[i][1]) > len(crawl[i+1][1])):
                temp = crawl[i]
                crawl[i] = crawl[i+1]
                crawl[i+1] = temp
    for t in crawl:
        print("link {} is linked to:".format(t[0]))
        for k in t[1]:
            print("   -{}".format(k))

            
>>> def Crawler(link):
	    printCrawl(webCrawl(link))

	    
>>> def printCrawl(crawl):
    change = True
    while(change):
        change = False
        for i in range(len(crawl)-1):
            if (len(crawl[i][1]) > len(crawl[i+1][1])):
                temp = crawl[i]
                crawl[i] = crawl[i+1]
                crawl[i+1] = temp
                change = True
    for t in crawl:
        print("link {} is linked to:".format(t[0]))
        for k in t[1]:
            print("   -{}".format(k))

            
>>> Crawler("https://www.crawler-test.com/")
Crawling https://www.crawler-test.com/ got : ['https://www.crawler-test.com//urls/double_slash/disallowed_start', 'https://subdomain.crawler-test.com', 'https://invalid.crawler-test.com', 'http://crawler-test.com/', 'http://www.crawler-test.com', 'https://www.crawler-test.com']
Crawling https://www.crawler-test.com//urls/double_slash/disallowed_start got : []
Crawling https://subdomain.crawler-test.com got : []
Eror for https://invalid.crawler-test.com
Crawling https://invalid.crawler-test.com got : []
Crawling http://crawler-test.com/ got : ['https://crawler-test.com//urls/double_slash/disallowed_start', 'https://subdomain.crawler-test.com', 'https://invalid.crawler-test.com', 'http://crawler-test.com/', 'http://crawler-test.com', 'https://crawler-test.com']
Crawling http://www.crawler-test.com got : ['https://www.crawler-test.com//urls/double_slash/disallowed_start', 'https://subdomain.crawler-test.com', 'https://invalid.crawler-test.com', 'http://crawler-test.com/', 'http://www.crawler-test.com', 'https://www.crawler-test.com']
Crawling https://www.crawler-test.com got : ['https://www.crawler-test.com//urls/double_slash/disallowed_start', 'https://subdomain.crawler-test.com', 'https://invalid.crawler-test.com', 'http://crawler-test.com/', 'http://www.crawler-test.com', 'https://www.crawler-test.com']
Crawling https://crawler-test.com//urls/double_slash/disallowed_start got : []
Crawling http://crawler-test.com got : ['https://crawler-test.com//urls/double_slash/disallowed_start', 'https://subdomain.crawler-test.com', 'https://invalid.crawler-test.com', 'http://crawler-test.com/', 'http://crawler-test.com', 'https://crawler-test.com']
Crawling https://crawler-test.com got : ['https://crawler-test.com//urls/double_slash/disallowed_start', 'https://subdomain.crawler-test.com', 'https://invalid.crawler-test.com', 'http://crawler-test.com/', 'http://crawler-test.com', 'https://crawler-test.com']
link https://www.crawler-test.com/ is linked to:
   -start page
link https://www.crawler-test.com//urls/double_slash/disallowed_start is linked to:
   -https://www.crawler-test.com/
   -http://www.crawler-test.com
   -https://www.crawler-test.com
link http://www.crawler-test.com is linked to:
   -https://www.crawler-test.com/
   -http://www.crawler-test.com
   -https://www.crawler-test.com
link https://www.crawler-test.com is linked to:
   -https://www.crawler-test.com/
   -http://www.crawler-test.com
   -https://www.crawler-test.com
link https://crawler-test.com//urls/double_slash/disallowed_start is linked to:
   -http://crawler-test.com/
   -http://crawler-test.com
   -https://crawler-test.com
link http://crawler-test.com is linked to:
   -http://crawler-test.com/
   -http://crawler-test.com
   -https://crawler-test.com
link https://crawler-test.com is linked to:
   -http://crawler-test.com/
   -http://crawler-test.com
   -https://crawler-test.com
link https://subdomain.crawler-test.com is linked to:
   -https://www.crawler-test.com/
   -http://crawler-test.com/
   -http://www.crawler-test.com
   -https://www.crawler-test.com
   -http://crawler-test.com
   -https://crawler-test.com
link https://invalid.crawler-test.com is linked to:
   -https://www.crawler-test.com/
   -http://crawler-test.com/
   -http://www.crawler-test.com
   -https://www.crawler-test.com
   -http://crawler-test.com
   -https://crawler-test.com
link http://crawler-test.com/ is linked to:
   -https://www.crawler-test.com/
   -http://crawler-test.com/
   -http://www.crawler-test.com
   -https://www.crawler-test.com
   -http://crawler-test.com
   -https://crawler-test.com
>>> 
