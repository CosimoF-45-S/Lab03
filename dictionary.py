class Dictionary:
    def __init__(self):
        self.dict_listed = []

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                self.dict_listed.append(line.strip())

    def printAll(self):
        for line in self.dict_listed:
            print(line)


    @property
    def dict(self):
        return self.dict_listed