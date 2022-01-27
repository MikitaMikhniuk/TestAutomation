import src.testSubject as source

class TestPen:

    def test_getColor(self):
        a = source.Pen(color="RED")
        answer = a.getColor()
        assert answer == "BLUE"
        print(a.getColor())
