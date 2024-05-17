from plates import is_valid

def test_plates():
    assert is_valid("AAA22A") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("AAA222") == True
    assert is_valid("!. !!") == False
    assert is_valid("3 14") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("22AAAA") == False
    assert is_valid("AAAA222") == False


def main():
    test_plates()

if __name__ == "__main__":
    main()
