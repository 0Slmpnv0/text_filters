import random

punctuation = '!()-[]{};:\'\",./?@#$%^&*_~'


def no_punctuation(text):
    return ''.join([i for i in text if i not in punctuation])


def random_case_filter(text): # каждая буква или большая или маленькая. Выбор рандомный
    result_str = ''
    for symbol in text.lower():
        if symbol not in punctuation:
            if random.choice([True, False]):
                result_str += symbol.upper()
            result_str += symbol
        else:
            result_str += symbol
    return result_str


def reverse_filter(text):  # переворачивает текст
    result_list = []
    for i in [s for s in text]:
        result_list.insert(0, i)
    return ''.join(result_list)


def snake_case_filter(text):
    return '_'.join(no_punctuation(text).lower().split(' '))


def PascalCaseFilter(text):
    result_str = ''
    words_list = no_punctuation(text).lower().split(' ')
    for word in words_list:
        result_str += word.capitalize()
    return result_str

def camelCaseFilter(text):
    result_str = ''
    words_list = no_punctuation(text).lower().split(' ')
    result_str += words_list.pop(0)
    for word in words_list:
        result_str += word.capitalize()
    return result_str


def main_menu():
    print(f'''Меню фильтров:
0. Выход
1. reverse_filter
2. snake_case_filter
3. PascalCaseFilter
4. camelCaseFelter
5. lowercasefilter
6. UPPERCASEFILTER
7. {random_case_filter('random_case_filter')}
''')
    input_num = input('Выберите нужный фильтр для текста, введя соответствующую цифру\n')
    try:    punctuation = '!()-[]{};:\'\",./?@#$%^&*_~'
        int(input_num)
    except:
        print('Вы должны ввести одну цифру. Не строку. Не список. Не что-либо еще')
        return main_menu()
    if 1 < int(input_num) > 8:
        print('Такого варианта ответа нет. Вы можете выбрать один из семи доступных фильтров, или нажмите 8 чтобы выйти')
        return main_menu()
    return int(input_num)


def yes_no_func():
    print('Подтвердить действие? [y/n]')
    answer = input('у - да, n - нет')
    if answer != 'y' and answer != 'э':
        print('Такого варианта ответа не существует. Введите существующий ваиант ответа')
        return yes_no_func()
    elif answer == 'y':
        return True
    return False

filter_number = 1
while filter_number != 0:
    filter_number = main_menu()
    match filter_number:
        case 1:
            print('reverse_filter разворачивает ваш текст.')
            if yes_no_func():
                print(reverse_filter(input('Введите текст: ')))
                print('До свидания!')
                break
            continue

        case 2:
            print('snake_case_filter убирает знаки препинания, делает каждую букву прописной и заменяет пробелы на _')
            if yes_no_func():
                print(snake_case_filter(input('Введите текст: ')))
                print('До свидания!')
                break
            continue

        case 3:
            print('PascalCaseFilter убирает знаки препинания, делает каждую букву прописной, убирает пробелы и делает '
                  'первую букву каждого слова заглавной')
            if yes_no_func():
                print(PascalCaseFilter(input('Введите текст: ')))
                print('До свидания!')
                break
            continue
        case 4:
            print('camelCaseFilter убирает знаки препинания, делает каждую букву прописной, убирает пробелы и делает '
                  'первую букву каждого слова кроме первого заглавной')
            if yes_no_func():
                print(camelCaseFilter(input('Введите текст: ')))
                print('До свидания!')
                break
            continue
        case 5:
            print('lowercasefilter делает каждую букву прописной')
            if yes_no_func():
                print((input('Введите текст: ')).lower())
                print('До свидания!')
                break
            continue
        case 6:
            print('UPPERCASEFILTER делает каждую букву заглавной')
            if yes_no_func():
                print((input('Введите текст: ')).upper())
                print('До свидания!')
                break
            continue
        case 7:
            print(f'{random_case_filter("random_case_filter")} случайным образом делает каждую букву заглавной или прописной')
            if yes_no_func():
                print(random_case_filter(input('Введите текст: ')))
                print('До свидания!')
                break
            continue


