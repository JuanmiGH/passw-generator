from flask import Flask, render_template
import os
import secrets
import string
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

app = Flask(__name__, instance_path='/')
app.config['SECRET_KEY'] = '20315e1899eca26a36b5eb1a73bdcd1217cf6ec6'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=["GET", "POST"])
def home():

    return render_template('home.html')



if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)