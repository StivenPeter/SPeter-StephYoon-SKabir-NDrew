import sqlite3
from datetime import datetime
import time



def createStoryTable():
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	q = "CREATE TABLE stories (userid TEXT, title TEXT, cont TEXT, timestam TEXT)"
	c.execute(q)

def save():
	db.commit()

def close():
	db.close()

# True: user exists; False if not
def userExists(user):
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	q = "SELECT userid FROM accounts WHERE accounts.userid = \'" + user + "\'"
	c.execute(q)
	if (c.fetchone()): # if userid exists
                db.commit()
                db.close()
		return True
	else:
                db.commit()
                db.close()
		return False

# True: story exists; False if not
def storyExists(title):
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	q = "SELECT title FROM stories WHERE stories.title = \'" + title + "\'"
	c.execute(q)
	if (c.fetchone()): # if title exists
                db.commit()
                db.close()
		return True
	else:
                db.commit()
                db.close()
		return False
	

# returns True if story is added into story table; False if not
# adds new story with NEW title
def addNewStory(userid, title, cont):
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	if userExists(userid) and (not storyExists(title)): # if user exists & title doesn't exist
		timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
		q = "INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')" % (userid, title, cont, timestam)
		c.execute(q)
		db.commit()
                db.close()
		return True
	else:
                db.commit()
                db.close()
		return False

# returns True if story is added into story table; False if not
# adds new entry with TITLE THAT EXISTS
def addContStory(userid, title, cont):
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	if userExists(userid) and storyExists(title):
		timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
		q = 'INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')'%(userid,title,cont, timestam)
		c.execute(q)
		db.commit()
                db.close()
		return True
	else:
                db.commit()
                db.close()
		return False

# not printing out information
def getStory(title):
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	if storyExists(title):
		q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.title = \'%s\'" % (title)
		results = c.execute(q)
		db.commit()
                db.close()
		return results.fetchall()
	else:
                db.commit()
                db.close()
		return False

# not printing out information
def getStoriesFromUser(userid):
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	if userExists(userid):
		q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.userid = \'%s\'" % (userid)
		results = c.execute(q)
		db.commit()
                db.close()
		return results.fetchall()
	else:
                db.commit()
                db.close()
		return False

# returns object - should it return string?
# list of stories
def getLatestStory():
        f = "data/data.db"
        db = sqlite3.connect(f)
        c = db.cursor()
	q = "SELECT * FROM stories;"
	results = c.execute(q)
	return results.fetchall()[-1]

def test():
	#createStoryTable()
	#print addContStory("a", "c", "blah blah")
	#print(userExists("a"))
	#print(userExists("harambe"))
	#print addNewStory("a", "kjslhkgfdh", "la")
	#print(getLatestStory)
	#print storyExists("boo")
	#print storyExists("no")
	#print getStoriesFromUser("a")
	print getLatestStory()


