import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("YOUGILE_TOKEN")
BASE_URL = os.getenv("YOUGILE_URL", "https://yougile.com")

if not TOKEN:
    raise ValueError(
        "Ошибка: Токен YOUGILE_TOKEN не найден в переменных окружения!")
