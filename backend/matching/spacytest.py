import spacy

import csv
with open(r'C:\Users\Jacob\Documents\LaddrBase\laddr\backend\matching\LolDuoCsv.csv','r') as f:
    reader = csv.reader(f)
    bios = list(reader)

nlp = spacy.load('en_core_web_md')

doc1=nlp(u"I hate to play chess.")
doc2=nlp(u"I love to play chess.")

goals=nlp(bios)

with open(r'C:\Users\Jacob\Documents\LaddrBase\laddr\backend\matching\nlpresults.csv',mode='w') as nlpresults:
    nlp_writer = csv.writer(nlpresults,delimiter=",")
    for bio in bios:
        for bio2 in bios:
            biostr = ''.join(bio)
            bio2str = ''.join(bio2)
            bionlp = nlp(biostr)
            bio2nlp = nlp(bio2str)
            biosims=bionlp.similarity(bio2nlp)
            nlp_writer.writerow([biostr,bio2str,biosims])


