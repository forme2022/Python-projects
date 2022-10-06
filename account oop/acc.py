from os import access


class Acc:
    def __init__(self,filepath):
        self.fp=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.fp, 'w') as file:
            file.write(str(self.balance))

# account=Acc("balance.txt")
# print(account.balance)
# account.withdraw(10)
# print(account.balance)
# account.commit()

class Checking(Acc):
    ''' this class generates checking account objects'''
    type="checking"

    def __init__(self,filepath, fee):
        Acc.__init__(self, filepath)
        self.feee=fee

    def transfer(self,amount):
        self.balance=self.balance - amount - self.feee

jacks_check=Checking("jack.txt", 1)
jacks_check.transfer(5)
print(jacks_check.balance)
jacks_check.commit()
print(jacks_check.type)

johns_check=Checking("john.txt", 1)
johns_check.transfer(5)
print(johns_check.balance)
johns_check.commit()
print(johns_check.type)
print(johns_check.__doc__)