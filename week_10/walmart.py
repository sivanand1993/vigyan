import urllib.request
fname = r"C:\Users\anand\Downloads\Walmart Grocery - Order History.html"
# HtmlFile = open(fname,'w')
# print (HtmlFile)
HtmlFile = open(fname, 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
from bs4 import BeautifulSoup
# bs = BeautifulSoup(source_code)
# print(bs)