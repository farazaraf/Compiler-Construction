'''Faraz Ahmad Qureshi - 200901045
Section B | BSCS 01 | Compiler Construction | Assignment 03
'''

from pathlib import Path    #to resolve absolute path to the file.
from xml.dom.minidom import parse #minidom is subset of the DOM (Document Object Model) library
import csv  #make csv file as we cannot make xlsx files without external modules.

print("[1]Trying to open \'compiler.xml\' file...")
relative_path = Path(__file__).parent #calculate the exact path to file
absolutePath = relative_path.resolve() / 'compiler.xml'
xmlObject = open(absolutePath,"r") #open the compiler.xml file
print("[2]File opened successfully...")
csvFile = open(relative_path.resolve() / '200901045_Assign_03.csv', 'w') #initialize our csv file
csvFieldNames = ['bookID','author','title','genre','price','publish_date','description']

csvInput = csv.DictWriter(csvFile, fieldnames=csvFieldNames)
csvInput.writeheader()

print("[3]Parsing the XML file...")
domObject = parse(xmlObject)    
books = domObject.getElementsByTagName("book")
print("[4]There are %d Books in the xml file." % books.length)
print("[5]Extracting following data:",csvFieldNames)

authorList=[]
titleList=[]
genreList=[] 
priceList=[]
publish_dateList=[]
descriptionList=[]
bookidList=[]
for book in books:
    bookidList.append(book.getAttribute('id'))
    authorList.append(book.getElementsByTagName("author")[0].firstChild.data)
    titleList.append(book.getElementsByTagName("title")[0].firstChild.data)
    genreList.append(book.getElementsByTagName("genre")[0].firstChild.data)
    priceList.append(book.getElementsByTagName("price")[0].firstChild.data)
    publish_dateList.append(book.getElementsByTagName("publish_date")[0].firstChild.data)
    descriptionList.append(book.getElementsByTagName("description")[0].firstChild.data)

for i in range(0,len(books)):
    csvInput.writerow({'bookID':bookidList[i],'title': titleList[i], 'author': authorList[i],'genre':genreList[i],'price':priceList[i],'publish_date':publish_dateList[i],'description':descriptionList[i]})

print('[6]Output has been stored to csv file!')