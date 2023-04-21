class Account:
    def __init__(self, name):
        """
        Initializes an account object with the specified name and a balance of 0.

        Parameters:
        name (str): The name to associate with the account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        """
        Increases the account balance by the specified amount.

        Parameters:
        amount (float): The amount to add to the account balance.

        Returns:
        bool: True if the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        """
        Decreases the account balance by the specified amount.

        Parameters:
        amount (float): The amount to subtract from the account balance.

        Returns:
        bool: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
        float: The current account balance.
        """
        return self.__account_balance

    def get_name(self):
        """
        Returns the name associated with the account.

        Returns:
        str: The name associated with the account.
        """
        return self.__account_name