from src.testSubject import Pen
import pytest


class TestPen:

    # isWork() method tests

    def test_isWork_defaults(self):
        a = Pen()
        testValue = a.isWork()
        assert testValue == True

    @pytest.mark.parametrize("containerValue,expectedResult", [(1,True),
    (0,False),
    (-1,False),
    pytest.param("txt", "ERROR", marks=pytest.mark.xfail(reason="Expected! Can't compare <str> and <int>.")),
    ])
    def test_isWork(self, containerValue, expectedResult):
        a = Pen(inkContainerValue= containerValue)
        testValue = a.isWork()
        assert testValue == expectedResult

    # getColor() method tests

    def test_getColor_defaults(self):
        a = Pen()
        testValue = a.getColor()
        assert testValue == "BLUE"

    @pytest.mark.parametrize("color, expectedResult", [("RED", "RED"),
    ("green", "GREEN"), ("#FFFFFF", "#FFFFFF"),
    ])
    def test_getColor_changedColor(self, color, expectedResult):
        a = Pen(color= color)
        testValue = a.getColor()
        assert testValue.upper() == expectedResult

    # write(word) method tests

    @pytest.mark.parametrize("containerValue, expectedResult", [(0, "Pen is empty!"),
    (-1, "Pen is empty!"), 
    ])
    def test_write_isNotWorking(self, containerValue, expectedResult):
        a = Pen(inkContainerValue= containerValue)
        notWorking = a.write("text_sample")
        assert notWorking == expectedResult

    @pytest.mark.parametrize("letterSize, wordSample", [(1.0, ""), (0.0, "TestAutomation")])
    def test_sizeOfWord_zeroSize(self, letterSize, wordSample):
        a = Pen(inkContainerValue= 100, sizeLetter= letterSize)
        wordReturn = a.write(wordSample)
        assert len(wordReturn) == 0

    @pytest.mark.parametrize("word, expectedResult", [("Hey!","Hey!"), ("Privet", "Privet")])
    def test_sizeOfWord(self, word, expectedResult):
        a = Pen(inkContainerValue = 6)
        wordReturn = a.write(word)
        assert wordReturn == expectedResult

    @pytest.mark.parametrize("word, containerValue", [("qwerty", 5), 
    ("Hello!", 2), pytest.param("Hell", 0, marks=pytest.mark.xfail(reason= "Expected! We can't write with empty pen.")), 
    ("Lol", 2.5),
    pytest.param("Hey!", -1, marks=pytest.mark.xfail(reason="Expected! We can't have negative inkContainerVaule.")),
    ])
    def test_partOfWord(self, word, containerValue):
        a = Pen(inkContainerValue= containerValue)
        wordReturn = a.write(word)
        assert wordReturn == word[0:containerValue]

    # doSomethingElse method tests
    def test_doSomethingElse(self):
        a = Pen()
        doSmth = a.doSomethingElse()
        assert doSmth == a.color
