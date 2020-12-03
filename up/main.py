# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    breed = StringField('What Breed are you?')
    submit = SubmitField('Submit')


@app.route('/form', methods=['GET', 'POST'])
def form():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''
    return render_template('default/pages/form.html', form=form, breed=breed)


@app.route('/')
def index():

    return render_template('default/pages/index.html', title='Home Page')


@app.route('/admin')
def admin():
    return render_template('admin/login.html')


@app.route('/dashboard')
def dashboard():
    email = request.args.get('email')

    return render_template('admin/dashboard.html', email=email)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
