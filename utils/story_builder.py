import sqlite3
from datetime import datetime

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

def userExists(user):
	q = "SELECT userid FROM accounts WHERE accounts.userid = \'" + user + "\'"
	c.execute(q)
	if (c.fetchone()): # if userid exists
		return True
	else:
		return False

def storyExists(title):
	q = "SELECT title FROM stories WHERE stories.title = \'" + title + "\'"
	c.execute(q)
	if (c.fetchone()): # if title exists
		return True
	else:
		return False

def addNewStory(userid, title, cont):
	if userExists(userid) and (not storyExists(title)): # if user exists & title doesn't exist
		timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
		q = "INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')" % (userid, title, cont, timestam)
		c.execute(q)
		return True
	else:
		return False

# must check if title of story is valid!
# case: story title doesn't exist
def addContStory(userid, title, cont):
	if userExists(userid) and storyExists(title):
		timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
		q = 'INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')'%(userid,title,cont, timestam)
		c.execute(q)
		return True
	else:
		return False

# must check if title is valid!
# not printing out information
def getStory(title):
	if storyExists(title):
		q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.title = \' %s \'" % (title)
		results = c.execute(q)
		print results
		for entry in results:
			print "%s, %s, %s"%(entry[0], entry[1], entry[2])
		#return True
	else:
		return False

# not printing out information
def getStoriesFromUser(userid):
	if userExists(userid):
		q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.userid = \' %s \'" % (userid)
		results = c.execute(q)
		print results
		for entry in results:
			print entry
		return True
	else:
		return False

# returns object - should it return string?
# list of stories
def getLatestStory():
	q = "SELECT * FROM stories;"
	results = c.execute(q)
	latestrow = []
	time = 0
	for row in results:
		rowtime = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
		if (rowtime.timestamp() - time):
			time = rowtime.timestamp
			latestrow = row
		return latestrow

def test():
	#createStoryTable()
	#print addContStory("a", "c", "blah blah")
	#print(userExists("a"))
	#print(userExists("harambe"))
	#print addNewStory("a", "d", "la")
	#print(getLatestStory)
	#print storyExists("boo")
	#print storyExists("no")
	print getStoriesFromUser("a")
	save()
	close()

test()
