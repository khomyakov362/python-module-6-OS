from utils import *
import os

local_folder = os.path.dirname(os.path.abspath(__file__))
dictionary_path = os.path.join(local_folder, 'dictionaries', 'sample.json')
levels_path = os.path.join(local_folder, 'levels.json')
results_path = os.path.join(local_folder, 'users_stats')

user_name = get_user_name()
difficulty = user_lvl()

dictionary = choose_dictionary(dictionary_path, difficulty)
answers = test_answers(dictionary)
current_results = result(answers, user_name, difficulty, levels_path)
write_results(results_path, current_results)

see_results(results_path)
