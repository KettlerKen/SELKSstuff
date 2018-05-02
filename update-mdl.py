import requests
import csv
import re

listURL = 'http://www.malwaredomainlist.com/mdlcsv.php'

download = requests.get(listURL)

r = csv.reader(download.text.splitlines(), delimiter=',')
my_list = list(r)
categories = []

#Cleaning the 3rd row to get the IP
for row in my_list:
    if len(row) > 2:
        row[2] = re.search(r'[0-9]+(?:\.[0-9]+){3}', row[2]).group(0)

#Creating a set of categories to number
for row in my_list:
    if len(row) > 4:
        row[4] = row[4].replace(",", " ");
        categories.append(row[4])

categories = set(categories)
categories = list(categories)
categories.sort()

#Creating a categories.txt (num,category,DESC)
file = open('categories.txt', 'w+')
CategoriesDict = {}
i = 1
for item in categories:
    file.write(str(i) + ',' + item + ',' + 'DESC\n')
    CategoriesDict[item] = i
    i = i + 1

#Creating an mdl.list file
mdl = open('mdl.list', 'w+')
IPDict = {}
for row in my_list:
    if len(row) > 2:
        if row[2] in IDict:
            if IPDict[row[2]][1] < 126:
                IPDict[row[2]] = (CategoriesDict[row[4]], IPDict[row[2]][1] + 2)
        else:
            IPDict[row[2]] = (CategoriesDict[row[4]], 40)

for IP in IPDict:
    mdl.write(IP + "," + str(IPDict[IP][0]) + "," + str(IPDict[IP][1]) + '\n')

mdl.close()
file.close()



    
