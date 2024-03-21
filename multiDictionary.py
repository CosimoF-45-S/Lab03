import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dictionary = {}

    def printDic(self, language):
        dict = d.Dictionary()
        if not self.dictionary.__contains__(language):
            dict.loadDictionary(f"resources/{language}.txt")
            self.dictionary[language] = dict

    def searchWord(self, words, language):
        listW = []
        diction = self.dictionary.get(language).dict
        for word in words:
            control = False
            for word_dic in diction:
                if word == word_dic:
                    control = True
            richW = rw.RichWord(word)
            richW.corretta = control
            listW.append(richW)

        return listW


    def searchWordLinear(self, words, language):
        listW = []
        diction = self.dictionary.get(language).dict
        for word in words:
            if word in diction:
                richW = rw.RichWord(word)
                richW.corretta = True
                listW.append(richW)
            else:
                richW = rw.RichWord(word)
                richW.corretta = False
                listW.append(richW)
        return listW

    def searchWordDicotomic(self, words, language):
        listW = []
        diction = self.dictionary.get(language).dict
        for word in words:
            central = diction[int((len(diction)-1)/2)]
            if word < central:
                if word in diction[:int((len(diction)-1)/2)]:
                    richW = rw.RichWord(word)
                    richW.corretta = True
                    listW.append(richW)
                else:
                    richW = rw.RichWord(word)
                    richW.corretta = False
                    listW.append(richW)

            if word > central:
                if word in diction[int((len(diction)-1)/2):]:
                    richW = rw.RichWord(word)
                    richW.corretta = True
                    listW.append(richW)
                else:
                    richW = rw.RichWord(word)
                    richW.corretta = False
                    listW.append(richW)

            if word == central:
                richW = rw.RichWord(word)
                richW.corretta = True
                listW.append(richW)

        return listW





