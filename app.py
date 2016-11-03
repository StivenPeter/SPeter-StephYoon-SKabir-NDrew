from flask import Flask, render_template, request, url_for, session, redirect
import hashlib
import os
import sqlite3
import utils.accounts_builder
import hashlib
#import utils.story_builder
#accounts builder has issues

app = Flask(__name__)
app.secret_key = os.urandom(10)

#f = "data/data.db"
#db = sqlite3.connect(f)
#c = db.cursor()



@app.route("/")
@app.route("/main-menu")
def main():   
	if "user" not in session:
		return redirect(url_for('login'))
	else:
                print session['user']
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
                if dbPassword==hashlib.sha256(password).hexdigest():
                        session['user']=username            
                        return redirect(url_for('main'))
	return render_template('main-menu.html')

		




@app.route("/login/")

def login():   
        if 'user' in session:
                return redirect(url_for('main'))
        return render_template("login.html")


@app.route("/logout/", methods=['POST'])
def logout():
        if request.form['logout']=='Logout':
                session.pop('user')   
        return redirect(url_for('login'))

if(__name__ == "__main__"):
    app.debug = True
    app.run();
