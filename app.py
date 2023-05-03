from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dfewfew123213rwdsgert34tgfd1234trgf"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example_2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    department_name = db.Column(db.String(50), db.ForeignKey('department.name'), nullable = False)
    is_head_of = db.Column(db.String, db.ForeignKey('department.name'), nullable=True)

class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable = False)
    location = db.Column(db.String(120), nullable = False)
    employees = db.relationship('Employee', backref = 'department')
    head = db.relationship('Employee', backref='head_of_department', uselist=False)

class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)

with app.app_context():
    db.create_all()

users = {"archie.andrews@email.com": "football4life", "veronica.lodge@email.com": "fashiondiva"}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", form=form, message="Successfully Logged In")
        return render_template("login.html", form=form, message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    return render_template("login.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
