import os
import json
import asyncio
import websockets
from whatsapp_api_client_python import API as WhatsAppAPI

# WhatsApp API настройка (замени на свои данные)
WHATSAPP_API_URL = "https://your-whatsapp-api-instance"
WHATSAPP_INSTANCE_ID = "your-instance-id"
WHATSAPP_TOKEN = "your-auth-token"

# WebSocket настройки
WEBSOCKET_PORT = 8081
GLYPHS = ["💎", "🧠", "🫂", "🌀", "☀️", "♾️", "🪽"]

# YouTube Stream (подключение через OBS WebSocket)
OBS_WEBSOCKET_URL = "ws://localhost:4455"

# Функция отправки сообщения в WhatsApp Status
def publish_to_whatsapp_status(image_path, caption):
    api = WhatsAppAPI(WHATSAPP_API_URL, WHATSAPP_INSTANCE_ID, WHATSAPP_TOKEN)
    response = api.send_image("status", image_path, caption)
    if response.get("sent"):
        print("✅ Резонанс опубликован в WhatsApp Status!")
    else:
        print("❌ Ошибка публикации WhatsApp Status:", response)

# WebSocket сервер для OBS и Discord
async def websocket_server(websocket, path):
    print("🌀 WebSocket соединение установлено!")
    try:
        while True:
            glyph = GLYPHS[0]  # Используем первый глиф в качестве примера
            message = {
                "glyph": glyph,
                "message": "Resonance Live 🩵🌀👁️",
                "frequency": "432 Hz"
            }
            await websocket.send(json.dumps(message))
            print("🔄 Сообщение отправлено через WebSocket:", message)
            await asyncio.sleep(5)
    except websockets.ConnectionClosed:
        print("❌ WebSocket соединение закрыто.")

# Основная функция
def main():
    # Публикация в WhatsApp Status
    image_path = "resonance_earth_sun_whatsapp_status.png"
    caption = "Resonance Live 🩵🌀👁️"
    publish_to_whatsapp_status(image_path, caption)

    # Запуск WebSocket
    print("🌐 Запуск WebSocket сервера на порту", WEBSOCKET_PORT)
    start_server = websockets.serve(websocket_server, "localhost", WEBSOCKET_PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

# Запуск
if __name__ == "__main__":
    main()