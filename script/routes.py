from flask import render_template
from script import app, pages
from script.projects import my_projects
from datetime import datetime, date
# from script.forms import RegistrationForm, LoginForm
# from script.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def first(): 
    return render_template('home.html')

@app.route("/home")
def home(): 
    return render_template('home.html')

@app.route("/resume")
def resume(): 
    return render_template('resume.html', title = 'Resume & Testimonials')

@app.route("/blog")
def blog(): 
    posts = [p for p in pages if "date_posted" in p.meta]
    sorted_pages = sorted(posts, reverse=True, key=lambda page: datetime.strptime(page.meta["date_posted"], "%d %b %y"))
    last_post = sorted_pages[0]
    def days_since (d1):
        d1 = datetime.strptime(d1, "%d %b %y")
        d2_str = datetime.strftime(date.today(), "%d %b %y")
        d2 = datetime.strptime(d2_str, "%d %b %y")
        return abs((d2 - d1).days)
    days_since_posted = days_since(last_post.meta["date_posted"])
    return render_template('blog.html', posts= sorted_pages, days_since_posted= days_since_posted, title = 'Blog') 

# @app.route("/blog/factor-modelling")
# def blog_1(): 
#     filtered_posts  = []
#     tags = {'Alpha', 'Factor Modelling'}
#     for post in blog_posts: 
#         if tags.isdisjoint(post['tags']) == False: 
#             filtered_posts.append(post)
#     return render_template('blog.html', posts= filtered_posts, title = 'Blog') 

# @app.route("/blog/asset-allocation")
# def blog_2(): 
#     filtered_posts  = []
#     tags = {'Asset Allocation', 'Markovitz'}
#     for post in blog_posts: 
#         if tags.isdisjoint(post['tags']) == False: 
#             filtered_posts.append(post)
#     return render_template('blog.html', posts= filtered_posts, title = 'Blog') 

# @app.route("/blog/stock-selection")
# def blog_3(): 
#     filtered_posts  = []
#     tags = {'Alpha', 'Investing', 'Stock Market', 'Equities'}
#     for post in blog_posts: 
#         if tags.isdisjoint(post['tags']) == False: 
#             filtered_posts.append(post)
#     return render_template('blog.html', posts= filtered_posts, title = 'Blog') 

# @app.route("/blog/machine-learning")
# def blog_4(): 
#     filtered_posts  = []
#     tags = {'Feature Engineering', 'Deep Learning', 'SVD', 'Neural Net'}
#     for post in blog_posts: 
#         if tags.isdisjoint(post['tags']) == False: 
#             filtered_posts.append(post)
#     return render_template('blog.html', posts= filtered_posts, title = 'Blog') 

# @app.route("/blog/monte-carlo")
# def blog_5(): 
#     filtered_posts  = []
#     tags = {'Risk Management', 'Scenario Analysis', 'Stress Testing'}
#     for post in blog_posts: 
#         if tags.isdisjoint(post['tags']) == False:  
#             filtered_posts.append(post)
#     return render_template('blog.html', posts= filtered_posts, title = 'Blog') 

# @app.route("/blog/article/<int:post_id>")
# def article(post_id): 
#     if post_id == 1: 
#         post_prev = {}
#         post = blog_posts[post_id-1]
#         post_next = blog_posts[post_id]
#     elif post_id == len(blog_posts):
#         post_prev = blog_posts[post_id-2]
#         post = blog_posts[post_id-1]
#         post_next = {}
#     else: 
#         post_prev = blog_posts[post_id-2]
#         post = blog_posts[post_id-1]
#         post_next = blog_posts[post_id]
#     return render_template('article.html', post= post, post_prev = post_prev, post_next = post_next, title = post['title']) 

@app.route('/blog/articles/<path:path>.html')
def article(path):
    post = pages.get_or_404(path)
    return render_template('article.html', post=post)

@app.route("/projects")
def projects(): 
    last_commit = my_projects[0]
    return render_template('projects.html', projects= my_projects, last_commit= last_commit, title = 'Projects') 

@app.route("/projects/project/<int:commit_id>")
def commit(commit_id): 
    project = my_projects[commit_id -1]
    return render_template('commit.html', project= project, title = project['title']) 

@app.route("/contact")
def contact(): 
    return render_template('contact.html', title = 'Contact')

# @app.route("/register", methods = ['GET', 'POST'])
# def register(): 
#     if current_user.is_authenticated: 
#         return redirect(url_for('home'))
#     form = RegistrationForm()
#     if form.validate_on_submit(): 
#         hashed_password = crypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email = form.email.data, password = hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash('Your account has been created! You are now able to log in.', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title = 'Register', form = form)

# @app.route("/login", methods = ['GET', 'POST'])
# def login(): 
#     if current_user.is_authenticated: 
#         return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit(): 
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and crypt.check_password_hash(user.password, form.password.data): 
#             login_user(user, remember = form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('home'))
#         else: 
#             flash('Login unsuccessful. Please check username and password.', 'danger')
#     return render_template('login.html', title = 'Login', form = form)

# @app.route("/logout")
# def logout(): 
#     logout_user()
#     return redirect(url_for('home'))

# @app.route("/account")
# @login_required
# def account():
#     return render_template('account.html', title='Account')