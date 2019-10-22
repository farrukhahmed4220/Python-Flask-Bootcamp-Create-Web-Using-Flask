# from flask import Flask, render_template, redirect, flash, session, url_for
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'kmykey'

# class SimpleForm(FlaskForm):
# 	submit = SubmitField('Click Me.')


# @app.route('/',methods=['GET','POST'])
# def index():
# 	form = SimpleForm()

# 	if form.validate_on_submit():
# 		flash('You Just Click the button !')
# 		return redirect(url_for('index'))

# 	return render_template('flash.html', form=form)


# if __name__ == '__main__':
# 	app.run(debug=True)


from flask import (Flask, 
					render_template, 
					flash, redirect, 
					url_for)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class SimpleForm(FlaskForm):
	submit= SubmitField('Click Me.')

@app.route('/', methods=['GET', 'POST'])
def index():
	form= SimpleForm()

	if form.validate_on_submit():
		flash('Hey ! you just click this button.')
		flash('How are you?')
		flash('How was your day?')
		return redirect(url_for('index'))

	return render_template('flash.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)
