from flask import Flask , render_template

from wtforms_fields import *
from models import *

app = Flask(__name__)
app.secret_key = 'replace key later'

#configure database

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ozawkdoyvqhipc:f35523972b309aab0ab3a73978616ee325ed23ae5808eb143c1174a77ff7a56d@ec2-54-197-234-117.compute-1.amazonaws.com:5432/drrtj2v553ai9'

db = SQLAlchemy(app)

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
