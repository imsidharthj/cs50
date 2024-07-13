from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    cookies = Jar()
    cookies.deposit(12)
    assert cookies.size == 12

    _cookies = Jar(12)
    with pytest.raises(ValueError):
        _cookies.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7

    _jar = Jar()
    _jar.deposit(12)
    with pytest.raises(ValueError):
        _jar.withdraw(13)