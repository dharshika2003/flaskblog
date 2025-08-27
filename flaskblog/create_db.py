from flaskblog import db

# Create all database tables
with db.app.app_context():
    db.create_all()

with app.app_context():
    posts = Post.query.all()

