from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Nicole'}
    posts = [
        {
            'author': {'nickname': 'Alum Post 1'},
            'body': 'This is the body of the first post.'
        },
        {
            'author': {'nickname': 'Teacher Post 2'},
            'body': 'This is the body of the second post.'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)



@app.route('/about')
def about():
    return render_template('about.html',
                           title='About')