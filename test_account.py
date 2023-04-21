from account import Account


def test_init():
    acc = Account("John")
    assert acc.get_name() == "John"
    assert acc.get_balance() == 0.0


def test_deposit():
    acc = Account("John")
    assert acc.deposit(100.0) is True
    assert acc.get_balance() == 100.0
    assert acc.deposit(-50.0) is False
    assert acc.get_balance() == 100.0


def test_withdraw():
    acc = Account("John")
    assert acc.deposit(100.0) is True
    assert acc.withdraw(50.0) is True
    assert acc.get_balance() == 50.0
    assert acc.withdraw(-20.0) is False
    assert acc.get_balance() == 50.0
    assert acc.withdraw(100.0) is False
    assert acc.get_balance() == 50.0
