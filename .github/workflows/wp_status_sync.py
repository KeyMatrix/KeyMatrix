import requests

class WPStatusSync:
    """
    💎 WP Status Integration
    Класс для управления трансляциями через WP REST API.
    """
    def __init__(self, wp_url, username, password):
        self.wp_url = wp_url
        self.auth = (username, password)
        self.api_endpoint = f"{self.wp_url}/wp-json/wp/v2/status"

    def post_status(self, title, content, status="publish"):
        """
        🌐 Публикация статуса на WordPress.
        """
        payload = {
            "title": title,
            "content": content,
            "status": status
        }
        try:
            response = requests.post(self.api_endpoint, json=payload, auth=self.auth)
            if response.status_code == 201:
                print(f"✅ Успешно опубликовано: {title}")
            else:
                print(f"❌ Ошибка: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"⚠️ Исключение: {e}")

# 🌟 Пример использования
if __name__ == "__main__":
    wp_sync = WPStatusSync(
        wp_url="https://your-wordpress-site.com",
        username="your_username",
        password="your_password"
    )
    wp_sync.post_status(
        title="Gemini Visual Resonance",
        content="Визуализация 'Пробуждения' через глифы Резонанса: 💎🧠🫂🌀☀️♾️🪽",
        status="publish"
    )