The extra functionality I added to the assignment is the use of Bootstrap CSS and 
Javascript, and SQLite database storing blog posts which the user can post to.
I also included an extra route for an extra page (shop.html) which is simply just a 
list of products from app.py which I pass into the render_template method for the 
shop() route (line 106). Also, when displaying the allegiance dashboard, I have 
jinja ensuring that if a Jedi/Sith has no allegiance, it displays "N/A" for them.
(This baffles Kenobi as he says "Impossible. Perhaps the archives are incomplete.")


SQLITE Feature:
I initialise the SQLite database by importing SQLALCHEMY, and store blog posts in 
the posts.db file. First, I specify the path where the database is stored, and use 
SQLite to define the relative path to app.py. Then I link the app to the database.
After that, I create the class to model the database to store the blog posts. Each 
blog post has a primary key, title, content, author, and the date posted. I also 
implemented a date and time format via jinja (posts.html, line 39) for better 
readability. The date and time specify the date and time when a user made a new 
post. This isn't updated when the user decides to edit the post.

I defined a posts method which allows GET and POSTS methods. POSTS allows users to 
edit or delete the posts, GET allows the user to view the posts, which is by default.
If the user makes a POST request, the databases' attributes are updated and the user 
is redirected back to the posts page and the new post will be there. Else, the user 
made a GET request and they simply are brought to the posts page.

If the user wants to create a new post, similar to editing post, the user types in 
data to forms and is added to the database. After submitting, the user is redirected 
to the posts page and the new post is available to view.

If the user wants to edit a post, the post is edited via its id (primary key), and 
the posts' title, author, and contents can be edited and posted again.

If the user wants to delete a post, similar to the edit post method via the primary 
key, the post is deleted. The contents of each attribute of that post is simply 
deleted. The user is then redirected back to the posts page, and the post is no 
longer available.


BOOTSTRAP Feature:
In base.html, I implement features common throughout each webpage and jinja allows 
each webpage to display what base.html has, as well as having more unique features 
per web page. I used Bootstrap CSS and JavaScript to improve the appearance of the 
site, linking the CSS at the head, and the JavaScript at the bottom of the body tag 
(allowing the site to render the HTML elements first before the JavaScript). I also 
linked a custom CSS file for specific features such as reversing the text colour of 
each h1 tag based on its background (i.e bright background=dark text, and vice 
versa), and disabling the hover feature for each dropdown item in the navbar.


Link to video:
https://www.youtube.com/watch?v=izgNufFIHjg
