class Pen:
    def __init__(self, inkContainerValue = 1000, sizeLetter = 1.0, color = "RED"):
        self.inkContainerValue = inkContainerValue  # сколько чернила в ручке
        self.sizeLetter = sizeLetter  # размер букв, которые пишутся ручкой
        self.color = color  # цвет ручки

    def write(self, word):
        if not self.isWork():
            return ""

        sizeOfWord = len(word) * self.sizeLetter
        if sizeOfWord <= self.inkContainerValue:
            self.inkContainerValue -= sizeOfWord
            return word

        partOfWord = word[0: self.inkContainerValue]
        self.inkContainerValue = 0
        return partOfWord

    #BUGGGGGGGGGGGGGGGG
    def getColor(self):
        return "BLUE"

    def isWork(self):
        return self.inkContainerValue > 0

    def doSomethingElse(self):
        print(self.color)