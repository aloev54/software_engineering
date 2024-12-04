from detail import Detail
from date import *


def add_detail():
    '''Функция добавления детали'''
    code = input("Введите код детали: ")
    address = input("Введите адрес ячейки")
    count = input("Введите количство в ячейке")
    database.append(Detail(code, address, count))


def remove_detail():
    '''Функция удаления детали'''
    code = input("Введите код детали: ")
    global database
    database = [detail for detail in database if detail.detail_code != code]
    print(f"Деталь с кодом {code} успешно удалена!")


def print_details():
    if database:
        for detail in database:
            print(detail)
    else:
        print("Склад пуст!")