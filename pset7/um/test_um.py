import pytest
from um import count

def test_count():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thamks, um...") == 2

def test_count_false():
    assert count("yummy") == 0

def test_count_case():
    assert count("Hello um world") == 1
    assert count("um") == 1