import pickle
import csv
from konlpy.tag import Twitter
import re


def group_data(raw_data, merge_by_entity=False):
    if len(raw_data) == 0:
        return []
    # data: list of (t, e, p, r)
    # return:
    #    a list [(list of relation id, list of (text, position))]
    if not merge_by_entity:
        # every single instance becomes a group
        data = [([r], [(t, p)]) for t, e, p, r in raw_data]
    else:
        # merge mentions by entity names
        group = dict()
        for t, e, p, r in raw_data:
            if e not in group:
                group[e] = (set(), [], [])
            group[e][0].add(r)
            group[e][1].append(t)
            group[e][2].append(p)

    return group


def tagging(s):
    e1 = s[s.find("<e1>"):s.find("</e1>") + 5]
    e2 = s[s.find("<e2>"):s.find("</e2>") + 5]
    s = s.replace(e1, " <(_sbj_)> ", 1)
    s = s.replace(e2, " <(_obj_)> ", 1)
    s = s.replace("[", " << ")
    s = s.replace("]", " >> ")
    # tokens = s.split(" ")
    # s = tokens
    tokens = tw.pos(s, norm=True, stem=True)
    s = ""
    for token in tokens:
        token = list(token)
        s += token[0] + "/" + token[1] + " "
    entities = re.findall("<</Punctuation.*?>>/Punctuation", s)
    for i in range(len(entities)):
        r = ""
        t_list = entities[i].split(" ")
        for e in t_list:
            if e == "<</Punctuation" or e == ">>/Punctuation":  continue
            r += e.split("/")[0]
        r += "/Entity"
        s = s.replace(entities[i], r, 1)
    s = s.replace("<(_/Punctuation obj/Alpha _)>/Punctuation", "<<_obj_>>", 1)
    s = s.replace("<(_/Punctuation sbj/Alpha _)>/Punctuation", "<<_sbj_>>", 1)
    s = s.replace("<(_obj_)>", "<<_obj_>>", 1)
    s = s.replace("<(_sbj_)>", "<<_sbj_>>", 1)
    e1 = e1[4:e1.find("</e1>")] + "/Entity"
    e2 = e2[4:e2.find("</e2>")] + "/Entity"
    s = s.replace("<<_obj_>>"," " + e2 + " ",1)
    s = s.replace("<<_sbj_>>"," " + e1 + " ",1)
    return s,e1,e2

with open("../../data/kaist/relation_dict.pkl", 'rb') as f:
    rel_ind = pickle.load(f)

tw = Twitter()
sentence_data = list(csv.reader(open("../../data/kaist/tta_answer_76_underscore.csv",'r',encoding='utf-8')))
# origin_sentences=[]
label_data_raw_list = []
remove_count = 0

for line in sentence_data:

    # origin_sentences.append(line)
    sentence = line[0]
    relation = line[1]

    if relation not in rel_ind:
        remove_count = remove_count + 1
        continue

    if sentence.find("<e1>") == -1 or sentence.find("<e2>") == -1:
        continue
    sentence, e1, e2 = tagging(sentence)

    # print(sentence, e1, e2)

    entity = (e1, e2)

    sentence = sentence.split()

    p1 = sentence.index(e1)
    p2 = sentence.index(e2)

    position = (p1, p1 + 1, p2, p2 + 1)

    label_data_raw = (sentence, entity, position, relation)
    label_data_raw_list.append(label_data_raw)

print(remove_count)

group = group_data(label_data_raw_list, True)

with open('../../data/kaist/tta_answer_76.pkl', 'wb') as f:
    pickle.dump(group, f)








