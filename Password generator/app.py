from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += secrets.choice(characters)
    return password

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        try:
            length = int(request.form["length"])
            if length < 8 or length > 100:
                password = "The length should be from 1 to 100"
            else:
                password = generate_password(length)
        except ValueError:
            password = "Enter int number"
    return render_template("index.html", password=password)
