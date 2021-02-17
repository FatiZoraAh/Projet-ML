

import requests
from bs4 import BeautifulSoup
import csv
html =requests.get('https://www.dawn.com/')
soup=BeautifulSoup(html.text,"lxml")
h2=soup.find_all('h2',{'data-layout':'story'})
mcsv=open('links.json','w')
fieldnames=['LINKTEXT','FILELINK']
writer=csv.DictWriter(mcsv,fieldnames=fieldnames)
writer.writeheader()
for link in h2:
    myLink=BeautifulSoup(str(link),'html.parser')
    gettinglink=myLink.find('a',href= True)
    writer.writerow({'LINKTEXT':str(gettinglink.find(text=True)),
                     'FILELINK':str(gettinglink['href'])})
mcsv.close()
print('csv has been generated')

