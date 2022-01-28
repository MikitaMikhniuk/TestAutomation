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

    def test_getColor_changedColor(self):
        a = Pen(color= "RED")
        testValue = a.getColor()
        assert testValue == "RED"


    #_________________________JUST IN CASE__________________________
