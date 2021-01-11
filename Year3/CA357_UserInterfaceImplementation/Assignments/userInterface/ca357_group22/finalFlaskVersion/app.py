import json
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, current_user, logout_user, LoginManager, UserMixin
# Forms Page take classes from file formsPage
from formsPage import LoginForm, RegistrationForm
app = Flask(__name__)
# this secret key is needed for regestering and loggin in users
app.config["SECRET_KEY"] = "33ab45e64b227041277b2c71483cc154"
login_manager = LoginManager(app)
# JSON dataset for books, reviews, and group members
# Books from: https://github.com/bvaughn/infinite-list-reflow-examples/blob/master/books.json
books = "amazonBooks.json"
reviews = "reviews.json"
members = "members.json"

# storing bookset in data variable
with open(books, "r") as jsonf:
    bookDataset = json.load(jsonf)

# storing reviews in data variable
with open(reviews, "r") as reviewf:
    reviewSet = json.load(reviewf)

# storing member data in data variable
with open(members, "r") as membersf:
    memberSet = json.load(membersf)

# route to home page
@app.route("/")
def index():
    return render_template("index.html", books=bookDataset)

# route to search results page
@app.route('/searchResults', methods=['GET', "POST"])
def results():

    match = []

    # if user makes a POST request
    if request.method == 'POST':
        # access data inside
        query = request.form.get('query')
        qSet = set(query.lower().split())
        for book in bookDataset:
            currTags = set(book["tags"])
            if len(qSet.intersection(currTags)) > 0:
                match.append(book)

        # bring them to results.html displaying query results
        return render_template('results.html', query=query, matches=match, books=bookDataset)

    # handling "contact us" in footer
    return redirect("/")

# route for displaying all books
@app.route("/books")
def viewBooks():

    # for now, showing first 10 books for testing purposes...
    return render_template("books.html", books=bookDataset)

# route for displaying a book with reviews
@app.route('/books/book/<int:bid>', methods=['GET', 'POST'])
def book(bid):

    for b in bookDataset:
        if bid == b["bookID"]:
            break

    return render_template("book.html", book=b, reviews=reviewSet, bID=bid)

# route for displaying "About Us" info
@app.route('/about')
def about_page():
    return render_template("about.html", memberData=memberSet)

# route for displaying "Contact Us" info
@app.route('/contact')
def contact_us():
    return render_template("contact.html", memberData=memberSet)


@app.route('/contact_submit')
def contact_submit():
    return render_template("contact_submit.html", memberData=memberSet)



# creating file called "forums.db", storing forum posts in database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forums.db'
db = SQLAlchemy(app)

# creation of database
class ForumPost(db.Model):

    # making forum posts unique via id, and setting other attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # if author not specified, set default as N/A
    author = db.Column(db.String(20), nullable=False, default='N/A')
    # sets date at which post was made
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # print out whenever we create new forum post so we recognise it
    def __repr__(self):
        return 'Forum post ' + str(self.id)

# route for displaying forum posts (Jedi and Sith Archive)
@app.route('/forums', methods=['GET', 'POST'])
def forums():

    # obtaining user input from HTML and adding to database
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        newPost = ForumPost(title=post_title, content=post_content, author=post_author)
        # adding new post to the current session of database
        db.session.add(newPost)
        # saves the database "permanently", so even when exiting/re-running program, 
        # database still stores record of forum posts
        db.session.commit()
        # redirecting back to same page
        return redirect('/forums')
    # else we're not POSTing
    else:
        # getting all forum posts from database (ordered by data posted)
        all_posts = ForumPost.query.order_by(ForumPost.date_posted).all()
        return render_template('forums.html', posts=all_posts)

# route for creating a new post
@app.route('/forums/new', methods=['GET', 'POST'])
def newPost():
    # if user is making a POST request (i.e making a new post)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        # adding the new post to the database, and commiting it
        newPost = ForumPost(title=post_title, content=post_content, author=post_author)
        db.session.add(newPost)
        db.session.commit()
        return redirect('/forums')

    # else user is making GET request to go to new page to create posts
    else:
        return render_template('newPost.html')

# route for editing a forum post (editing means we POST)
@app.route('/forums/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # creates a new forum post instance in database
    post = ForumPost.query.get_or_404(id)

    # if user posting changes, we over-write the current post by querying to appropriate attributes
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        # commit changes
        db.session.commit()
        # then redirect to post page
        return redirect('/forums')

    # else we display the edit page for the user to edit a post
    else:
        return render_template('editPost.html', post=post)

# deletes forum post from database based on id
@app.route('/forums/delete/<int:id>')
def delete(id):
    # gets post to delete via id if it exists (don't want it to break)
    post = ForumPost.query.get_or_404(id)
    # deletes from database
    db.session.delete(post)
    # commits update to database
    db.session.commit()
    # redirect to same page
    return redirect('/forums')



# creation of account database
class User(db.Model, UserMixin):
    # making forum posts unique via id, and setting other attributes
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # print out whenever we create new forum post so we recognise it
    def __repr__(self):
        return  f"User('{self.username}', {self.email})"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# redirects user to a login form
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user == None:
            flash(f"We cannot find your information in the database please try again", "danger")
        elif not (user.username == form.username.data) & (user.email == form.email.data) & (user.password == form.password.data):
            flash(f"We cannot find your information in the database please try again", "danger")
        else:
            login_user(user, remember=False)
            flash(f"Welcome Back {form.username.data}!", "success")
            return redirect(url_for("index"))
    return render_template("login.html", form=form)

# redirects user to a registeration form
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data) != None or User.query.filter_by(email=form.email.data) != None:
            flash(f"Sorry the username/email you have chosen have already been used please try again with a different username/email", "danger")
        else:
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=False)
            flash(f"You have sucessfully created an account {form.username.data}!", "success")
            return redirect(url_for("index"))
    return render_template("register.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logOut():
    logout_user()
    flash(f"You have sucessfully logged out of your account", "success")
    return redirect(url_for("index"))



# checks if we have db, if not, db.create_all()
# then debugging
if __name__ == '__main__':
    import os
    if not os.path.exists('db.sqlite'):
            db.create_all()
    app.run(debug=True)
