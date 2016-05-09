# Get puppies from puppyfinder
# coding: utf-8

# In[ ]:

from lxml import html
import requests
import csv
import string
    
outfile = open('pupfile.xls','wb')
csv_out=csv.writer(outfile, delimiter='\t')


# In[ ]:

def pritems(selector):
    return [item.text.replace('\n', '').replace('\r', '').encode('utf8') for item in tree.cssselect(selector)]

def do_page(tree):
    listingDate = pritems('p.dateListed b')
    titles = tree.cssselect('ul.items li h2.block-title')
    title=[t.get('title').encode('utf8') for t in titles]
    rescue = pritems('span.rescue-ic')
    breed = pritems('div.properties table tr:nth-child(2) td a')
    age = pritems('div.properties table tr:nth-child(4) td b')
    location = pritems('div.properties table td a.set-tip')
    gender = pritems('div.properties span.ic')
    description = pritems('div.description')
    return zip(listingDate, title, rescue, breed, location, gender, age, description)

for i in range(1,141):
    page = requests.get('http://puppyfinder.com/dogs-for-adoption?&locationKey=california&`id`_page='+str(i)+'#listtop')
    tree = html.fromstring(page.content)
    print "I", i 
    puppies = do_page(tree)
    for row in puppies:
        try:
            csv_out.writerow(row)
        except UnicodeEncodeError as e:
            print (row, i, e.errno, e.strerror)
            continue



