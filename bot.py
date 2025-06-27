from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("f9LHodD0cOKUwU3M9gFI9E_LzkT0rOafU1Gky1RGDH0PEyp71-zHvQLffC_Cey6AAVj5GYMpY1PVRX97OWQI")

MAX_API_URL = "https://botapi.myteam.mail.ru/v1"

def send_message(chat_id, text, keyboard=None):
    url = f"{MAX_API_URL}/messages/sendText"
    headers = {"Authorization": f"Bearer {BOT_TOKEN}"}
    payload = {
        "chatId": chat_id,
        "text": text
    }
    if keyboard:
        payload["inlineKeyboardMarkup"] = keyboard
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


# Главное меню с кнопками
def main_menu():
    return {
        "inlineKeyboard": [
            [
                {"text": "🔥 ТОП", "callbackData": "top"},
                {"text": "🆕 НОВИНКИ", "callbackData": "new"}
            ],
            [
                {"text": "🎧 Моя музыка", "callbackData": "user_music"},
                {"text": "🔎 Поиск", "callbackData": "search"}
            ]
        ]
    }

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Получено:", data)

    message = data.get("message")
    callback = data.get("callbackQuery")

    if message:
        chat_id = message["chat"]["chatId"]
        text = message.get("text", "")

        if text == "/start":
            send_message(chat_id, "Привет! Выберите, что хотите 🎶", main_menu())
        else:
            send_message(chat_id, "Нажмите кнопку ниже 👇", main_menu())

    elif callback:
        chat_id = callback["message"]["chat"]["chatId"]
        data = callback["callbackData"]

        if data == "top":
            send_message(chat_id, "Вот ТОП-10 треков 🔥 (заглушка)")
        elif data == "new":
            send_message(chat_id, "Свежие новинки 🎵 (заглушка)")
        elif data == "user_music":
            send_message(chat_id, "Введите свою ссылку на VK или ID:")
        elif data == "search":
            send_message(chat_id, "Введите имя трека или исполнителя:")
        else:
            send_message(chat_id, "Неизвестная команда 😐")

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
