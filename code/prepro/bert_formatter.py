import pickle
import csv

with open("../../data/kaist/relation_dict_65.pkl", 'rb') as f:
    rel_ind = pickle.load(f)

sentence_data = list(csv.reader(open("../../data/kaist/crowd_agreement_true.csv", 'r', encoding='utf-8')))
f = open('../../data/kaist/train_agreement_65.tsv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f, delimiter='\t')

# csvwriter = csv.writer(open('../../data/kaist/test_65.csv', 'w', encoding='utf-8'))

print_list = []
remove_count = 0
for line in sentence_data:
    sentence = line[0]
    relation = line[1]

    if relation not in rel_ind:
        remove_count = remove_count + 1
        continue

    if sentence.find("<e1>") == -1 or sentence.find("<e2>") == -1:
        continue

    e1 = sentence[sentence.find("<e1>") + 4:sentence.find("</e1>")]
    e2 = sentence[sentence.find("<e2>") + 4:sentence.find("</e2>")]

    sentence = sentence.replace("  ", " ")
    sentence = sentence.replace("  ", " ")

    sentence = sentence.replace("[", "")
    sentence = sentence.replace("]", "")

    # sentence = sentence.replace("<e1>", "")
    # sentence = sentence.replace("<e2>", "")
    # sentence = sentence.replace("</e1>", "")
    # sentence = sentence.replace("</e2>", "")

    wr.writerow([relation, e1, e2, sentence])
    # csvwriter.writerow([sentence, relation])

print(remove_count)
f.close()