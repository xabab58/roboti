# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменные окружения
ENV DEBUG=1
ENV DJANGO_SETTINGS_MODULE=wine_and_dine.settings
ENV SECRET_KEY=django-insecure-your-secret-key-here
ENV STATIC_ROOT=/app/staticfiles
ENV STATIC_URL=/static/
ENV MEDIA_ROOT=/app/media
ENV MEDIA_URL=/media/

# Создаем необходимые директории
RUN mkdir -p media staticfiles

# Копируем проект
COPY . .

# Собираем статические файлы и выполняем миграции
RUN python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 