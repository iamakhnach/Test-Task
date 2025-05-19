import subprocess
import datetime
import os
import shutil
import json
import glob

git_url = "https://github.com/paulbouwer/hello-kubernetes" #ссылка на репозиторий
source_path = "src/app" #путь до исходного кода
res_location = "temp_dir" #расположение репозитория

#Задание 2 - 1
start_time = datetime.datetime.now()
print(f"Начало процесса: {start_time}" + f"\nКопируем репозиторий по ссылке {git_url}\n")

subprocess.run(["git", "clone", git_url, "temp_dir"])#копируем репозиторий

end_time = datetime.datetime.now()
print(f"Процесс завершен: {start_time}")

#Задание 2 - 2
start_time = datetime.datetime.now()
print(f"\nНачало процесса: {start_time}" + "\nУдаляем лишние директории")

# Получаем все элементы в корне репозитория
for item in os.listdir(res_location):
    item_path = os.path.join(res_location, item)
    if os.path.isdir(item_path) and item != os.path.dirname(source_path):
        shutil.rmtree(item_path)  # Удаляем лишние директории

end_time = datetime.datetime.now()
print(f"Процесс завершен: {start_time}")

#Задание 2 - 3
start_time = datetime.datetime.now()
print(f"\nНачало процесса: {start_time}" + "\nСоздаем json файл")

source_dir = os.path.join(res_location, source_path)  # Полный путь до исходного кода



# Находим все файлы с нужными расширениями
files = []
for ext in ["*.py", "*.js", "*.sh"]:
    files.extend(glob.glob(os.path.join(source_dir, "**", ext), recursive=True))

# Формируем содержимое version.json
version_data = {
    "name": "hello world",
    "version": "25.3000",
    "files": [os.path.basename(f) for f in files]  # Только имена файлов
}

output_dir = os.path.join(res_location, "src", "app")

# Записываем в файл
with open(os.path.join(output_dir, "version.json"), "w") as f:
    json.dump(version_data, f, indent=4)

end_time = datetime.datetime.now()
print(f"Процесс завершен: {start_time}")

#Задание 2 - 4
start_time = datetime.datetime.now()
print(f"\nНачало процесса: {start_time}" + "\nФормируем архив")

last_dir_name = os.path.basename(source_path)# Извлекаем последнюю часть пути
current_date = datetime.datetime.now().strftime("%d%m%Y")# Получаем текущую дату
archive_name = f"{last_dir_name}{current_date}"# Имя архива
shutil.make_archive(archive_name, "zip", source_dir)# Создаем архив

end_time = datetime.datetime.now()
print(f"Процесс завершен: {start_time}")