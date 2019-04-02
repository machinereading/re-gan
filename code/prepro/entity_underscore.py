import csv

sentence_data = list(csv.reader(open("../../data/kaist/tta_answer_76.csv", 'r', encoding='utf-8')))

cw = csv.writer(open("../../data/kaist/tta_answer_76_underscore.csv", 'w', encoding='utf-8', newline=''))

for line in sentence_data:
    sentence = line[0]
    relation = line[1]

    if sentence.find("<e1>") == -1 or sentence.find("<e2>") == -1:
        continue

    p1s = sentence.find("<e1>")
    p2s = sentence.find("<e2>")

    p1e = sentence.find("</e1>") + 5
    p2e = sentence.find("</e2>") + 5

    e1 = sentence[p1s:p1e]
    e2 = sentence[p2s:p2e]

    e1 = e1.replace(" ", "_");
    e2 = e2.replace(" ", "_");

    if p1s > p2s:
        cw.writerow([sentence[:p2s] + e2 + sentence[p2e:p1s] + e1 + sentence[p1e:], relation])
    else:
        cw.writerow([sentence[:p1s] + e1 + sentence[p1e:p2s] + e2 + sentence[p2e:], relation])


