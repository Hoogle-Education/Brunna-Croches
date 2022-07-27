
class Account :

  def __init__(self, holder, cpf) :
    self.holder = holder
    self.balance = 0.0
    self.cpf = cpf

  def deposit(amount):
    pass


acc = Account("Joao", "223.123.214-22")
acc.deposit(1000.0)
print(acc)