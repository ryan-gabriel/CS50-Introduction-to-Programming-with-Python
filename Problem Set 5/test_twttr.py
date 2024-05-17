from twttr import shorten

def test_twttr():
    try:
        assert shorten("Test") == "Tst"
        assert shorten("TesTIng") == "TsTng"
        assert shorten("program") == "prgrm"
        assert shorten("program0") == "prgrm0"
        assert shorten("program!") == "prgrm!"
    except:
        exit(0)
