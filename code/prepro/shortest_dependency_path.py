from prepro.etri_caller import getETRI
from prepro.djikstra import *
from konlpy.tag import Twitter
import json
import csv
import pickle



def get_edges(dependency_arr):
    for dependency in dependency_arr:
        id = dependency["id"]
        text = dependency["text"]
        head = dependency["head"]
        label = dependency["label"]


def get_ESDP(SDP, dependency_arr):
    print()


if __name__ == "__main__":

    tw = Twitter()

    with open("../../data/kaist/relation_dict.pkl", 'rb') as f:
        rel_ind = pickle.load(f)

    sentence_data = list(csv.reader(open("../../data/kaist/crowd_gi_true.csv",'r',encoding='utf-8')))
    for line in sentence_data:
        sentence = line[0]
        relation = line[1]

        if relation not in rel_ind:
            remove_count = remove_count + 1
            continue

        if sentence.find("<e1>") == -1 or sentence.find("<e2>") == -1:
            continue

        e1 = sentence[sentence.find("<e1>"):sentence.find("</e1>") + 5]
        e2 = sentence[sentence.find("<e2>"):sentence.find("</e2>") + 5]

        sentence = sentence.replace("[", "")
        sentence = sentence.replace("]", "")

        tokens = sentence.split()

        p1 = tokens.index(e1)
        p2 = tokens.index(e2)

        sentence = sentence.replace("<e1>", "")
        sentence = sentence.replace("<e2>", "")
        sentence = sentence.replace("</e1>", "")
        sentence = sentence.replace("</e2>", "")

        etri_result = getETRI(sentence)

        etri_sentence_arr = etri_result["sentence"]
        for etri_sentence in etri_sentence_arr:
            graph = Graph()
            dependency_arr = etri_sentence["dependency"]
            edges = get_edges(dependency_arr)
            for edge in edges:
                graph.add_edge(*edge)
            SDP = dijsktra(graph, p1, p2)
            ESDP = get_ESDP(SDP, dependency_arr)

        SDP_stc = ""
        ESDP_stc = ""

        for item in SDP:
            SDP_stc += item + " "

        for item in ESDP:
            ESDP_stc = item + " "

