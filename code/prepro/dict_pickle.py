import pickle


f = open("../../data/kaist/embedding/elmo/elmo_dict.txt", "r")
lines = f.readlines()
f.close()
vocab_list = []
for line in lines:
    vocab_list.append(line.replace("\n", ""))

# property_dict = {'nationality': 1, 'birthPlace': 2, 'country': 0, 'residence': 3, 'deathPlace': 4}

with open('../../data/kaist/embedding/elmo/elmo_dict.pkl', 'wb') as f:
    pickle.dump(vocab_list, f)

