# KVINT Test Job
Тестовое задание на вакансию Junior Python Developer. Алексей Кирпа.

## Структура
```
├── core                     # Основная директория проекта
│   ├── user_interfaces      # Интерфейсы взаимодействия с пользователем
│   │   └── telegram_bot.py  # Обработчики дейсвий пользователя в телеграм боте
│   ├── services.py          # Бизнес-логика
│   ├── settings.py          # Настройки проекта
│   └── types.py             # Используемые типы данных, содержит только класс с обработкой диалога
├── tests                    # Директория с тестами
│   ├── __init__.py
│   └── tests.py             # Тесты
├── env.example              # Переменные окружения 
├── .gitignore               # Игнорируемые файлы и директории
├── main.py                  # Файл запуска телеграм бота
├── README.md                # Инструкция по использованию проекта
└── requirements.txt         # Зависимости проекта
```

## Установка
1. Создать виртуальное окружение
```shell
python3 -m venv venv
```
2. Активировать виртуальное окружение
```shell
source venv/bin/activate
```
3. Установить зависимости
```shell
pip install -r requirements.txt
```
4. Скопировать файл с переменными окружения и прописать собственные переменные
```shell
cp .env.example .env
```
```dotenv
# Telegram Bot Token
TOKEN=ваш-телеграм-токен
```
## Запуск Телеграм-бота
```shell
python main.py
```
## Запуск тестов
```shell
coverage run -m unittest
```
## Проверка покрытия тестов
```shell
coverage report -m
```
