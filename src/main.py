import os
from pathlib import Path

from src.data_reader import process_bank_search, read_transactions_from_csv, read_transactions_from_excel
from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")



def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню: ")
    print("1. Получить информацию о транзакциях из JSON-файла.")
    print("2. Получить информацию о транзакциях из CSV-файла.")
    print("3. Получить информацию о транзакциях из XLSX-файла.")

    choice = input("Пользователь: ")
    transactions = []
    if choice == "1":
        file_path = os.path.join(PATH_TO_FILE, "operations.json")
        file_path = Path(file_path)
        transactions = load_transactions(file_path)
        print("Программа: Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = os.path.join(PATH_TO_FILE, "transactions.csv")
        file_path = Path(file_path)
        transactions = read_transactions_from_csv(file_path)
        print("Программа: Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = os.path.join(PATH_TO_FILE, "transactions_excel.xlsx")
        file_path = Path(file_path)
        transactions = read_transactions_from_excel(file_path)
        print("Программа: Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")

    statuses = ["EXECUTED", "CANCELED", "PENDING"]


    while True:
        stat_in = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию. "
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь:"
            )
            .strip()
            .upper()
        )
        if stat_in in statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{stat_in}"')
            filtered_transactions = filter_by_state(transactions, stat_in)
            break
        else:
            print(f'Программа: Статус операции "{stat_in}" недоступен.')

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()

    if sort_choice == "да":
        next_choice = input("Сортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        if next_choice == "по возрастанию":
            filtered_transactions = sort_by_date(filtered_transactions, reverse=False)
        elif next_choice == "по убыванию":
            filtered_transactions = sort_by_date(filtered_transactions)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_choice == "да":
        filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
        description_filter = (
            input(
                "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь:"
            )
            .strip()
            .lower()
        )
        if description_filter == "да":
            search_str = input("Введите строку для поиска: ")
            filtered_transactions = process_bank_search(filtered_transactions, search_str)
            print("Распечатываю итоговый список транзакций...")

    if filtered_transactions:
        print(f"Программа: Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            # Извлекаем данные
            date_full = transaction.get("date", "")
            description = transaction.get("description", "")
            from_info = transaction.get("from", "")
            to_info = transaction.get("to", "")
            amount = transaction.get("operationAmount", {}).get("amount", "0.00")
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "USD")

            # Форматируем дату
            formatted_date = get_date(date_full)


            masked_from = "Без отправителя"
            masked_to = "Без получателя"

            from_parts = from_info.split()
            if from_parts:
                from_type_indicator = from_parts[0].lower()
                from_number = from_parts[-1]  # Последний элемент

                if from_type_indicator in ['maestro', 'mastercard', 'visa', 'mir']:
                    masked_from = get_mask_card_number(from_number)
                elif from_type_indicator == 'счет':
                    masked_from = get_mask_account(from_number)
                else:
                    masked_from = get_mask_card_number(from_number)  # Предполагаем, что это карта, если не счет

            to_parts = to_info.split()
            if to_parts:
                to_type_indicator = to_parts[0].lower()
                to_number = to_parts[-1]

                if to_type_indicator == 'счет':
                    masked_to = get_mask_account(to_number)
                elif to_type_indicator in ['maestro', 'mastercard', 'visa', 'mir']:
                    masked_to = get_mask_card_number(to_number)
                else:
                    masked_to = get_mask_card_number(to_number)


            # Первая строка: Дата и описание
            print(f"{formatted_date} {description}")

            # Вторая строка: Отправитель -> Получатель
            print(f"{masked_from} -> {masked_to}")

            # Третья строка: Сумма и валюта
            print(f"Сумма: {amount} {currency}")
            print("-" * 20)  # Разделитель между операциями для наглядности

    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
