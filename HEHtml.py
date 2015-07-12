import re
#import urlib
import logging
import requests
from http.cookiejar import CookieJar as cj
from newspaper import *

def getDomain(url):
  m = re.search(r'http[s]?://(.*?)/',url)
  if m:
     return m.group()
  else:
     return ''

def fixLinks(html,link):
  def f(m):
    return link + m.group(1)

  reobj = re.compile('href="(/.*?)"')
  new = reobj.sub(f,html)
  return new

def getLinks(url,regex):
    #website = urllib.request.urlopen(url)
    #html = website.read().decode('utf-8')
    html = get_html(url)
    if isinstance(html, bytes):
        html = Parser.get_unicode_html(html)
    regex_new = '"(' + regex + ')"'
    print('regex:' + regex_new)
    links = re.findall(regex_new, html)

    return list(set(links))
