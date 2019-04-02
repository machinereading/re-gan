from konlpy.tag import Twitter
import re


class twitter_parser():
    def __init__(self):
        self.tw = Twitter()

    def tagging(self, s):
        e1 = s[s.find("<e1>"):s.find("</e1>") + 5]
        e2 = s[s.find("<e2>"):s.find("</e2>") + 5]
        s = s.replace(e1, " <(_sbj_)> ", 1)
        s = s.replace(e2, " <(_obj_)> ", 1)
        s = s.replace("[", " << ")
        s = s.replace("]", " >> ")
        tokens = s.split(" ")
        s = tokens
        tokens = self.tw.pos(s, norm=True, stem=True)
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
        s = s.replace("<(_obj_)>"," <<_obj_>> ",1)
        s = s.replace("<(_sbj_)>"," <<_sbj_>> ",1)
        e1 = e1[4:e1.find("</e1>")] + "/Entity"
        e2 = e2[4:e2.find("</e2>")] + "/Entity"
        return s,e1,e2