from flask import Flask, render_template, redirect, url_for
from scrap import bbc_scrap, toi_scrap
app = Flask(__name__)

app.config['SECRET_KEY'] = '497b2582064cd81ddcfddd3fa18e5cd7'

bbc_news = bbc_scrap()
toi_news = toi_scrap()


@app.route('/')
@app.route('/bbc')
def bbc():
    return render_template('bbc.html', bbc_news=bbc_news)


@app.route('/toi')
def toi():
    return render_template('toi.html', toi_news=toi_news)


if __name__ == '__main__':
    app.run(debug=True)