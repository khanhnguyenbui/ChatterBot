# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:23:51 2018

@author: Khanh Bui
"""
import io
import ast

def load_line_dataset(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    data = {}
    i=0
    for line in fin:
        token = line.rstrip().split(' +++$+++ ')
        try:
            data[token[0]] = token[4]
        except:
            print('Error at line: '+str(i))
        i += 1
        #if i==10000:
        #   break
    return data

line_dataset = load_line_dataset('E:\Current Projects\Chatbot\cornell movie-dialogs corpus\movie_lines.txt')

def load_conversation_dataset(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    data = {}
    i=0
    for line in fin:
        token = line.rstrip().split(' +++$+++ ')
        try:
            data[i] = token[3]
        except:
            print('Error at line: '+str(i))
        i += 1
        #if i==10:
           #break
    return data


conversation_dataset = load_conversation_dataset('E:\Current Projects\Chatbot\cornell movie-dialogs corpus\movie_conversations.txt')

def response_pair(dataset):
    i=0
    allPairs={}
    for element in dataset:
        array = dataset[i]
        array = ast.literal_eval(array)
        i+=1
        for k in range(len(array)-1):
            allPairs[array[k]] = array[k+1]
    return allPairs

allPairs = response_pair(conversation_dataset)
a = list(allPairs.keys())
    



text_file = open("E:\Current Projects\ChatterBot\MovieDataset.yml", "w")
text_file.write("categories:\n- movie\nconversations:\n")
for pair in allPairs.keys():
    try:
        a = line_dataset[pair]
        b = line_dataset[allPairs[pair]]
        c = {'"': '',',':'', "'": '', '-':'',"*": '', ":": '', "[": '', "]": '', "	":'', "`":'', "{":'',"}":'', "(":'',")":'', ";":'',"&":'',"|":'',"!":''}
        d = {': "': ': ', ": '": ': ', ':':'<colon>', '	':' ',"'cause":"Because"," 'at's":"That's"}
        for x,y in c.items():
            if a.strip(' ').startswith(x):
                a = a.replace(x, y)
            if b.strip(' ').startswith(x):
                b = b.replace(x, y)
        for x,y in c.items():
            if a.strip(' ').startswith(x):
                a = a.replace(x, y)
            if b.strip(' ').startswith(x):
                b = b.replace(x, y)        
                
        for x,y in d.items():
            a = a.replace(x, y)
            b = b.replace(x, y)     
                
        
        line_dataset[pair]
        text_file.write("- - "+ a + "\n" + "  - " + b +"\n")
    except:
        print("error at: " + str(pair))
text_file.close()

