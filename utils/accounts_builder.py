import sqlite3
import hashlib

f = "data/data.db"
db = sqlite3.connect(f)
c = db.cursor()

def createAccountsTable():
	q = "CREATE TABLE accounts (userid TEXT, pass TEXT);"
	c.execute(q)

def saveAndClose():
	db.commit()
	db.close()

def addAccount(user, password):
	check = "SELECT userid FROM accounts WHERE accounts.userid = " + user + ";"
	results = c.execute(check)
	if len(results) == 0:
		passw = hashlib.sha256(password).hexdigest()
		q = 'INSERT INTO accounts VALUES (%s,%s);'%(userid,passw)
		c.execute(q)
		return True
	else:
		return False

def getAccountPass(user):
	q = "SELECT pass FROM accounts WHERE accounts.userid = " + user + ";"
	results = c.execute(check)
	return results[0][0]
