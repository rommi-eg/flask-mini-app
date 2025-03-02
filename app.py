""" Мини-приложение для загрузки таблатур с сайта songsterr.com """

from flask import Flask, render_template, redirect, send_file
from core.forms import InputForm
from core.settings import SECRET_KEY, API
from core.songsterr import songsterr_parse, downloads


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def index_page():
    """ Эндпоинт для отображения формы и загрузки файла """

    form = InputForm()
    if form.validate_on_submit():
        url: str = form.url.data
        source, filename = songsterr_parse(url, API)
        if not (source is None and filename is None):
            return send_file(
                path_or_file=downloads(source),
                as_attachment=True,
                download_name=filename
            )
        else:
            return redirect('/')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
