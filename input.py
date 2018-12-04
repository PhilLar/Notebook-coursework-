import os
from check import *

def input_name():
    n = ''
    while True:
        name = input('Ввод: ')
        # check
        if check_name(name) is False:
            print('Неверный формат имени!')
            print('Первая буква заглавная!')
            print('Имена должны содержать только символы кириллицы!')
            print('Имена содержат не более 15 символов!')
            print("Введите 'q', чтобы выйти в меню или нажмите 'enter', чтобы попробовать снова")
            n = input()
            if n =='q':
                return [name, n]
            else:
                os.system('clear')
                continue
        else:
            return [name, n]


def input_number(nb = None):
    n = ''
    while True:
        os.system('clear')
        print('Введите номер телефона [6 цифр, уникальный]:')
        number = input()
        # check
        if check_number(number, nb) is False:
            print('Неверный формат номера!')
            print('Номер содержит 6 цифр!')
            print('Номер должен быть уникальным!')
            print("Введите 'q', чтобы выйти в меню или нажмите 'enter', чтобы попробовать снова")
            n = input()
            if n =='q':
                return [number, n]
            else:
                continue
        else:
            return [number, n]

def input_bdate():
    n = ''
    while True:
        os.system('clear')
        print('Введите дату рождения [dd.mm.yyyy]:')
        bdate = input()
        # check
        if check_bdate(bdate) is False:
            print('Неверный формат даты!')
            print('Вы должны ввести 8 цифр в формате dd.mm.yyyy!')
            print('Введите дату рождения в интервале [1900;2018]!')
            print("Введите 'q', чтобы выйти в меню или нажмите 'enter', чтобы попробовать снова")
            n = input()
            if n =='q':
                return [bdate, n]
            else:
                continue
        else:
            return [bdate, n]
