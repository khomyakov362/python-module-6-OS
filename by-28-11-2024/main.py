from utils import *
import os
import json

local_folder = os.path.dirname(os.path.abspath(__file__))

user_name = get_user_name()
difficulty = user_lvl()

with open(os.path.join(local_folder, 'dictionaries', 'sample.json'), 'rt', encoding='utf-8') as file:
    dict_of_dicts = json.loads(file.read())

dictionary = choose_dictionary(dict_of_dicts, difficulty)
answers = test_answers(dictionary)
current_results = result(answers, user_name, difficulty)

with open(os.path.join(local_folder, 'users_stats', f'{user_name}.json'), 'wt', encoding='utf-8') as file:
    file.write(json.dumps(current_results, ensure_ascii=False))

see_results(local_folder, 'users_stats')
