from turtle import color
from src import testSubject

def test_getColor():
    answer = testSubject.Pen.getColor(color)
    assert answer == "BLUE"