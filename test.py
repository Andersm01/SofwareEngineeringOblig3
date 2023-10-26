from SofwareEngineeringOblig3.main import isLeapYear


def testIsLeapyearDividedBy400():
    assert isLeapYear(2000) == True

def test2NotLeapyearSinceNotDividableBy400():
    assert isLeapYear(1900) == False

def test3IsNotLeapyearSinceNotDividableBy400():
    assert isLeapYear(1700) == False

def test4IsLeapyearSinceDividableBy4Not100():
    assert isLeapYear(2020) == True

def test5IsNotLeapyearSinceNotDividableBy4():
    assert isLeapYear(2100) == False