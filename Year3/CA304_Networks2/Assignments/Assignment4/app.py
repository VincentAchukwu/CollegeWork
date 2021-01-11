import json, csv
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

products = [
    {
        "title": "Anakin's Saber",
        "content": "Unavailable (Buried in sand)"
    },
    {
        "title": "Kenobi's Saber",
        "content": "High ground Galactic Credits"
    },
    {
        "title": "Full Mandalorian Armour",
        "content": "2,000 Galactic Credits"
    },
    {
        "title": "Han Solo's Blaster",
        "content": "400 Galactic Credits"
    },
    {
        "title": "Star Destroyer",
        "content": "1,000,000 Galactic Credits"
    }
]

# specifying CSV and JSON files to read from and write to, respectively
csvFile = "allegiance.csv"
jsonFile = "allegiance.json"

# route to home page
@app.route("/")
def index():
    return render_template("index.html")

# route to form page for user to POST name
@app.route('/formtest', methods=['GET', "POST"])
def login():

    # message initially empty
    message = ''

    # if user makes a POST request
    if request.method == 'POST':
        # access data inside
        username = request.form.get('username')

        # if username is not empty (i.e user typed something), 
        # bring them to hello.html displaying message with their name
        if username:
            return render_template('hello.html', message="Hello there, {}.".format(username))

        # else redirect user back to the form to get their name
        else:
            return redirect('/formtest')

    # else the user is brought to the form page since it's a GET request
    return render_template('login.html', message="Do, or do not. There is no try!")

# displays allegiances in raw JSON format
@app.route('/allegiances')
def makeJson():
    data = {}

    # first reading the csv file and adding info to dictionary
    with open(csvFile, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['Name']
            data[key] = rows

    # then writing the contents of the data dictionary to JSON file
    with open(jsonFile, "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    # setting the mimetype to application/json
    response = app.response_class(
        response=json.dumps(data, indent=4),
        status=200,
        mimetype='application/json'
    )

    return response

# displays the allegiances in a new html page via html table
@app.route('/allegiancedashboard')
def displayJedi():

    # reads the JSON file and then pass it to the allegianceDashboard html page
    with open("allegiance.json", "r") as jsonf:
        jediOrSith = json.load(jsonf)

    return render_template("allegianceDashboard.html", jediOrSith=jediOrSith)



# ################## EXTRA ##################
# extra functionality: - sqlite database for blog posts
#                      - extra route (/shop for shop.html)

# route to shop page
@app.route("/shop")
def shop():

    # products stored in list of ditionaries
    return render_template("shop.html", products=products)

# creating file called "posts.db", storing blog posts in database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# creation of database
class BlogPost(db.Model):

    # making blogposts unique via id, and setting other attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # if author not specified, set defualt as N/A
    author = db.Column(db.String(20), nullable=False, default='N/A')
    # sets date at which post was made
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # print out whenever we create new blog post so we recognise it
    def __repr__(self):
        return 'Blog post ' + str(self.id)

# route for displaying blog posts (Jedi and Sith Archive)
@app.route('/posts', methods=['GET', 'POST'])
def posts():

    # if POST, we want to read all data from form, then send it to database
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        newPost = BlogPost(title=post_title, content=post_content, author=post_author)
        # adding new post to the current session of database
        db.session.add(newPost)
        # saves the database "permanently", so even when exiting/re-running program, database still stores previous blog posts
        db.session.commit()
        # redirecting back to same page
        return redirect('/posts')
    # else we're not POSTing
    else:
        # getting all blog posts from database (ordered by data posted)
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

# route for creating a new post
@app.route('/posts/new', methods=['GET', 'POST'])
def newPost():
    # if user is making a POST request (i.e making a new post)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        # adding the new post to the database, and commiting it
        newPost = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(newPost)
        db.session.commit()
        return redirect('/posts')

    # else user wants to view posts (GET request)
    else:
        return render_template('newPost.html')

# route for editing a blog post (editing means we POST)
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    # creates a new blog post instance in database
    post = BlogPost.query.get_or_404(id)

    # if user posting changes, we over-write the current post by querying to appropriate attributes
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        # commit changes
        db.session.commit()
        # then redirect to post page
        return redirect('/posts')

    # else we display the edit page for the user to edit a post
    else:
        return render_template('edit.html', post=post)

# deletes blog post from database based on id
@app.route('/posts/delete/<int:id>')
def delete(id):
    # gets post to delete via id if it exists (don't want it to break)
    post = BlogPost.query.get_or_404(id)
    # deletes from database
    db.session.delete(post)
    # commits update to database
    db.session.commit()
    # redirect to same page
    return redirect('/posts')

# checks if we have db, if not, db.create_all()
# then while running, enable debugging
if __name__ == '__main__':
    import os
    if not os.path.exists('db.sqlite'):
            db.create_all()
    app.run(debug=True)
