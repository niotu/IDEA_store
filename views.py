from flask import render_template
from flask import Flask


app = Flask(__name__)

@app.route('/')
def base():  # put application's code here
    return render_template('base.html')

def main():
    app.run()