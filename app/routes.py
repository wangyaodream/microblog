from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'wangyao'}
    return render_template('index.html', user=user)


@app.route('/loop')
def loop_index():
    user = {'username': 'wangyao'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('loop_index.html', title='Home', user=user, posts=posts)
