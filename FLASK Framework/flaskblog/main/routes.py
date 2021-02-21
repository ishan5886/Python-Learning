from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home') # HomePage can be navigated to by either '/' or '/home'
def homepage():
    # return '<h1>Home Page<h1>'
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    # return '<h1>About Page<h1>'
    return render_template('about.html', title='About')

