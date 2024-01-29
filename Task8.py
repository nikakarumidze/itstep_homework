#Task 1
array_multiplicator = lambda arr, num: [item * num for item in arr]

print(array_multiplicator([1,2,3],2))

#Task 2
filter_case_array = lambda arr: len(list(filter(lambda str: str[0].isupper(), arr )))

print(filter_case_array(['Asd','asd','Baba','bob']))

#Task 3
def sum_nums(arr):
    sum_positive_nums = sum(filter(lambda num: num > 0,arr))
    sum_negative_nums = sum(filter(lambda num: num < 0,arr))
    return f"""
        sum positive: {sum_positive_nums}
        sum negative: {sum_negative_nums}
        """

print(sum_nums([1,-2,3,-4]))

#Task 4
class Bank:
    def __init__(self):
        self.users = []  # Array to store user information

    def create_account(self, user):
        self.users.append(user)
        print(f"Account created for {user.name} with account number {user.account_number}")

    def deposit(self, account_number, amount):
        user = self.find_user(account_number)
        try:
            user.balance += amount
            print(f"Deposited ${amount} into account {account_number}. New balance: ${user.balance}")
        except:
            print(f"Account {account_number} not found.")

    def check_balance(self, account_number):
        user = self.find_user(account_number)
        try:
            print(f"Balance in account {account_number}: ${user.balance}")
        except:
            print(f"Account {account_number} not found.")

    def find_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None


class User:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

bank = Bank()

# Create user
user1 = User("Gio", "12345678")
bank.create_account(user1)

# Deposit and withdraw
bank.deposit("12345678", 1000)

# Check balance
bank.check_balance("12345678")
