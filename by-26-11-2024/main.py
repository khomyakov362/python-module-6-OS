import os
text = '''Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом.'''

# Этот кусок я добавил, так как не хотел создавать отдельный проект ещё и для этого задания
current_directory_path = os.path.dirname(os.path.abspath(__file__))
file_name = 'file.txt'
file_path = os.path.join(current_directory_path, file_name)

def write_to_file(file, content):

    with open(file, 'wt', encoding='utf-8') as current_file:
        current_file.write(content)

write_to_file(file_path, text)

def print_file(file):

    with open(file, 'rt', encoding='utf-8') as current_file:
        print(current_file.read())

print_file(file_path)