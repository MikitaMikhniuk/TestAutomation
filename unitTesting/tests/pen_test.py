from src.testSubject import Pen
import pytest


class TestPen:

    # isWork() method tests
    def test_isWork_defaults(self):
        a = Pen()
        testValue = a.isWork()
        assert testValue == True

    def test_isWork_zeroValue(self):
        a = Pen(inkContainerValue= 0)
        testValue = a.isWork()
        assert testValue == False

    def test_isWork_negativeValue(self):
        a = Pen(inkContainerValue= -1)
        testValue = a.isWork()
        assert testValue == False

    @pytest.mark.xfail(reason="Expected! Can't compare <str> and <int>.")
    def test_isWork_notNumber(self):
        a = Pen(inkContainerValue= "txt")

    # getColor() method tests
    def test_getColor_defaults(self):
        a = Pen()
        testValue = a.getColor()
        assert testValue == "BLUE"

    def test_getColor_changedColor(self):
        a = Pen(color= "RED")
        testValue = a.getColor()
        assert testValue == "RED"