import os

from src.data_reader import process_bank_search
from src.utils import load_transactions

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню: ")
    print("1. Получить информацию о транзакциях из JSON-файла.")
    print("2. Получить информацию о транзакциях из CSV-файла.")
    print("3. Получить информацию о транзакциях из XLSX-файла.")

    choice = input("Пользователь: ")
    if choice == "1":
        file_path = os.path.join(PATH_TO_FILE, "operations.json")
        transactions = load_transactions(file_path)
        print("Программа: Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = os.path.join(PATH_TO_FILE, "transactions.csv")
        transactions = load_transactions(file_path)
        print("Программа: Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = os.path.join(PATH_TO_FILE, "transactions_excel.xlsx")
        transactions = load_transactions(file_path)
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
            filtered_transactions = [t for t in transactions if str(t.get("state", "")).upper() == stat_in]
            break
        else:
            print(f'Программа: Статус операции "{stat_in}" недоступен.')

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()

    if sort_choice == "да":
        next_choice = input("Сортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        if next_choice == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x["date"])
        elif next_choice == "по убыванию":
            filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_choice == "да":
        filtered_transactions = [
            t
            for t in filtered_transactions
            if "operationAmount" in t and t["operationAmount"]["currency"]["code"] == "RUB"
        ]
        description_filter = (
            input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            .strip()
            .lower()
        )
        if description_filter == "да":
            search_str = input("Введите строку для поиска: ")
            filtered_transactions = process_bank_search(filtered_transactions, search_str)
        print("Распечатываю итоговый список транзакций...")

        if filtered_transactions:
            print(f"Программа: Всего банковских операций в выборке: {len(filtered_transactions)}]")
            for transaction in filtered_transactions:
                date = transaction.get("date", "")
                description = transaction.get("description", "")
                account = transaction.get("account", "")[-4:]  # последние 4 цифры счёта
                amount = transaction.get("operationAmount", {}).get("amount", "")
                currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")

                print(f"{date} {description}")
                print(f"Счет **{account}")
                print(f"Сумма: {amount} {currency} \n")
        else:
            print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == "__main__":
    main()