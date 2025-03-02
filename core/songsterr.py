""" Модуль для парсинга сайта songsterr.com """

import re
from pathlib import Path
from io import BytesIO
import requests


def get(url: str):
    """ Возвращает результат GET запроса """

    return requests.get(url, timeout=1.5)


def songsterr_parse(url: str, api: str) -> tuple:
    """ Парсит данные с сайта songsterr """

    try:
        song_item = re.findall(r'\d+', url)[0]
        response: str = get(f'{api}{song_item}').json()
        source: str = response['source']
        filename: str= (
            f'{response['artist']} -'
            f' {response['title']}'
            f'{Path(source).suffix}'
        )
        return (source, filename)
    except (KeyError, IndexError) as e:
        print(f'Error: {e}')
        return (None, None)


def downloads(url: str):
    """ Заоружает файл в память """

    return BytesIO(get(url).content)
