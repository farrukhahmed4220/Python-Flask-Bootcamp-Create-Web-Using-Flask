from flask import Flask, render_template, redirect, flash, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kmykey'

class SimpleForm(FlaskForm):
	breed = StringField('What breed are you?')
	submit = SubmitField('Click Me.')



@app.route('/',methods=['GET','POST'])
def index():
	form = SimpleForm()

	if form.validate_on_submit():
		session['breed'] = form.breed.data
		flash(f"You Just changed your breed to: {session['breed']}")
		return redirect(url_for('index'))

	return render_template('pro.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)


