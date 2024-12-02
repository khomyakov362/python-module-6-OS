from datetime import datetime
import re
import os
import json

def get_user_name() -> str:
    """Эта функиция нужна, чтобы удостовериться, что имя, введённое пользователем, может быть использовано как название файла."""
    name = input('Введите своё имя: ')
    if re.match(r'^[\w -_]{1,64}$', name):
        return name
    else:
        print('В имени можно использовать только буквы, цифры, пробелы, дефисы и знаки нижнего подчёркивания.\nИмя не может быть длиннее 64 символов.')
        return get_user_name()


def user_lvl() -> str:
    
    user_input = input('Введите уровень сложности: "простой", "средний" или "сложный": ').lower().strip()
    if user_input == "простой" or user_input == "средний" or user_input == "сложный":
        return user_input
    else: 
        print('Некорректный ввод!') 
        return user_lvl()

def choose_dictionary(dictionary_path : str, lvl : str) -> dict:
    
    try:
        with open(dictionary_path, 'rt', encoding='utf-8') as file:
            dict_of_dicts = json.loads(file.read())
        return dict_of_dicts[lvl]
    except KeyError:
        print('Ключ не был найден в словаре, удостоверьтесь, что вы используете .json файл нужного формата.')
    except FileNotFoundError:
        print('Файл не найден. Удостовертесь, что путь к файлу указан верно.')


def test_words(key : str, value : str) -> bool:

    user_input = input(f'Слово: {key}, {len(value)} букв, первая буква: {value[0]}... Ваш ответ: ').lower().strip()

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

def write_results(results_folder : str, results_dict : dict) -> None:
    user_name = results_dict['user_name'] 
    with open(os.path.join(results_folder ,f'{user_name}.json'), 'wt', encoding='utf-8') as file:
        file.write(json.dumps(results_dict, ensure_ascii=False))

def result(answers : dict, user_name : str, difficulty : str, levels_path : str) -> dict:
    
    with open(levels_path, 'rt', encoding='utf-8') as file:
        levels = json.loads(file.read())

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
    
    level = levels[str(len(correct))]
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

def see_results(results_folder) -> None:
    user_input = input('\nХотите уивдеть другие результаты? Введите "да", если да, любое другое сообщение, если нет: ').strip().lower()
    if user_input == 'да':
        stats_files = os.listdir(os.path.join(results_folder))
        for file_name in stats_files:
            with open(os.path.join(results_folder, file_name), 'rt', encoding='utf-8') as file:
                stats = json.loads(file.read())
                display_results(stats)
