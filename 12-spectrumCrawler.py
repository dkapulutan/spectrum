from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.spectrummonitoring.com/frequencies/'
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
print(type(soup))
soupStr = str(soup)
c = 0

country = re.findall('<a id="(\S+)"', soupStr)
print(country)
update = re.findall('Updated: ([0-9]+\s\S+\s[0-9]+)</td', soupStr)
print(update)

# while country[c] != 
############
# c = soup('a', id=re.compile('[a-z]*') )
# x = str(c[0])
# country = re.findall('<a id="(\S+)"', x)
# # print(country, type(country))
# print(country)
#
# update = re.findall('Updated: ([0-9]+\s\S+\s[0-9]+)</td', x)
# print(update)
#
# l = soup('table', border="0", cellspacing="1", cellpadding="0")
# x = str(l[:5])
# link = re.findall('style="color:#FFFFFF;text-align:center;font-size:55%;background-color:#606060;">(FDD\s\S+link)', x)
# print(link)
# freq = re.findall('style="width:50px;">([0-9]+):</td>', x)
# print(freq)
# band = re.findall('style="width:\S+;text-align:[leftright]+;font-size:55%;">(\s*[0-9]+)', x)
# print(band)
##################

#
# telco = soup('table', border="0", cellspacing="4", cellpadding="1")
# print(telco[0])
