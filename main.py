import os
import random
import datetime

from Note import Note
from NoteList import NoteList
from input import *
import bd_work

if __name__ == '__main__':

    notebook = NoteList()
    if os.path.exists("notebook.txt"):
        os.remove("notebook.txt")

    while True:
        os.system('clear')
        print('Выберите задачу')
        print('1. Вывести список')
        print('2. Добавить контакт')
        print('3. Найти контакт')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Добавить несколько случайных контактов')
        print('7. Cортировать контакты')
        print('8. Работа с базой данных')
        print('9. Задание на поиск')
        print('10. Выход')
        choice = input()

        if choice == '1':
            os.system('clear')
            if notebook.head is None:
                print('Список контактов пуст!')
            else:
                notebook.print_list()
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue

        elif choice == '2':
            sub_notebook = NoteList()
            ### input name
            os.system('clear')
            print('Введите имя \n[имена содержат только символы кириллицы и первая буква - заглавная]\n\
[не более 15 символов]')
            l = input_name()
            name, n = l[0], l[1]
            if n == 'q':
                os.system('clear')
                continue
            ### input sname
            os.system('clear')
            print('Введите фамилию [фамилии содержат только символы кириллицы и первая буква - заглавная]\n\
[не более 15 символов]')
            l = input_name()
            sname, n = l[0], l[1]
            if n == 'q':
                os.system('clear')
                continue
            ### input number
            os.system('clear')
            l = input_number(notebook)
            number, n = l[0], l[1]
            if n == 'q':
                os.system('clear')
                continue
            ### input bdate
            os.system('clear')
            l = input_bdate()
            bdate, n = l[0], l[1]
            if n == 'q':
                os.system('clear')
                continue
            notebook.fill_list(Note(name, sname, number, bdate))
            os.system('clear')
            print('Вы добавили следующий контакт: ')
            sub_notebook.fill_list(notebook.find_note(number = number))
            sub_notebook.print_list()
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue


        elif choice == '3':
            os.system('clear')
            if notebook.head is None:
                print('Список контактов пуст!')
            else:
                print('Найти контакт по:')
                print('1. Имени-фамилии')
                print('2. Номеру телефона')
                print('3. Дате рождения')
                mini_choice = input()
                sub_notebook = NoteList()
                tmp = notebook.head
                while tmp:
                    sub_notebook.fill_list(Note(tmp.name,tmp.sname,tmp.number,tmp.bdate))
                    tmp = tmp.next
                #sub_notebook = notebook
                result = NoteList()

                if mini_choice == '1':
                    ### input name
                    os.system('clear')
                    print('Введите имя:')
                    l = input_name()
                    name, n = l[0], l[1]
                    if n == 'q':
                        os.system('clear')
                        continue
                    ### input sname
                    os.system('clear')
                    print('Введите фамилию:')
                    l = input_name()
                    sname, n = l[0], l[1]
                    if n == 'q':
                        os.system('clear')
                        continue
                    res = sub_notebook.find_note(name, sname)
                    count = 0
                    while res is not None:
                        count += 1
                        result.fill_list(Note(res.name, res.sname, res.number, res.bdate))
                        sub_notebook.remove_note(res)
                        res = sub_notebook.find_note(name, sname)
                    if count == 0:
                        print('Ничего не найдено!')
                    elif count == 1:
                        result.print_list()
                    else:
                        print('Найдено несколько вариантов: ')
                        result.print_list()


                elif mini_choice == '2':
                    os.system('clear')
                    #print('Введите номер телефона:')
                    l = input_number()
                    number, n = l[0], l[1]
                    if n == 'q':
                        os.system('clear')
                        continue
                    res = notebook.find_note(number = number)
                    if res is None:
                        print('Запись отсутствует!')
                    else:
                        result.fill_list(Note(res.name, res.sname, res.number, res.bdate))
                        result.print_list()

                elif mini_choice == '3':
                    os.system('clear')
                    print('Введите дату рождения:')
                    l = input_bdate()
                    bdate, n = l[0], l[1]
                    if n == 'q':
                        os.system('clear')
                        continue
                    res = sub_notebook.find_note(bdate = bdate)
                    count = 0
                    while res is not None:
                        count += 1
                        result.fill_list(Note(res.name, res.sname, res.number, res.bdate))
                        sub_notebook.remove_note(res)
                        res = sub_notebook.find_note(bdate = bdate)
                    if count == 0:
                        print('Ничего не найдено!')
                    elif count == 1:
                        result.print_list()
                    else:
                        print('Найдено несколько вариантов: ')
                        result.print_list()
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue

        elif choice == '4':
            sub_notebook = NoteList()
            os.system('clear')
            if notebook.head is None:
                print('Список контактов пуст!')
            else:
                print('Введите номер телефона изменяемого контакта:')
                l = input_number()
                number, n = l[0], l[1]
                if n == 'q':
                    os.system('clear')
                    continue
                data = notebook.find_note(number = number)
                if data is None:
                    print('Запись отсутствует!')
                else:
                    os.system('clear')
                    print('Изменямый контакт: ')
                    sub_notebook.fill_list(notebook.find_note(number = number))
                    sub_notebook.print_list()
                    print('Выберите, что изменить:')
                    print('1. Имя и Фамилию')
                    print('2. Номер Телефона')
                    print('3. Дата рождения')
                    mini_choice = input()
                    if mini_choice == '1':
                        os.system('clear')
                        print('Введит новое имя:')
                        l = input_name()
                        new_name, n = l[0], l[1]
                        if n == 'q':
                            os.system('clear')
                            continue
                        os.system('clear')
                        print('Введит новую фамилию:')
                        l = input_name()
                        new_sname, n = l[0], l[1]
                        if n == 'q':
                            os.system('clear')
                            continue
                        notebook.change_data(data, new_name, new_sname)
                        print('Контакт успешно изменен!')

                    elif mini_choice == '2':
                        os.system('clear')
                        print('Введите новый номер:')
                        l = input_number(notebook)
                        new_number, n = l[0], l[1]
                        if n == 'q':
                            os.system('clear')
                            continue
                        notebook.change_data(data, new_number = new_number)
                        print('Контакт успешно изменен!')

                    elif mini_choice == '3':
                        os.system('clear')
                        print('Введите новую дату рождения:')
                        l = input_bdate()
                        new_bdate, n = l[0], l[1]
                        if n == 'q':
                            os.system('clear')
                            continue
                        #new_bdate = input()
                        notebook.change_data(data, new_bdate = new_bdate)
                        print('Контакт успешно изменен!')
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue

        elif choice == '5':
            os.system('clear')
            if notebook.head is None:
                print('Список контактов пуст!')
            else:
                print('Введите номер телефона контакта:')
                l = input_number()
                number, n = l[0], l[1]
                if n == 'q':
                    os.system('clear')
                    continue
                else:
                    data = notebook.find_note(number = number)
                    if data is None:
                        print('Запись отсутствует!')
                    else:
                        notebook.remove_note(data)
                        print('Контакт успешно удален.')
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue


        elif choice == '6':
            os.system('clear')
            print('сколько?')
            n = input()
            if check_natural(n):
                for i in range(int(n)):
                    notebook.fill_list(notebook.random_note())
                print('Контакты успешно внесены в список.')
            else:
                print('Введите натуральное число!')
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue

        elif choice == '7':
            os.system('clear')
            if notebook.head is None:
                print('Список контактов пуст!')
            else:
                notebook.sort_list()
                print('Список контактов успешно отсортирован')
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue

        elif choice == '8':
            try:
                while True:
                    os.system('clear')
                    print('1. Сохранить контакты')
                    print('2. Просмотреть список из базы данных')
                    print('3. Выбрать список из базы данных')
                    print('4. Удалить список из базы данных')
                    print('5. Выход')
                    submenu_choice = input()
                    os.system('clear')
                    if submenu_choice == '1':
                        if notebook.head is None:
                            print('Список контактов пуст!')
                        else:
                            print('1. Добавить контакты в существующий список контактов.')
                            print('2. Создать новый список контактов и добавить их туда.')
                            mini_choice = input()

                            if mini_choice == '1':
                                l = bd_work.bd_list()
                                if not l:
                                    os.system('clear')
                                    print('В базе данных нет ни одного списка!')
                                    print("Нажмите 'enter', чтобы вернуться в подменю")
                                    mini_choice = input()
                                    if mini_choice is not None:
                                        os.system('clear')
                                        continue
                                else:
                                    count = 0
                                    for i in l:
                                        count += 1
                                        print(str(count)+'. '+i[0])
                                    numb = input('Введите номер списка: ')
                                    if check_natural(numb):
                                        numb = int(numb)
                                        if numb>0 and numb<=count:
                                            bd_name = l[numb-1][0]
                                            notebook.write_to_bd(bd_name)
                                            print('контакты были успешно добавлены')
                                        else:
                                            print('Некорентный ввод! Введите натуральное число от 1 до {}'.format(count))
                                    else:
                                        print('Введите натуральное число!')
                                    print("Нажмите 'enter', чтобы вернуться в подменю")
                                    mini_choice = input()
                                    if mini_choice is not None:
                                        os.system('clear')
                                        continue
                            if mini_choice == '2':
                                bd_name = input('Введите название списка: ')
                                if bd_name != '':
                                    if not check_bd(bd_name):
                                        bd_work.create_bd(bd_name)
                                        notebook.write_to_bd(bd_name)
                                        os.system('clear')
                                        print('Список контактов {} успешно внесен в базу данных'.format(bd_name))
                                    else:
                                        print('список уже создан!')
                                else:
                                    print('Вы ничего не ввели!')
                            else:
                                continue
                        print("Нажмите 'enter', чтобы вернуться в подменю")
                        mini_choice = input()
                        if mini_choice is not None:
                            os.system('clear')
                            continue

                    if submenu_choice =='2':
                        os.system('clear')
                        if os.path.exists("notebook.db"):
                            l = bd_work.bd_list()
                            if not l:
                                os.system('clear')
                                print('В базе данных нет ни одного списка контактов!')
                            else:
                                count = 0
                                for i in l:
                                    count += 1
                                    print(str(count)+'. '+i[0])
                                print('Введите номер списка или q, чтобы выйти: ')
                                numb = input()
                                if check_natural(numb):
                                    numb = int(numb)
                                    if numb>0 and numb<=count:
                                        bd_name = l[numb-1][0]
                                        notebook.print_from_bd(bd_name)
                                    else:
                                        print('Некорректный ввод! Введите натуральное число от 1 до {}'.format(count))
                                elif numb == 'q':
                                    continue
                                else:
                                    print('Введите натуральное число!')
                        else:
                            print('файл не создан!')
                        #os.system('clear')
                        print("Нажмите 'enter', чтобы вернуться в подменю")
                        mini_choice = input()
                        if mini_choice is not None:
                            os.system('clear')
                            continue

                    if submenu_choice =='3':
                        os.system('clear')
                        if os.path.exists("notebook.db"):
                            l = bd_work.bd_list()
                            if not l:
                                os.system('clear')
                                print('В базе данных нет ни одного списка контактов!')
                            else:
                                count = 0
                                for i in l:
                                    count += 1
                                    print(str(count)+'. '+i[0])
                                print('Введите номер списка или q, чтобы выйти: ')
                                print('[данное действие перезапишет текущие контакты]')
                                numb = input()
                                if check_natural(numb):
                                    numb = int(numb)
                                    if numb>0 and numb<=count:
                                        bd_name = l[numb-1][0]
                                        notebook.read_from_bd(bd_name)
                                        os.system('clear')
                                        print(' список был заменен списком {}'.format(bd_name))
                                    else:
                                        print('Некорректный ввод! Введите натуральное число от 1 до {}'.format(count))
                                elif numb == 'q':
                                    continue
                                else:
                                    print('Введите натуральное число!')
                        else:
                            print('файл не создан!')
                        #os.system('clear')
                        print("Нажмите 'enter', чтобы вернуться в подменю")
                        mini_choice = input()
                        if mini_choice is not None:
                            os.system('clear')
                            continue

                    if submenu_choice == '4':
                        os.system('clear')
                        if os.path.exists("notebook.db"):
                            l = bd_work.bd_list()
                            if not l:
                                print('В базе данных нет ни одного списка контаков!')
                            else:
                                count = 0
                                for i in l:
                                    count += 1
                                    print(str(count)+'. '+i[0])
                                print('Введите номер списка или q, чтобы выйти: ')
                                #print('[данное действие перезапишет текущие контакты]')
                                numb = input()
                                if check_natural(numb):
                                    numb = int(numb)
                                    if numb>0 and numb<=count:
                                        bd_name = l[numb-1][0]
                                        bd_work.delete_bd(bd_name)
                                        os.system('clear')
                                        print('список {} был удален'.format(bd_name))
                                    else:
                                        print('Некорентный ввод! Введите натуральное число от 1 до {}'.format(count))
                                elif numb == 'q':
                                    continue
                                else:
                                    print('Введите натуральное число!')
                        else:
                            print('файл не создан!')
                        print("Нажмитер 'enter', чтобы вернуться в меню")
                        mini_choice = input()
                        if mini_choice is not None:
                            os.system('clear')
                            continue

                    if submenu_choice == '5':
                        break
            except sqlite3.DatabaseError:
                os.system('clear')
                print("База данных была повреждена и перемещена в папку 'damaged_dbs'.")
                count = 1
                l = str(datetime.datetime.now())[:19]
                if os.path.exists('damaged_dbs'):
                    os.rename('notebook.db', 'damaged_dbs/damaged_db_{}'.format(l))
                else:
                    os.mkdir('damaged_dbs')
                    os.rename('notebook.db', 'damaged_dbs/damaged_db_{}'.format(l))
                print("Нажмите 'enter', чтобы вернуться в подменю")
                mini_choice = input()
                if mini_choice is not None:
                    os.system('clear')
                    continue




        elif choice == '9':
            os.system('clear')
            if notebook.head is None:
                print('Список контактов пуст!')
            else:
                sub_notebook = NoteList()
                tmp = notebook.head
                while tmp:
                    sub_notebook.fill_list(Note(tmp.name,tmp.sname,tmp.number,tmp.bdate))
                    tmp = tmp.next
                result = NoteList()
                os.system('clear')
                print('Найти информацию о людях, чья фамилия была введена')
                print('Введите фамилию:')
                l = input_name()
                sname, n = l[0], l[1]
                if n == 'q':
                    os.system('clear')
                    continue
                res = sub_notebook.spec_task(sname)
                count = 0
                while res is not None:
                    count += 1
                    result.fill_list(Note(res.name, res.sname, res.number, res.bdate))
                    sub_notebook.remove_note(res)
                    res = sub_notebook.spec_task( sname)
                if count == 0:
                    print('Ничего не найдено!')
                elif count == 1:
                    result.print_list()
                else:
                    print('Найдено несколько вариантов: ')
                    result.print_list()
            print("Нажмитер 'enter', чтобы вернуться в меню")
            mini_choice = input()
            if mini_choice is not None:
                os.system('clear')
                continue


        elif choice == '10':
            os.system('clear')
            break
