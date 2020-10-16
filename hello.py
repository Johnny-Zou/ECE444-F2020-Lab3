from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
import re

class NameForm(Form):
	name = StringField('What is your name?', validators=[DataRequired()])
	email = StringField('What is your UofT Email address?', validators=[DataRequired(),Email(message="Please enter a valid email address")])
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
        	flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        if re.search("utoronto",form.email.data):
        	session['UofTEmail'] = True
        else:
        	session['UofTEmail'] = False
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), valid_email=session.get('UofTEmail'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

# error code routes
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')