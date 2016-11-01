import sqlite3
from datetime import datetime

f = "data/data.db" 
db = sqlite3.connect(f) 
c = db.cursor() 

def  CreateStoryTable():
	q = "CREATE TABLE stories (userid TEXT, title TEXT, cont TEXT, timestam TEXT);"
	c.execute(q) 
def SaveAndClose(): 
	db.commit()
	db.close()

def AddStory(userid, title, cont):
	timestam = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S') 
	q = 'INSERT INTO stories VALUES (%s,%s,%s,%s);'%(userid,title,cont, timestam)
	c.execute(q)
def GetStory(title):
	q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.title = " + title + ";"
	results = c.execute(q)
	return results
def GetStoriesFromUser(userid):
	q = "SELECT userid, title, cont, timestam FROM stories WHERE stories.userid = " + userid + ";"
	results = c.execute(q)
	return results
def GetLatestStory(): 
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