def readall(nm):
    with open(nm, 'r', encoding = 'utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

def write_1(nm):
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    str_new = '\n' + str_new1 + ', ' + str_new2 + ', ' + str_new3 + ', ' + str_new4
    with open(nm, 'a') as txt_file:
        txt_file.write(str_new)
        
def find_item(nm):
    item = input('Характеристика: ')
    with open(nm, 'r', encoding = 'uft8') as txt_file:
        for line in txt_file:
            if item.lower() in line.lower():
                print(line.strip())

def find_item2(nm):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер(0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Телефон): '))
    with open(nm, 'r', encoding= 'uft8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)
                
def sort_data(nm):
    list_1 = []
    item_type = int(input('Введите номер(0 - Фамилия, 1 - Имя, 2 - Отчество, 3 - Телефон): '))
    with open(nm, 'r', encoding='uft8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            list_1.append(line)
        list_1.sort(key = lambda person:person[item_type])
    with open(nm, 'w', encoding='uft8') as txt_file:
        for line in list_1:
            line = ', '.join(line)
            txt_file.write(line)
            
# Изменяет информацию из файла
def edit_data(nm):
    print('\nПП | ФИО | Телефон')
    with open(nm, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print(' ')
        index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
        tel_book_lines = tel_book.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(' | ')
        fio = input('Введите ФИО: ')
        phone = input('Введите номер телефона: ')
        num = elements[0]
        if len(fio) == 0:
            fio = elements[1]
        if len(phone) == 0:
            phone = elements[2]
        edited_line = 'f{num} | {fio} | {phone}'
        tel_book_lines[index_delete_data] = edited_line
        print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
        with open(nm, 'w', encoding='utf-8') as f:
            f.write('\n'.join(tel_book_lines))
            
edit_data('data.txt')
readall('data.txt')
write_1('data.txt')
find_item('data.txt')
find_item2('data.txt')
sort_data('data.txt')