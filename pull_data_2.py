import os
import requests
import csv
from bs4 import BeautifulSoup
import numpy
import pandas as pd
import process_party_data

name_msgs = {}

def update_name_msgs(name, msg, name_msgs): #DONE
    if name not in name_msgs:
        name_msgs[name] = []
    name_msgs[name].append(msg)
    return name_msgs

def get_document_term_matrix(msgs):
    row_len = len(msgs)
    row_count = 0
    words = {}
    for row in msgs:
        for word in row.split(" "):
            word = word.strip(",.<>?/:;~@$%&()")
            if word not in words:
                words[word] = [0]*row_len
            words[word][row_count] += 1
        row_count += 1
    df = pd.DataFrame(data=words)
    print(df.columns)
    

def filter_row(row):
    pass

def filter_text(line): #DONE
    new_line = ""
    for i in range(len(line)):
        if ord(line[i]) in range(127):
                new_line += line[i]        
    line = new_line.replace('&amp;', '&')
    if line.find('https://') != -1:
        return line[:line.find('https://')-1]
    return line[:line.find('http://')-1]

def filter_label(line): #DONE
    name = line[line.find("From:")+6:line.find("(")-1]
    position = line[line.find("(")+1:line.find("from")-1]
    state = line[line.find("from")+5:line.find(")")]
    return (name, position, state)

def get_partisanship(name):
    'class="about-info-box__info-value"'
    name = name.replace(" ", "+")
    url = "https://duckduckgo.com/?q={}+&ia=news".format(name)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all("div", class_="about-info-box__info-row")
    print(soup.prettify())

url = "https://download.data.world/s/hhmt6motfqbspgn64k6b2ftverkc3e"

myfile = requests.get(url)
file = open("data.csv", "wb")
file.write(myfile.content)
file.close()

headings = "unit_id,bias,bias_confidence,message,message_confidence,label,text"

data = open("data.csv", "r", encoding="Latin-1")
count = 0
csv_reader = csv.DictReader(data, delimiter=",", quotechar='"')
texts = []
for row in csv_reader:
    msg = row['message']
    if msg != 'personal':
        name, pos, state = filter_label(row['label'])
        text = filter_text(row['text'])
        name_msgs = update_name_msgs(name, text, name_msgs)
        #doc_term_matrix = update_document_term_matrix(text, doc_term_matrix)
        texts.append(text)
        count += 1


#print(count)
#get_document_term_matrix(texts)
print(name_msgs.keys())



















#for row in csv_reader:
'''    unit_id = int(row['unit_id'])-766192484
    bias = row['bias']
    msg = row['message']
    name, pos, state = filter_label(row['label'])
    text = filter_text(row['text'])
    if msg != 'personal': print("-----------------------------------------------------------------------------------------------\nID: {}\nBIAS: {}\nMSG: {}\nNAME: {}\nPOS: {}\nSTATE: {}\nTEXT: {}\n-----------------------------------------------------------------------------------------------\n".format(unit_id, bias, msg, name, pos, state, text))
    time.sleep(3)'''
data.close()
