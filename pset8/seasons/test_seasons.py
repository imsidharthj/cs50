import pytest
from seasons import check_date

def test_check_date():
    assert check_date("1999-05-25") == (1999, 5, 25)
    assert check_date("1999-5-25") is None
    assert check_date("may 25, 1999") is None
