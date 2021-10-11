import os
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
#import pandas as pd
import time
import csv
from csvsort import csvsort
import operator
#from docx2pdf import convert
from csv import reader
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

filespath = []
shortlisted = []
contentcollection=[]
clientlist=[]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CVfolder=BASE_DIR+'/CV'
#get hiverlab client list
path=CVfolder
# r=root, d=directories, f = files
def listcheck():
    #this part make csv to a list of item
    #this part read each document
    output_string = StringIO()
    with open(singlefilepath, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    fullcontent=output_string.getvalue().lower().replace('\n','').replace('\r','')
    for whattofind in clientlist:
            searchelement=fullcontent.find(whattofind)
            if searchelement != -1:
                #print(singlefilepath)
                #print(whattofind)
                extracted=fullcontent[searchelement-20:searchelement+100].strip()
                print(extracted)
                with open(BASE_DIR+'/CVresult/cvresult.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    name=str(os.path.basename(singlefilepath))
                    writer.writerow([name,whattofind,extracted])
            else:
                print('can not find ', whattofind ,' in', singlefilepath)
    #print(fullcontent)    
def singlecontentcheck():
    output_string = StringIO()
    with open(singlefilepath, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    fullcontent=output_string.getvalue().lower().replace('\n','').replace('\r','')
    #print(fullcontent)
    searchelement=fullcontent.find(whattofind)
    if searchelement != -1:
        print(singlefilepath)
        #print(whattofind)
        extracted=fullcontent[searchelement-20:searchelement+100].strip()
        print(extracted)
        with open(BASE_DIR+'/CVresult/cvresult.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            name=str(os.path.basename(singlefilepath))
            writer.writerow([name,whattofind,extracted])
        #file.close()
        #contentcollection.append(extracted)
    else:
        print('can not find ', whattofind ,' in', singlefilepath)
    #print(searchelement)
print('Welcome to resume massive check app V1.1.6')
print('this program is written mainly for massive cv check as it is quite troublemsome to screen hundreds of cvs nowadays')
print('please read readme before using this')
time.sleep(1.5)
print('please drop all resumes into the [CV] folder before the analysis')
print('Currently this version is designed to search content in pdf resume format')
time.sleep(1.5)
print('If you would like to do a list search, please drop a info.csv file in [Infocsv] Folder, keep all data in one row')
print('.........')
time.sleep(3)
print('If you want to search random content, then your input should be single word or short phrase to get accurate result, like"annual revenue" "python","sales","intel"')
print('.........')
time.sleep(3)
print('This program will provide the result, organize, and write all result to the csv file in [CVresult] Folder')
print('You can search as many time as you want, and program will organize the final result\n')
#make a list of filepath for further reading
time.sleep(1.5)
# print('checking and converting docx to pdf...')
# convert(path)
# print('completed checking and converting')
# time.sleep(1.5)
print('Started...\n')
print('...................................................................................')
time.sleep(0.5)

for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            filespath.append(os.path.join(r, file))
Start=input('How do you want to search? [1] Search by keyword, [2] Search the list of item provided at [Infocsv] folder\n')
if Start=='1':
    while True:
        whattofind=input('What do you want to search from CVs:\nRemember: all input to be small letter\nInput[x] with Enter to Exit\n')
        if whattofind != 'x':
            for i in range(len(filespath)):
                #print(f[i])
                try:
                    singlefilepath=filespath[i]
                    singlecontentcheck()
            # block raising an exception
                except:
                    print('error file on ',file)
                    pass
        else:
            print('thank you and please check the result from [CVresult] folder')
            time.sleep(1.5)
            print('This Message Will Self-Destruct in Five Seconds')
            for i in range(5):
                print(5-i)
                time.sleep(1)
            break
elif Start=='2':
    print('total item...')
    print(len(filespath))
    time.sleep(1.5)
    with open(BASE_DIR+'/Infocsv/info.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
        for i in csv_reader:
            c=''.join(i)
            clientlist.append(c)
    print('item in the list')
    print(clientlist)
    time.sleep(1.5)
    for i in range(len(filespath)):
            #print(f[i])
        try:
            singlefilepath=filespath[i]
            listcheck()
    # block raising an exception
        except:
            print('error file on ',file)
            pass
with open(BASE_DIR+'/CVresult/cvresult.csv', 'r', newline='') as file:
    arranged=sorted(file,key=operator.itemgetter(0))
    print(arranged)
with open(BASE_DIR+'/CVresult/cvresult.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(arranged)):
        c=list(arranged[i].split(',',2))
        writer.writerow(c)