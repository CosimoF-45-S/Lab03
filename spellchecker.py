import time

import multiDictionary as md


class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        txt = replaceChars(txtIn)
        words = listLower(txt.split())
        multi_dict = md.MultiDictionary()
        multi_dict.printDic(language)
        print("______________________________")
        print("Using contains")
        start_time1 = time.time()
        list_w = multi_dict.searchWord(words, language)
        for w in list_w:
            if w.corretta is False:
                print(w.parola)
        end_time1 = time.time()
        elapsed_time1 = end_time1 - start_time1
        print(f"Tempo impiegato: {elapsed_time1}")
        print("______________________________")
        print("Using linear research")
        start_time2 = time.time()
        list_w = multi_dict.searchWordLinear(words, language)
        for w in list_w:
            if w.corretta is False:
                print(w.parola)
        end_time2 = time.time()
        elapsed_time2 = end_time2 - start_time2
        print(f"Tempo impiegato: {elapsed_time2}")
        print("______________________________")
        print("Using dicotomic research")
        start_time3 = time.time()
        list_w = multi_dict.searchWordDicotomic(words, language)
        for w in list_w:
            if w.corretta is False:
                print(w.parola)
        end_time3 = time.time()
        elapsed_time3 = end_time3 - start_time3
        print(f"Tempo impiegato: {elapsed_time3}")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

def listLower(list):
    output = []
    for element in list:
        output.append(element.lower())
    return output