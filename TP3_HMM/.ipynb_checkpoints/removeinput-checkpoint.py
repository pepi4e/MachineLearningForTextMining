import os.path as op
import codecs

def removeTag(text, tag):
    return text[:text.find("<"+tag+">")] + text[text.find("</"+tag+">") + len(tag)+3:]

filename = 'TP3.html'

file =codecs.open(filename, 'r')
text = file.read()
file.close()

tag = 'input'
while(tag in text):
    text = removeTag(text, tag)

file = open(filename,'w')
file.write(text)
file.close()