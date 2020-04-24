from CalcWithFunctions import one
from CalcWithFunctions import plus
from CalcWithFunctions import two
from CalcWithFunctions import seven
from CalcWithFunctions import times
from CalcWithFunctions import five
from CalcWithFunctions import divided_by
from CalcWithFunctions import three

def test_1():
    assert one(plus(one())) == 2

def test_2():
    assert seven(times(five())) == 35

def test_3():
    assert seven(divided_by(three())) == 2