import requests
from datetime import date
import time

code = input("Введите код валюты (например, USD): ").upper()
url = f"https://api.exchangerate-api.com/v4/latest/{code}"

try:
    response = requests.get(url)

    # Если статус не 200 (например, 404 — валюта не найдена)
    if response.status_code != 200:
        print("Ошибка: валюта не найдена или API недоступен.")
    else:
        data = response.json()
        rate = data["rates"]["RUB"]
        print(f"Курс {code} к RUB: {rate} рублей")
        print("Программа закроется через 4 секунды...")
        time.sleep(4)  # ждёт 4 секунды, потом закрывается

        with open("history.txt", "a") as f:
            f.write(f"{date.today()} {code} = {rate}\n")

except requests.exceptions.ConnectionError:
    print("Ошибка: нет интернета.")
except requests.exceptions.Timeout:
    print("Ошибка: сервер не отвечает.")
except Exception as e:
    print(f"Произошла ошибка: {e}")