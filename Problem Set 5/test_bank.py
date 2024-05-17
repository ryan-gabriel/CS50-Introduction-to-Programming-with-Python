from bank import value

def test_bank1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("   hello    ") == 0

def test_bank2():
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("    hi    ") == 20

def test_bank3():
    assert value("what") == 100
    assert value("WHAT") == 100
    assert value("     what    ") == 100

def main():
    test_bank1()
    test_bank2()
    test_bank3()

if __name__ == "__main__":
    main()
