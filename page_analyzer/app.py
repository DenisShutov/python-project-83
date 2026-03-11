import os
from urllib.parse import urlparse

import validators
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)

from url_repository import UrlRepository

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

repo = UrlRepository()


@app.route("/")
def index():
    messages = get_flashed_messages(with_categories=True)
    return render_template('index.html', messages=messages)


@app.route("/urls", methods=['POST'])
def add_url():
    url = request.form.get('url', '')
    normalize_url = normalize(url)

    if not validators.url(normalize_url) or len(normalize_url) > 255:
        flash('Неверный URl', 'danger')
        return render_template(
            'index.html',
            url=url
        ), 422
    
    url_data = repo.find_by_name(normalize_url)
    if url_data:
        id = url_data['id']
        flash('Данный URL уже добален', 'info')
        return redirect(url_for('show_url', id=id))
    
    id = repo.save(normalize_url)
    
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('show_url', id=id))


def normalize(url):
    parsed = urlparse(url)
    return f'{parsed.scheme}://{parsed.netloc}'.lower()


@app.route('/urls/<int:id>')
def show_url(id):
    messages = get_flashed_messages(with_categories=True)
    url = repo.find(id)
    return render_template(
        'show.html',
        url=url,
        messages=messages
    )


@app.route('/urls')
def get_urls():
    urls = (repo.get_content())
    urls.reverse()
    return render_template(
        'urls.html',
        urls=urls
    )