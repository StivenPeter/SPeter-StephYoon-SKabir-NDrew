import sqlite3
import hashlib

f = "../data/data.db"
db = sqlite3.connect(f)
c = db.cursor()

def createAccountsTable():
	q = "CREATE TABLE accounts (userid TEXT, pass TEXT)"
	c.execute(q)

def save():
	db.commit()

def close():
	db.close()

def addAccount(user, password):
	check = "SELECT userid FROM accounts WHERE accounts.userid = \'" + user + "\'"
	c.execute(check)
	if not c.fetchone(): # if userid does not exist
		passw = hashlib.sha256(password).hexdigest()
		q = "INSERT INTO accounts VALUES (\'%s\',\'%s\')" % (user, passw)
		c.execute(q)
		return True
	else: # userid exists
		return False

def getAccountPass(user):
	q = "SELECT pass FROM accounts WHERE accounts.userid = \'" + user + "\'"
	results = c.execute(q);
	for entry in results:
		return entry[0]
		
'''
def test():
	#createAccountsTable()
	print(addAccount("a", "a"))
	save()
	print(getAccountPass("a"))
	close()

test()
'''
