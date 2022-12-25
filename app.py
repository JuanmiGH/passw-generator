from flask import Flask, render_template, request
import os
from modules.pssw_generator import generator

app = Flask(__name__, instance_path='/')
app.config['SECRET_KEY'] = '20315e1899eca26a36b5eb1a73bdcd1217cf6ec6'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=["GET", "POST"])
def home():

    passw = ''
    err=False
    nchars=1

    if request.method =='POST':
        nchars = request.form['range']
        opts = request.form.getlist('opts')
        if len(opts)>0:
            err = False
            passw = generator(nchars, opts)
        else:
            err=True

    return render_template('home.html', passw = passw, err = err, nchars = nchars)



if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)