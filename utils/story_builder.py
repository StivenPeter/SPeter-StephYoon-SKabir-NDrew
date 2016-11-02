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

# must check if userid is valid!
def addNewStory(userid, title, cont):
	timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
	q = "INSERT INTO stories VALUES (\'%s\',\'%s\',\'%s\',\'%s\')" % (userid, title, cont, timestam)
	c.execute(q)

# must check if userid & title of story are valid!
# must add to pre-exisitng content, not add another entry
def addContStory(userid, title, cont):
	timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
	q = 'INSERT INTO stories VALUES (%s,%s,%s,%s);'%(userid,title,cont, timestam)
	c.execute(q)

# must check if title is valid!
def getStory(title):
	q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.title = " + title
	results = c.execute(q)
	return results[0][0]

# must check if userid is valid!
def getStoriesFromUser(userid):
	q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.userid = " + userid
	results = c.execute(q)
	return results[0][0]

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
	addContStory("a", "boo", "blah blah")
	save()
	close()

test()
