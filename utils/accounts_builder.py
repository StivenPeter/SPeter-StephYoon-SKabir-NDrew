import sqlite3
import hashlib

def createAccountsTable():
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "CREATE TABLE accounts (userid TEXT, pass TEXT)"
    c.execute(q)
    save(db)
    close(db)

def save(db):
	db.commit()

def close(db):
	db.close()

def addAccount(user, password):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    check = "SELECT userid FROM accounts WHERE accounts.userid = \'" + user + "\'"
    c.execute(check)
    if not c.fetchone(): # if userid does not exist
        passw = hashlib.sha256(password).hexdigest()
        q = "INSERT INTO accounts VALUES (\'%s\',\'%s\')" % (user, passw)
        c.execute(q)
        save(db)
        close(db)
        return True
    else: # userid exists
        return False

def getAccountPass(user):
    f = "data/data.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    q = "SELECT pass FROM accounts WHERE accounts.userid = \'" + user + "\'"
    results = c.execute(q)
    for entry in results:
        return entry[0]
    save(db)
    close(db)

#createAccountsTable()
