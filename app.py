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
		return render_template('main-menu.html')
			
@app.route("/authenticate/", methods=['POST'])
def register():
        username=request.form["user"]
        password=request.form["password"]
	if request.form["enter"]=='Register':
                result=utils.accounts_builder.addAccount(username,password)
		session['user']=username
		if result==True:
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

        
        return render_template("story-menu.html")

@app.route("/story-form/", methods=['POST'])
def storyform():
        if 'user' not in session:
                return redirect(url_for('main'))
        author=session['user']
        title=request.form['title']
        session['addStoryTitle']=title
        d={'prevUserId':author, 'timestamp':'','prevContent':''}
        if utils.story_builder.storyExists(title)!=False:
                session['message']='Story Title Exists'
                return redirect(url_for('main'))     
        return render_template("story-form.html", d=d, title=title, chapterdata='First Chapter')

@app.route("/story-display/", methods=['POST'])
def storydisplay():
        print request.form
        if 'user' not in session:
                return redirect(url_for('main'))
        elif request.form['enter']=='Publish':
                d={'author':session['user'], 'timestamp':'','content':request.form['newSubmission']}
                
        return render_template("story-display.html",chapterdict=d )


if(__name__ == "__main__"):
    app.debug = True
    app.run();
