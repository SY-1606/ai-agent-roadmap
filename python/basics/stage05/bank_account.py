
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("初始余额不能为负数")

        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于0")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须大于0")

        if amount > self._balance:
            print("余额不足")
            return False

        self._balance -= amount
        return True

    def show_balance(self):
        print(f"{self.owner} 的余额：{self._balance:.2f}")


def main():
    account = BankAccount("Tom", 1000)

    account.deposit(500)
    account.show_balance()

    account.withdraw(300)
    account.show_balance()

    account.withdraw(2000)
    account.show_balance()


if __name__ == "__main__":
    main()
