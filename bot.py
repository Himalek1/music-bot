from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("f9LHodD0cOJev6J16ssKmNdvSpVrXNBjJl3l_LO7fKmXwKlh7T8IbahQ-J023tAJsO9b9cecaTRh3vEaJhdq")  # Токен, который ты получил от @MasterBot в MAX

# Отвечаем на входящее сообщение
def send_message(chat_id, text):
    url = f"https://botapi.myteam.mail.ru/v1/messages/sendText"
    headers = {"Authorization": f"Bearer {BOT_TOKEN}"}
    payload = {
        "chatId": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data.get("message", {}).get("chat", {}).get("chatId")

    if chat_id:
        send_message(chat_id, "Привет! Это музыкальный бот 🤖")

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

