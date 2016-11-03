import sqlite3
from datetime import datetime
import time

f = "../data/data.db"
db = sqlite3.connect(f)
c = db.cursor()

def createStoryTable():
	q = "CREATE TABLE stories (userid TEXT, title TEXT, cont TEXT, timestam TEXT)"
	c.execute(q)

def save():
	db.commit()

def close():
	db.close()

# True: user exists; False if not
def userExists(user):
	q = "SELECT userid FROM accounts WHERE accounts.userid = \'" + user + "\'"
	c.execute(q)
	if (c.fetchone()): # if userid exists
		return True
	else:
		return False

# True: story exists; False if not
def storyExists(title):
	q = "SELECT title FROM stories WHERE stories.title = \'" + title + "\'"
	c.execute(q)
	if (c.fetchone()): # if title exists
		return True
	else:
		return False

# returns True if story is added into story table; False if not
# adds new story with NEW title
def addNewStory(userid, title, cont):
	if userExists(userid) and (not storyExists(title)): # if user exists & title doesn't exist
		timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
		q = "INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')" % (userid, title, cont, timestam)
		c.execute(q)
		return True
	else:
		return False

# returns True if story is added into story table; False if not
# adds new entry with TITLE THAT EXISTS
def addContStory(userid, title, cont):
	if userExists(userid) and storyExists(title):
		timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
		q = 'INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')'%(userid,title,cont, timestam)
		c.execute(q)
		return True
	else:
		return False

# not printing out information
def getStory(title):
	if storyExists(title):
		q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.title = \'%s\'" % (title)
		results = c.execute(q)
		return results.fetchall()
	else:
		return False

# not printing out information
def getStoriesFromUser(userid):
	if userExists(userid):
		q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.userid = \'%s\'" % (userid)
		results = c.execute(q)
		return results.fetchall()
	else:
		return False

# returns object - should it return string?
# list of stories
def getLatestStory():
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
	save()
	close()

test()
