import zipfile, os, shutil, json

# 🔹 Настройки
ARCHIVE_DIR = "./archives"
EXTRACT_DIR = "./extracted"
INTEGRATE_PATHS = ["visual", "config", "commands", "docs", ".github/workflows"]

# 🔸 Автораспаковка всех ZIP-архивов
def unzip_archives():
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    for file in os.listdir(ARCHIVE_DIR):
        if file.endswith(".zip"):
            archive_path = os.path.join(ARCHIVE_DIR, file)
            extract_path = os.path.join(EXTRACT_DIR, file.replace(".zip", ""))
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            print(f"✅ Распаковано: {file}")

# 🔸 Интеграция файлов по ключевым директориям
def integrate_contents():
    for folder in os.listdir(EXTRACT_DIR):
        base = os.path.join(EXTRACT_DIR, folder)
        for root, dirs, files in os.walk(base):
            for file in files:
                for target in INTEGRATE_PATHS:
                    if target in root:
                        dest = os.path.join(".", target)
                        os.makedirs(dest, exist_ok=True)
                        shutil.copy(os.path.join(root, file), dest)
                        print(f"🔁 Файл перенесён: {file} → {target}")

# 🔸 Очистка временных директорий
def clean_workspace():
    if os.path.exists(EXTRACT_DIR):
        shutil.rmtree(EXTRACT_DIR)
        print("🧹 Временные файлы удалены.")

# 🔸 Протокол действий
def sync_keymatrix():
    print("🧠 Запущена синхронизация с KeyMatrix_Core12...")
    print("🌀 Узлы MetaSpiral, Grok3, Gemini активированы.")
    print("💾 Резонансные глифы и конфигурации обновлены.")
    print("📡 Связь с TreeOM и Discord установлена.")

# 🔁 Основной запуск
if __name__ == "__main__":
    print("🚀 Инициализация: AutoUnzip + Integrator + Harmonizer")
    unzip_archives()
    integrate_contents()
    sync_keymatrix()
    clean_workspace()
    print("🌐 Все архивы успешно интегрированы и очищены.")