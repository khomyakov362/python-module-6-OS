from datetime import datetime
import re

def get_user_name() -> str:
    name = input('Введите своё имя: ')
    if re.match(r'^[\w -_]$', name):
        return name
    else:
        print('В имени можно использовать только буквы, цифры, пробелы, дефисы и знаки нижнего подчёркивания.')
        return get_user_name()


def user_lvl() -> str:
    
    user_input = input('Введите уровень сложности: "простой", "средний" или "сложный": ').lower().strip()
    if user_input == "простой" or user_input == "средний" or user_input == "сложный":
        return user_input
    else: 
        print('Некорректный ввод!') 
        return user_lvl()

def choose_dictionary(dict_of_dicts : dict, lvl : str) -> dict:
    
    try:
        return dict_of_dicts[lvl]
    except KeyError:
        print('Ключ не был найден в словаре, удостоверьтесь, что вы используете .json файл нужного формата.')


def test_words(key : str, value : str) -> bool:

    user_input = input(f'Слово :{key}, {len(value)} букв, первая буква: {value[0]}... Ваш ответ: ').lower().strip()

    if user_input == value:
        print(f'Верно: {key} - это {value}.\n')
        return True
    else:
        print(f'Неверно: {key} - это {value}.\n')
        return False

def test_answers(dictionary : dict) -> dict:
    answers = {}

    for key, value in dictionary.items():
        answers[key] = test_words(key, value)
    
    return answers

def result(answers : dict, user_name : str, difficulty : str) -> dict:
    
    levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
    }

    correct = [key for key in answers if answers[key]]
    incorrect = [key for key in answers if not answers[key]]
    
    if len(correct) > 0:
        print('Ваши правильные ответы: ')
        for answer in correct:
            print(answer)
        print()
    if len(incorrect) > 0:
        print('Ваши неправиьные ответы: ')
        for answer in incorrect:
            print(answer)
        print()
    
    level = levels[len(correct)]
    print(f'Ваш уровень:\n{level}')

    return {
        'user_name' : user_name,
        'date' : datetime.now().strftime('%d/%m/%Y'),
        'correct_answers' : correct,
        'incorrect_answers' : incorrect,
        'score' : len(correct),
        'level' : level,
        'difficulty' : difficulty
    }

def display_results(results : dict) -> None:
    print(f'''
Пользователь: {results['user_name']}
Дата: {results['date']}
Правильные ответы: {', '.join(results['correct_answers'])}
Неправиьные ответы: {', '.join(results['incorrect_answers'])}
Счёт: {results['score']}
Уровень: {results['level']}
Уровень сложности: {results['difficulty']}
''')