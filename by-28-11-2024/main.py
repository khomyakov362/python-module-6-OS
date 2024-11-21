from utils import user_lvl, test_answers, result, choose_dictionary, display_results, get_user_name
import os
import json

local_folder = os.path.dirname(os.path.abspath(__file__))

user_name = "Сергей" #get_user_name()
difficulty = "средний" #user_lvl()

with open(os.path.join(local_folder, 'dictionaries', 'sample.json'), 'rt', encoding='utf-8') as file:
    dict_of_dicts = json.loads(file.read())

dictionary = choose_dictionary(dict_of_dicts, difficulty)
answers = test_answers(dictionary)
current_results = result(answers, user_name, difficulty)

with open(os.path.join(local_folder, 'user_stats', f'{user_name}.json'), 'wt', encoding='utf-8') as file:
    dict_of_dicts = json.loads(file.read())







