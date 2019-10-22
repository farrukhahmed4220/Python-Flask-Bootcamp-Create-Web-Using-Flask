from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class InfoForm(FlaskForm):
	breed= StringField('What breed are you?', validators=[DataRequired()])
	submit=SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	form=InfoForm()

	if form.validate_on_submit():
		session['breed']=form.breed.data
		form.breed.data=''
		flash(f'Your choice of breed is {session["breed"]}')
		return redirect(url_for('index'))

	return render_template('pro.html', form=form)

# @app.route('/index2')
# def index2():
# 	return render_template('pro_ind2.html')

if __name__=='__main__':
	app.run(debug=True)