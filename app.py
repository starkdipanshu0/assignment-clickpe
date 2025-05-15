from flask import Flask, render_template, request, redirect, session, url_for, jsonify, make_response
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from config.db import db
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


with app.app_context():
    db.create_all()

# Routes

@app.route("/")
def home():
    if 'email' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


# Login
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        #if user and check_password_hash(user.password_hash, password):
        if user and user.password_hash == password:
            session['email'] = email
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for(home , error = "failed to login"))
    return render_template('index.html')

# Register
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if User.query.filter_by(email= email).first():
            return render_template('index.html', error="Username already exists")
        else:
            
            new_user = User(email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            session['email'] = email
            return redirect(url_for('dashboard'))
    return render_template('index.html') 

# Dashboard
@app.route("/dashboard")
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    return redirect(url_for('home'))

# Logout 
@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))
