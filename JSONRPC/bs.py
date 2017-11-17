#coding=utf-8
import urllib,urllib2
from bs4 import BeautifulSoup
try:
    html = urllib2.urlopen("http://192.168.80.128:8080/item/group")
except urllib2.HTTPError as err:
    print str(err)
soup = BeautifulSoup(html)
print soup
