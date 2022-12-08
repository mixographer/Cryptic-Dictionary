#!/usr/bin/env python3

import sys


file = open('dictionary.txt')
lines = file.readlines()


print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
print("<d:dictionary xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:d=\"http://www.apple.com/DTDs/DictionaryService-1.0.rng\">")
print("<d:entry id=\"xword\" d:title=\"XWORD\">")
print("  	<d:index d:value=\"XWORD\"/>")
print("	    <h1>XWORD</h1>")
print("  	<p>Crossword Words and Abbreviations</p>")
print("</d:entry>")
print('<d:entry id="front_back_matter" d:title="Mixo\'s Cryptic">')
print('    <d:index d:value="Title"/>')
print("    <h1><b>Mixo's Cryptic Dictionary</b></h1>")
print('    <h2>Cryptic words, abbreviations and indicators</h2>')
print('    <p>Mixo\'s Cryptic Dictionary includes abbreviations, deletions, homophones, and reversals.<br/> </p>')
print('    <p><i>Sir, I hope you will not object if I  offer you my most enthusiastic contrafribularities.')
print('           I’m anaspeptic, frasmotic, even compunctious to have caused you such pericombobulation.</i></p>')
print('           <p>- Blackadder</p>')
print('</d:entry>')
# the loop part
for line in lines: 
    line.strip()
    defn, abbr = line.split(":", 1)
    abbr = abbr.strip()
    #print(defn)
    #print('</d:' + abbr + '>')
    print('<d:entry id="' + abbr + '" d:title="' + abbr + '">')
    print('<d:index d:value="' + abbr + '"/>')
    print('	<h1> '+ abbr + '</h1>')
    print('	<p> '+ defn + '</p>')
    print('</d:entry>')


#the closure after the loop

print("</d:dictionary>")







