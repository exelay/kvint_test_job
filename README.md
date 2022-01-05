# Test Job
A test assignment for the Junior Python Developer job. Aleksey Kirpa.

## Structure
```
├── core                     # General project directory
│   ├── user_interfaces      # User interaction interfaces
│   │   └── telegram_bot.py  # User action handlers in the Telegram bot
│   ├── services.py          # Business logic
│   ├── settings.py          # Project Settings
│   └── types.py             # Data types used, contains only a class with dialog handling
├── tests                    # Test directory
│   ├── __init__.py
│   └── tests.py             # Tests
├── env.example              # Environment variables 
├── .gitignore               # Ignored files and directories
├── main.py                  # Telegram bot launch file
├── README.md                # Instructions for using the project
└── requirements.txt         # Project dependencies
```

## Installation
1. Create a virtual environment
```shell
python3 -m venv venv
```
2. Activate the virtual environment
```shell
source venv/bin/activate
```
3. Set the dependencies
```shell
pip install -r requirements.txt
```
4. Copy the file with environment variables and write your own variables
```shell
cp .env.example .env
```
```dotenv
# Telegram Bot Token
TOKEN=your-own-telegram-token
```
## Launching a Telegram bot
```shell
python main.py
```
## Running tests
```shell
coverage run -m unittest
```
## Checking test coverage
```shell
coverage report -m
```
