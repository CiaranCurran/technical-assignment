from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import WordCountForm
from app.scrape import countWord

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Word Count App')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = WordCountForm()
    if form.validate_on_submit():
        count = countWord(form.word.data, form.url.data)
        flash('The word "{}" appears in {} {} times'.format(
            form.word.data, form.url.data, count))
        return redirect(url_for('index'))
    return render_template('form.html', title='Word Count App', form=form)