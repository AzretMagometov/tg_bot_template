# Используем аргумент для версии Python, по умолчанию 3.12.4
ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim as base

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Создаём пользователя для запуска приложения
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Создаём директорию /logs и устанавливаем права доступа
RUN mkdir /logs && chown appuser:appuser /logs

# Копируем только файл зависимостей для кеширования слоёв
COPY requirements.txt .

# Устанавливаем зависимости с использованием кеширования pip
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем остальной код приложения
COPY . .


# Переключаемся на непривилегированного пользователя
USER appuser

# Определяем команду запуска
CMD ["python", "-m", "bot.main"]
