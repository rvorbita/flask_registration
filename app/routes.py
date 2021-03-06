from flask import render_template, flash, redirect, url_for
from app import app

from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():

    user = {'username': 'Mac'}
    posts = [
        {
            'authors': {'username': 'Paul'},
            'body': 'Beautiful World'
        }, 
        {
            'authors': {'username': 'Roger'},
            'body': 'Mobile Legend Bang bang'
        }
    ]

    return render_template('index.html', user=user, posts=posts)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        flash(f"Login request for user {form.username.data} {form.remember_me.data}")

        return redirect(url_for('index'))

    return render_template('login.html', form=form)