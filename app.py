from flask import Flask, render_template, request, url_for, session, redirect
import hashlib
import os
import sqlite3
import utils.accounts_builder
import utils.story_builder
import hashlib


app = Flask(__name__)
app.secret_key = os.urandom(10)



@app.route("/")
@app.route("/main-menu")
def main():
	if "user" not in session:
		return redirect(url_for('login'))
	elif 'message' in session:
                message=session['message']
                session['message']=''
                return render_template('main-menu.html', message=message)
	else:
                Stories=utils.story_builder.getStoriesFromUser(session['user'])
                Titles=[]
                for x in Stories:
                        if x[1] not in Titles:          
                                Titles.append(x[1])
                print Titles
		return render_template('main-menu.html', list=Titles)
			
@app.route("/authenticate/", methods=['POST'])
def register():
        username=request.form["user"]
        password=request.form["password"]
	if request.form["enter"]=='Register':
                if username=='' or password =='':
                        session['message']='Cant login without characters XD'

                        return redirect(url_for('main'))    
                        
                elif utils.accounts_builder.checkAccount(username)==False:
                        session['message']='Username exists'
                        return redirect(url_for('login'))           
                result=utils.accounts_builder.addAccount(username,password)
		if result==True:
                        session['user']=username
                        return redirect(url_for('main'))
                else:
                        return render_template('main-menu.html')                 		
	elif request.form['enter']=='Login':
                dbPassword=utils.accounts_builder.getAccountPass(username)
                if dbPassword==hashlib.sha256(password).hexdigest() and dbPassword != 'None':
                        session['user']=username
                        return redirect(url_for('main'))
                else:
                        session['message']='Username or Password is incorrect'
                        redirect(url_for('login'))     
	return redirect(url_for('login'))

		

@app.route("/login/")
def login():    
        if 'user' in session:
                return redirect(url_for('main'))
        elif 'message' in session:
                message=session['message']
                session['message']=''
                return render_template("login.html", message=message)
        
        return render_template("login.html")

@app.route("/logout/", methods=['POST'])
def logout():
        if request.form['logout']=='Logout':
                session.pop('user')
                
        return redirect(url_for('login'))


@app.route("/story-menu/", methods=['POST'])
def storymenu():
        if "user" not in session:
		return redirect(url_for('login'))
	Stories=utils.story_builder.getAll()
	Titles=[]
	for x in Stories:
                if x[1] not in Titles:          
                        Titles.append(x[1])
	
        return render_template("story-menu.html",list=Titles)

@app.route("/story-form/", methods=['POST'])
def storyform():
        if 'user' not in session:
                return redirect(url_for('main'))
        elif 'selection' not in request.form:             
                author=session['user']
                title=request.form['title']
                session['addStoryTitle']=title
                d={'prevUserId':author, 'timestamp':'','prevContent':''}
                if utils.story_builder.storyExists(title)!=False:
                        session['message']='Story Title Exists'
                        return redirect(url_for('main'))
                return render_template("story-form.html", d=d, title=title, chapterdata='First Chapter')
        else:
                title = request.form['selection']
                Storydata=utils.story_builder.getStory(title)
                print Storydata[0]
                d={'prevUserId':Storydata[-1][0], 'timestamp':Storydata[-1][2],'prevContent':Storydata[-1][2]}
                session['addStoryTitle']=title
                return render_template("story-form.html", d=d, title=title, chapterdata='')
                
                
                
        return render_template("story-form.html")

@app.route("/story-display/", methods=['POST'])
def storydisplay():
        print request.form
        if 'user' not in session:
                return redirect(url_for('main'))
        elif request.form['enter']=='Publish':
                title=session['addStoryTitle']
                author = session['user']
                content=request.form['newSubmission']
                session['addStoryTitle']=''
                if utils.story_builder.storyExists(title) == False:
                        utils.story_builder.addNewStory(author, title, content)
                elif authInStory(title,author):
                        session['message']='You have already contributed to the selected Story'
                        return redirect(url_for('main'))
                        
                else:
                        utils.story_builder.addContStory(author, title, content)
        story = utils.story_builder.getStory(title)                  
        return render_template("story-display.html",list=story, title=title)


def authInStory(title,author):
        story = utils.story_builder.getStory(title)
        for x in story:
                if x[0]==author:
                        return True
        return False

if(__name__ == "__main__"):
    app.debug = True
    app.run();
