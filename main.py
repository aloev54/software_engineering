from interface import Interface


def menu():
    '''Реализация пользовательского интерфейса'''
    interface = Interface()
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
            interface.add_detail()
        elif choice == "2":
            interface.remove_detail()
        elif choice == "3":
            interface.print_details()
        elif choice == "4":
            interface.filter_by_code()
        elif choice == "5":
            interface.total_count_by_code()
        elif choice == "6":
            interface.total_count_all()
        elif choice == "7":
            interface.sort_details()
        elif choice == "8":
            print("Выход из программы")
            break
        else:
            ("Некорректный выбор!")


if __name__ == "__main__":
    menu()
