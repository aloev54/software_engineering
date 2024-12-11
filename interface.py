from detail import Detail
from date import *


class Interface:

    def __init__(self):
        # Инициализируем список деталей
        self.details = [
            Detail(detail_code, cell_address, cell_count)
            for detail_code, cell_address, cell_count in database
        ]

    def add_detail(self):
        """Добавление записи (приемка)"""
        print("Добавление записи")
        detail_code = input("Введите код детали из 8 букв и цифр: ")
        cell_address = input("Введите адрес ячейки из 4 букв и цифр: ")
        cell_count = int(input("Введите количество: "))

        # Проверяем, существует ли запись с таким кодом и адресом
        for detail in self.details:
            if detail.detail_code == detail_code and detail.cell_address == cell_address:
                detail.cell_count += cell_count
                print("Количество обновлено.")
                return

        # Если записи нет, создаём новую
        new_detail = Detail(detail_code, cell_address, cell_count)
        self.details.append(new_detail)
        print("Запись добавлена.")

    def remove_detail(self):
        """Удаление записи (отгрузка)"""
        print("Удаление записи")
        detail_code = input("Введите код детали: ")
        cell_address = input("Введите адрес ячейки: ")
        cell_count = int(input("Введите количество: "))

        for detail in self.details:
            if detail.detail_code == detail_code and detail.cell_address == cell_address:
                if detail.cell_count > cell_count:
                    detail.cell_count -= cell_count
                    print("Количество обновлено.")
                elif detail.cell_count == cell_count:
                    self.details.remove(detail)
                    print("Запись удалена.")
                else:
                    print("Недостаточно деталей для отгрузки.")
                return
        print("Запись не найдена.")

    def print_details(self):
        """Вывод всех записей"""
        if not self.details:
            print("Список деталей пуст.")
            return
        print("Список деталей:")
        for detail in self.details:
            print(detail)

    def filter_by_code(self):
        """Фильтрация массива по коду детали"""
        code = input("Введите код детали для фильтрации: ")
        filtered = [
            detail for detail in self.details if detail.detail_code == code]
        if filtered:
            print("Найденные записи:")
            for detail in filtered:
                print(detail)
        else:
            print("Записей с таким кодом детали нет.")

    def total_count_by_code(self):
        """Поиск суммарного количества по коду детали"""
        code = input("Введите код детали: ")
        total = sum(
            detail.cell_count for detail in self.details if detail.detail_code == code)
        print(f"Суммарное количество деталей с кодом {code}: {total}")

    def total_count_all(self):
        """Поиск суммарного количества по всем категориям"""
        total = sum(detail.cell_count for detail in self.details)
        print(f"Суммарное количество всех деталей: {total}")

    def sort_details(self):
        """Сортировка по выбранному полю"""
        print("Выберите поле для сортировки:")
        print("1 - Код детали\n2 - Адрес ячейки\n3 - Количество")
        choice = int(input("Введите номер поля: "))
        if choice == 1:
            self.details.sort(key=lambda x: x.detail_code)
        elif choice == 2:
            self.details.sort(key=lambda x: x.cell_address)
        elif choice == 3:
            self.details.sort(key=lambda x: x.cell_count)
        else:
            print("Неверный выбор.")
            return
        print("Список отсортирован.")
        self.print_details()
