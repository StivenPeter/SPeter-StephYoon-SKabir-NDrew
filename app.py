from flask import Flask, render_template, request, url_for, session, redirect
import utils.login
import hashlib
import utils.Accounts_builder
import utils.Story_builder

app = Flask(__name__)
app.secret_key = os.urandom() #do we want to use this



@app.route("/")
@app.route("/main-menu")
def main():
	if "user" not in session:
		return redirect(url_for('login'))
	else:
		return render_template('main-menu.html')
		
	

@app.route("/auth/", methods=['POST'])
def register():
	if request.form["type"]=='register':
		Accounts_builder.AddAccount(request.form["user"],request.form["pass"])
	elif request.form['type']=='login':
		Accounts_builder.passcheck(request.form["user"],request.form["pass"]) #fxn not made yet
	return render_template('main-menu.html')
		




@app.route("/login")
def login():
    if 'user' in session:
        return redirect(url_for('main'))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if(__name__ == "__main__"):
    app.debug = True
    app.run();
