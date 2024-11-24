# bot/utils/logging.py

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from typing import Optional

from dotenv import load_dotenv, find_dotenv


def setup_logging_base_config(path: Optional[str] = None):
    """
    Настраивает базовую конфигурацию логирования.

    :param path: Путь к файлу логов. Если None, используется переменная окружения LOG_FILE_PATH или 'logs/app.log'.
    """
    # Загрузка переменных окружения из .env файла

    if path is None:
        # Попытка получить путь из переменной окружения
        path = os.getenv('LOG_FILE_PATH')

    if path is None or path.strip() == '':
        # Если переменная не задана или пуста, используем стандартный путь
        # Используем sys.path[0] для определения корневой директории проекта
        project_root = os.path.abspath(os.path.join(sys.path[0], os.pardir))
        log_directory = os.path.join(project_root, 'logs')
        log_file = os.path.join(log_directory, 'app.log')
    else:
        # Нормализуем путь и объединяем с корневой директорией
        normalized_path = os.path.normpath(path)
        project_root = os.path.abspath(os.path.join(sys.path[0], os.pardir))
        log_file = os.path.join(project_root, normalized_path)
        log_directory = os.path.dirname(log_file) or project_root

    # Проверка, что log_file не указывает на директорию
    if os.path.isdir(log_file):
        logging.error(f"Путь к файлу логов указывает на директорию: {log_file}")
        raise IsADirectoryError(f"Путь к файлу логов указывает на директорию: {log_file}")

    # Создание директории для логов, если она не существует
    try:
        os.makedirs(log_directory, exist_ok=True)
    except OSError as e:
        logging.basicConfig(level=logging.ERROR)
        logging.error(f"Не удалось создать директорию для логов: {e}")
        raise

    # Настройка базового конфигурации логирования
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=2),
            logging.StreamHandler()  # Вывод логов в консоль
        ]
    )
