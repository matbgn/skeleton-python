from ch.matbgn.iit.NAME import __main__


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    assert __main__.main() == "ready!"
