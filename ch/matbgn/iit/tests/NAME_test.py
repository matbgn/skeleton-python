import pytest

from ..NAME.__main__ import main


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


@pytest.mark.parametrize("test_input, expected", [('ready!', 0)])
def test_main_basic(test_input, expected):
    assert main(test_input) == expected
