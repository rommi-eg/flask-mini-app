from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    """ Класс формы запроса """

    url = StringField(
        'url',
        validators=[DataRequired()]
    )
