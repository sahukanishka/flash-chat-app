from flask import Flask , render_template

from wtforms_fields import *

app = Flask(__name__)
app.secret_key = 'replace key later'


@app.route("/",methods=['GET','POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return "registered"


    return render_template('index.html', form = reg_form)

@app.route("/about")
def about():
    return render_template('about.html')
if __name__ == "__main__":

    app.run(debug=True,port=7000)
