#!/usr/bin/python
import os
from xml.etree import ElementTree
from xml.dom import minidom

fileName = 'reed.xml'
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, fileName)
print(path)

dom = ElementTree.parse(path)
courses = dom.findall('course')
for course in courses:

    title = course.find('title').text
    number = course.find('crse').text
    days = course.find('days').text
    print(' * {} [{}] {}'.format(number, days, title))

#using minidom
fileName = 'test.xml'
doc = minidom.parse(fileName)
items = doc.getElementsByTagName('item')

print('Item 2 attribute: ' + items[1].attributes['name'].value)
for elem in items:
    print(elem.attributes['name'].value)

#get data from the first child
print('Item 2 data: ' + items[1].firstChild.data)
#get a specific childnodes data
print(items[1].childNodes[0].data)

#using elementtree
tree = ElementTree.parse('test.xml')
root = tree.getroot()

#get specific item attribute
print('Item 2 attribute: {}'.format(root[0][1].attrib))

#get all attributes
print('All attributes : ')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

#get specific item data
print('Item 2 data: {}'.format(root[0][1].text))

#get all data
print('All data')
for elem in root:
    for subelem in elem:
        print(subelem.text)

print('Number of items: {}'.format(len(root[0])))

#writing an xml file
data = ElementTree.Element('data')
items = ElementTree.SubElement(data, 'items')
item1 = ElementTree.SubElement(items, 'item')
item2 = ElementTree.SubElement(items, 'item')
item1.set('name', 'item1')
item2.set('name', 'item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

myData = ElementTree.tostring(data)
fh = open('items2.xml', 'w')
myData = myData.decode()
fh.write(myData)


