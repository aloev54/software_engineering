from func import *


def menu():
    '''Реализация пользовательского интерфейса'''
    while True:
        print("\nМеню:")
        print("1. Добавить запись (приемка)")
        print("2. Удалить запись (отгрузка)")
        print("3. Вывести весь склад")
        print("4. Фильтровать по коду детали")
        print("5. Суммарное количество по коду детали")
        print("6. Суммарное количество всех деталей")
        print("7. Сортировать склад")
        print("8. Выйти")

        choice = input("Выберите действие (1-8): ")

        if choice == "1":
            add_detail()
        elif choice == "2":
            remove_detail()
        elif choice == "3":
            print_details()
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            print("Выход из программы")
            break
        else:
            ("Некорректный выбор!")


if __name__ == "__main__":
    menu()
