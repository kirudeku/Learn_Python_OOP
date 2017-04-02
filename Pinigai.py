class Bank:
	
	def __init__(self, name, bank_name, account_type, account_funds):
		self.name = name
		self.bank_name = bank_name
		self.account_type = account_type
		self.account_funds = account_funds

	def __str__(self):
		return "{}. Customer's name: {}. Account type: {}. Owner of this account has funds of {} money.".format(self.bank_name, self.name, self.account_type, self.account_funds)

class money_moves(Bank):

	def withdrawal(self, withdraw):
		if self.account_funds <= 10 and withdraw <= self.account_funds:
			print ("You should consider depositing money! Your current funds: {}".format (self.account_funds))
			self.account_funds -= withdraw
		elif withdraw > self.account_funds:
			print ("You cannot withdraw {} money. You can withdraw a maximum of {} money.".format(withdraw, self.account_funds))
		else:
			self.account_funds -= withdraw

	def deposition(self, deposit):
		self.account_funds += deposit

edgaras = money_moves("Edgaras", "BankA", "Checkings", 100)
edgaras.withdrawal(91)
print(edgaras)

edgaras.withdrawal(1)
print(edgaras)

edgaras.withdrawal(10)
print(edgaras)
