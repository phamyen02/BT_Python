class BankAccount:
    minimum_balance = 50000

    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")

class Customer():
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        print(self.name, self.date_of_birth, self.email, self.phone)


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005

    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

    def calculate_interest(self):
        return self.balance * self.monthly_interest_rate

    def display(self):
        print("Acc Number:",self.account_number, "Balance:",
              self.balance, "Interest Rate:",self.monthly_interest_rate)

        if self.account_name is Customer:
            self.account_name.get_info()

savingacount = SavingAccount(123456655, "Nguyen Van A", 980000000000)
savingacount.display()
print("Tiền lãi:" ,savingacount.calculate_interest())

print("Thông tin khách hàng:")
customer = Customer("Nguyen Van A", "02-10-1994", "NguyenVanA@gmail.com", "0398183648")
customer.get_info()
