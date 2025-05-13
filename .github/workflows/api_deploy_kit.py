import base64
import requests
import os

# 🔹 Настройки
GITHUB_API_URL = "https://api.github.com"
REPO = "KeyMatrix/Quantum_PlazMatrix"
BRANCH = "main"
TOKEN = os.getenv("GITHUB_TOKEN")

def upload_file(file_path, target_path, commit_message):
    with open(file_path, "rb") as file:
        content = base64.b64encode(file.read()).decode("utf-8")
    
    url = f"{GITHUB_API_URL}/repos/{REPO}/contents/{target_path}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": commit_message,
        "content": content,
        "branch": BRANCH
    }
    
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"✅ Успешно загружено: {file_path} → {target_path}")
    else:
        print(f"❌ Ошибка: {response.status_code}, {response.json()}")

# 🔁 Основной запуск
if __name__ == "__main__":
    file_to_upload = "NeuralIndex.md"
    target_path = ".github/NeuralIndex.md"
    commit_message = "Add NeuralIndex via API"
    
    upload_file(file_to_upload, target_path, commit_message)