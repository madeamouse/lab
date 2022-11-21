import pytest
from account import *


def test_init():
    assert self.__account_name == 'John'
    assert self.__account_balance == 0

def test_deposit():
    assert deposit(127.56) == True
    assert deposit(-1) == False


def test_withdraw():
    asssert withdraw(2) == False
    assert withdraw