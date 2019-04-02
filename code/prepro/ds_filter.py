import csv

csvwriter = csv.writer(open('../../data/kaist/ds_wikilink_except_labeled.csv', 'w', encoding='utf-8'))

ds_set = set()
sentence_data = list(csv.reader(open("../../data/kaist/crowd_gi_true.csv",'r',encoding='utf-8')))
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('<e1>', '')
    sentence = sentence.replace('<e2>', '')
    sentence = sentence.replace('</e1>', '')
    sentence = sentence.replace('</e2>', '')
    sentence = sentence.replace('[', '')
    sentence = sentence.replace(']', '')
    sentence = sentence.replace('_', '')
    ds_set.add(sentence)

sentence_data = list(csv.reader(open("../../data/kaist/crowd_gi_false.csv",'r',encoding='utf-8')))
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('<e1>', '')
    sentence = sentence.replace('<e2>', '')
    sentence = sentence.replace('</e1>', '')
    sentence = sentence.replace('</e2>', '')
    sentence = sentence.replace('[', '')
    sentence = sentence.replace(']', '')
    sentence = sentence.replace('_', '')
    ds_set.add(sentence)

sentence_data = list(csv.reader(open("../../data/kaist/crowd_agreement_true.csv",'r',encoding='utf-8')))
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('<e1>', '')
    sentence = sentence.replace('<e2>', '')
    sentence = sentence.replace('</e1>', '')
    sentence = sentence.replace('</e2>', '')
    sentence = sentence.replace('[', '')
    sentence = sentence.replace(']', '')
    sentence = sentence.replace('_', '')
    ds_set.add(sentence)

sentence_data = list(csv.reader(open("../../data/kaist/crowd_agreement_false.csv",'r',encoding='utf-8')))
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('<e1>', '')
    sentence = sentence.replace('<e2>', '')
    sentence = sentence.replace('</e1>', '')
    sentence = sentence.replace('</e2>', '')
    sentence = sentence.replace('[', '')
    sentence = sentence.replace(']', '')
    sentence = sentence.replace('_', '')
    ds_set.add(sentence)

sentence_data = list(csv.reader(open("../../data/kaist/tta_answer_76.csv",'r',encoding='utf-8')))
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('<e1>', '')
    sentence = sentence.replace('<e2>', '')
    sentence = sentence.replace('</e1>', '')
    sentence = sentence.replace('</e2>', '')
    sentence = sentence.replace('[', '')
    sentence = sentence.replace(']', '')
    sentence = sentence.replace('_', '')
    ds_set.add(sentence)

sentence_data = list(csv.reader(open("../../data/kaist/ds_wikilinkCorpus.csv",'r',encoding='utf-8')))
for line in sentence_data:
    sentence = line[0]
    relation = line[1]
    sentence = sentence.replace(' ', '')
    sentence = sentence.replace('<e1>', '')
    sentence = sentence.replace('<e2>', '')
    sentence = sentence.replace('</e1>', '')
    sentence = sentence.replace('</e2>', '')
    sentence = sentence.replace('[', '')
    sentence = sentence.replace(']', '')
    sentence = sentence.replace('_', '')

    if sentence in ds_set:
        print(sentence)
    else:
        csvwriter.writerow([line[0], line[1]])

