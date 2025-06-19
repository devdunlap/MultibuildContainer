from flask import render_template
from . import main
from .forms import NameForm

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/hello', methods=['GET', 'POST'])
def hello():
    form = NameForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
    return render_template('hello.html', form=form, name=name)