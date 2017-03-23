import shelve
class loginDetails:
	def __init__(self, iUsername = '', iPassword = ''):
		self.username = iUsername
		self.password = iPassword
		

	def addUserCommandLine():
		newUser = input('User: ')
		newPass = input('Pass: ')

		newCreds = loginDetails(newUser, newPass)
		print(newCreds)
		with shelve.open('logindb','c') as db:
			db[newCreds.username] = newCreds
		print('all done')
	def addUserBox(userN,passN):
		newCreds = loginDetails(userN, passN)
		with shelve.open('logindb','c') as db:
			if userN not in db.keys():

				db[newCreds.username] = newCreds
				return "success"
			else:
				return "error"

	def check(user,passs):
		with shelve.open('logindb','r') as db:
			if user in db:
				userCreds = db[user]
				print(userCreds)
				if userCreds.password == passs:
					return 'login successful'
				else:
					return 'password incorrect'
			else:
				return 'username not found'


if __name__ == "__main__":
	pass