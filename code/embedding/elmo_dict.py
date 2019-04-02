line_count = 0
file_count = 0

dict = {}

dict_writer = open("../data/kaist/elmo/elmo_dict.txt", 'w')
dict_writer.write("<S>\n")
dict_writer.write("</S>\n")
dict_writer.write("<UNK>\n")

write_lines = []

corpus_reader = open("../data/kaist/elmo/wikilinkCorpus_wv.txt", 'r')
lines = corpus_reader.readlines()
for line in lines:
    line_count = line_count + 1
    if line_count % 10000 == 0:
        split_writer = open("../data/kaist/elmo/train_corpus/{0}.txt".format(file_count), 'w')
        for write_line in write_lines:
            split_writer.write(write_line)
        write_lines.clear()
        line_count = 0
        file_count = file_count + 1
        split_writer.close()
    else:
        write_lines.append(line)
    tokens = line.split()
    for token in tokens:
        if token in dict:
            curr_count = dict.get(token)
            curr_count = curr_count + 1
            dict[token] = curr_count
        else:
            dict[token] = 1

sorted_dict = sorted(dict, key=lambda k : dict[k], reverse=True)
for item in sorted_dict:
    dict_writer.write(item + "\n")

dict_writer.close()
corpus_reader.close()