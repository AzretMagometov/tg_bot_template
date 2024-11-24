import logging
from utils.logging import setup_logging_base_config


def main():
    # Настройка логирования
    setup_logging_base_config()

    # Пример логов
    logging.debug("Это сообщение отладки.")
    logging.info("Это информационное сообщение.")
    logging.warning("Это предупреждающее сообщение.")
    logging.error("Это сообщение об ошибке.")
    logging.critical("Это критическое сообщение.")


if __name__ == "__main__":
    main()
