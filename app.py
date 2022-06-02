# python 3.10...
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# for the form.hidden method in register.html
app.config['SECRET_KEY']='thisisfirstflaskapp'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/register')
def register():
    form = RegistrationForm
    return render_template('register.html', title="register", form=form)

@app.route('/book')
def book():
    return render_template('book.html', title="book")

@app.route('/sites')
def sites():
    return render_template('sites.html', title="sites")

#individual sites
@app.route('/kakum')
def kakum():
    return render_template("kakum.html", title="kakum national park")

@app.route('/kwame')
def kwame():
    return render_template("kwame.html", title="Dr. Kwame Nkrumah Memorial Park".lower())

@app.route('/bosomtwe')
def bosomtwe():
    return render_template("bosomtwe.html", title="lake bosomtwe")

@app.route('/elmina')
def elmina():
    return render_template("elmina.html", title="elmina castle")

@app.route('/accra')
def accra():
    return render_template("accra.html", title="accra")

@app.route('/boti')
def boti():
    return render_template("boti.html", title="boti waterfalls")

@app.route('/flag')
def flag():
    return render_template("flag.html", title="flag staff house")

@app.route('/larabanga')
def larabanga():
    return render_template("larabanga.html", title="larabanga ancient mosque")

@app.route('/afadja')
def afadja():
    return render_template("afadja.html", title="mount afadja")




if __name__ == "__main__":
    app.run(debug=True)
