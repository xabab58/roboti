# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Создаем необходимые директории
RUN mkdir -p media static staticfiles

# Создаем .env файл с секретным ключом
RUN echo "SECRET_KEY=django-insecure-your-secret-key-here" > .env

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Выполняем миграции и создаем суперпользователя
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Открываем порт
EXPOSE 8000

# Устанавливаем переменные окружения
ENV DEBUG=1

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 