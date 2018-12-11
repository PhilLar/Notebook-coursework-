import os
import random
import sqlite3
#import codecs

from Note import Note
from check import *

class NoteList:
    def __init__(self):
        self.head = None
        self.new_head = None

    def fill_list(self, note):
        #f_note = Note(note.name, note.sname, note.number, note.bdate)
        if(self.head==None):
            self.head = note
        else:
            tmp = self.head
            while(tmp.next):
                tmp = tmp.next
            tmp.next = note

    def fill_new_list(self, note):
        f_note = Note(note.name, note.sname, note.number, note.bdate)
        if(self.new_head==None):
            self.new_head = f_note
        else:
            new_tmp = self.new_head
            while(new_tmp.next):
                new_tmp = new_tmp.next
            new_tmp.next = f_note

    def random_note(self):
        names = ['Максим', 'Даниил', 'Дима','Никита','Юрий','Султан','Владимир','Настя',\
        'Роман','Филипп','Аня', 'Иван','Катя','Сергей','Влад', 'Дарья']
        surnames = ['Самушенков','Бережнов','Чепусов','Титов','Головкин',\
        'Кузнецов', 'Буинов','Иванов', 'Сомов', 'Петров','Ларионов','Мялов','Малинов',\
        'Томпсон','Корелов','Герасимовов', 'Зинчуков','Васильев','Елинов']
        name = random.choice(names)
        sname = random.choice(surnames)
        number = ''
        for i in range(6):
            number += str(random.randint(0,9))
        bdate = ''
        day = str(random.randint(1,30))
        if len(day) == 1:
            day = '0' + day
        month = str(random.randint(1,12))
        if len(month) == 1:
            month = '0' + month
        year = str(random.randint(1950,2018))
        bdate = day+'.'+month+'.'+year
        return Note(name, sname, number, bdate)

    def print_list(self):
        tmp = self.head
        print('| Фамилия         | Имя             | Телефон | \
Дата рождения |')
        print('---------------------------------------------------------------')
        while tmp:
            print('| {}{} | {}{} | {}  | \
{}    |'.format(tmp.sname,(15-len(tmp.sname))*' ', tmp.name,(15-len(tmp.name))*' ',\
tmp.number, tmp.bdate))
            print('---------------------------------------------------------------')
            tmp = tmp.next

    def print_new_list(self):
        tmp = self.new_head
        print('| Фамилия         | Имя             | Телефон | \
Дата рождения |')
        print('---------------------------------------------------------------')
        while(tmp):
            print('| {}{} | {}{} | {}  | \
{}    |'.format(tmp.sname,(15-len(tmp.sname))*' ', tmp.name,(15-len(tmp.name))*' ',\
tmp.number, tmp.bdate))
            print('---------------------------------------------------------------')
            tmp = tmp.next

    def find_note(self, name=None, sname=None, number=None, bdate=None):
        tmp = self.head
        if number is not None:
            while tmp:
                if tmp.number == number:
                    return tmp
                tmp = tmp.next
        elif name is not None and sname is not None:
            while tmp:
                if tmp.name == name and tmp.sname == sname:
                    return tmp
                tmp = tmp.next
        elif bdate is not None:
            while tmp:
                if tmp.bdate == bdate:
                    return tmp
                tmp = tmp.next
        else:
            return None

    def spec_task(self, sname):
        tmp = self.head
        while tmp:
            if tmp.sname == sname:
                return tmp
            tmp = tmp.next

    def change_data(self, note, new_name=None, new_sname=None,\
    new_number = None, new_bdate = None):
        tmp = self.head
        while(tmp):
            if tmp == note:
                if new_name is not None and new_sname is not None:
                    tmp.name = new_name
                    tmp.sname = new_sname
                elif new_number is not None:
                    tmp.number = new_number
                elif new_bdate is not None:
                    tmp.bdate = new_bdate
                break
            tmp = tmp.next

    def remove_note(self, note):
        tmp = self.head
        if tmp == note:
            self.head = tmp.next
        else:
            while tmp:
                if tmp.next == note:
                    tmp.next = tmp.next.next
                tmp = tmp.next

    def remove_note_lab(self, n):
        count = 0
        #isRemoved = False
        tmp = self.head
        if n == 1:
            self.head = tmp.next
        else:
            while tmp:
                count += 1
                if count == n:
                    tmp.next = tmp.next.next
                    print('Произошло удoление')
                    break
                tmp = tmp.next
            if n < 1:
                print('ошибка ввода!\n должно быть n > 0\n')
            if n > count:
                print('ошибка ввода!\n за гранью массива!\n')

    def sort_list(self):
        self.new_head = None
        #tmp = self.head
        least = 1071
        while self.head:
            temp = self.head
            least = 1071
            while temp:
                n = ord(temp.sname[0])
                if n<least:
                    least = n
                    tmp_least = temp
                temp = temp.next
            self.fill_new_list(tmp_least)
            self.remove_note(tmp_least)
        self.head = self.new_head


#         print('| Фамилия         | Имя             | Телефон | \
# Дата рождения |')
#         print('---------------------------------------------------------------')
#         while tmp:
#             print('| {}{} | {}{} | {}  | \
# {}    |'.format(tmp.sname,(15-len(tmp.sname))*' ', tmp.name,(15-len(tmp.name))*' ',\
# tmp.number, tmp.bdate))
#             #print('_________________________________________')
#             print('---------------------------------------------------------------')

#     def write_to_bfile(self):
#         tmp = self.head
#         FILENAME = "notebook.txt"
#         notes = '| Фамилия         | Имя             | Телефон | \
# Дата рождения |\n---------------------------------------------------------------\n'
#         while(tmp):
#             note = '| {}{} | {}{} | {}  | {}    |\n\
# ---------------------------------------------------------------\n\
# '.format(tmp.sname,(15-len(tmp.sname))*' ', tmp.name,(15-len(tmp.name))*' ',\
# tmp.number, tmp.bdate)
#             tmp = tmp.next
#             notes += note
#         # with open(FILENAME, "wb") as file:
#         #     pickle.dump(notes, file)
#         with open(FILENAME, 'a') as the_file:
#             the_file.write(notes)

    def write_to_bd(self, bd_name):
        conn = sqlite3.connect('notebook.db')
        c = conn.cursor()
        tmp = self.head
        c.execute("SELECT num FROM {}".format(bd_name))
        nums_fetch = c.fetchall()
        num_list = []
        for i in nums_fetch:
            num_list.append(i[0])
        while tmp:
            if not tmp.number in num_list:
                c.execute("INSERT INTO {} VALUES ('{}', '{}', {}, '{}')"\
                .format(bd_name, tmp.name, tmp.sname, tmp.number, tmp.bdate))
            tmp = tmp.next
        conn.commit()
        #c.close()


    def read_from_bd(self, bd_name):
        self.head = None
        conn = sqlite3.connect('notebook.db')
        c = conn.cursor()
        c.execute("SELECT * FROM {}".format(bd_name))
        l = c.fetchall()
        for i in l:
            self.fill_list(Note(i[0],i[1],i[2],i[3]))

    def print_from_bd(self, bd_name):
        self.new_head = None
        conn = sqlite3.connect('notebook.db')
        c = conn.cursor()
        c.execute("SELECT * FROM {}".format(bd_name))
        l = c.fetchall()
        for i in l:
            self.fill_new_list(Note(i[0],i[1],i[2],i[3]))
        self.print_new_list()
