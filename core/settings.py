import os
from dotenv import load_dotenv


load_dotenv()


API = 'https://www.songsterr.com/api/meta/'
SECRET_KEY = os.getenv('SECRET_KEY') or 'any_key'
