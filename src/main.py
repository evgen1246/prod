import os

from src.utils import load_transactions


def main:
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню: ')
    print('1. Получить информацию о транзакциях из JSON-файла.')
    print('2. Получить информацию о транзакциях из CSV-файла.')
    print('3. Получить информацию о транзакциях из XLSX-файла.')

    choice = input("Пользователь: ")
    if choice == '1':
        file_path = os.path.join("operations.json")
        transactions = load_transactions(file_path)
        print('Программа: Для обработки выбран JSON-файл.')
    elif choice == '2':
        file_path = os.path.join('transactions.csv')