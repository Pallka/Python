from flask import Flask, render_template, request
import random

app = Flask(__name__)

def home(message):
    return render_template('index.html', message=message)

def guess_number(user_number, target_number):
    return f"You win! Answer is {target_number}" if user_number == target_number else "Nope, try one more time"

@app.route("/", methods=["GET", "POST"])
def index():
    target_number = random.randint(1, 10) 
    message = ''
    if request.method == "POST":
        try:
            user_number = int(request.form["user-number"])
            if target_number < user_number:
                message = 'Number is less'
            elif target_number > user_number:
                message = 'Number is more'
            else:
                message = guess_number(user_number, target_number)
        except ValueError:
            message = "Enter an integer number"
    return home(message)

if __name__ == '__main__':
    app.run(debug=True)