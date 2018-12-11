import os
import sqlite3

def check_name(s):
    if s == '' or (ord(s[0]) not in range(1040,1072)) or len(s)>15:
        return False
    for i in s[1::]:
        if ord(i) not in range(1072, 1104):
            return False
    return True

def check_number(s, nb):
    if len(s) != 6 or (nb and nb.find_note(number = s)):
        return False
    for i in s:
        if ord(i) not in range(48,58):
            return False
    return True

def check_natural(s):
    if not s:
        return False
    for i in s:
        if ord(i) not in range(48,58):
            return False
    return True

def check_bdate(s):
    if not len(s) == 10:
        # os.system('clear')
        # print('Неверный формат даты!')
        # print('Вы должны ввести 8 цифр в формате dd.mm.yyyy!')
        # print('Введите дату рождения в интервале [1900;2018]!')
        return False
    elif s[0:2] > '31' or s[0:2]=='00':
        # os.system('clear')
        # print('В месяце условно 31 день!')
        return False
    elif s[3:5] > '12' or s[3:5]=='00':
        # os.system('clear')
        # print('В году 12 месяцев!')
        return False
    elif int(s[6::]) not in range(1900, 2019):
        # os.system('clear')
        # print('Введите дату рождения в интервале [1900;2018]!')
        return False
    s = s[0:2]+s[3:5]+s[6::]
    for i in s:
        if ord(i) not in range(48,58):
            # os.system('clear')
            # print('Неверный формат даты!')
            # print('Дата содержит только цифры!')
            return False
    return True

def check_bd(bd_name):
    conn = sqlite3.connect('notebook.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master \
WHERE type='table' AND name='{}'".format(bd_name))
    if not c.fetchone():
        return False
    else:
        return True
    #c.close()
