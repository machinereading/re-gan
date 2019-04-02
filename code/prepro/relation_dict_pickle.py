import pickle


f = open("../../data/kaist/relation_dict_65.txt", "r")
lines = f.readlines()
f.close()
count = 0
property_dict = {}
for line in lines:
    property_dict[line.replace("\n", "")] = count
    count = count + 1

# property_dict = {'nationality': 1, 'birthPlace': 2, 'country': 0, 'residence': 3, 'deathPlace': 4}

with open('../../data/kaist/relation_dict_65.pkl', 'wb') as f:
    pickle.dump(property_dict, f)

