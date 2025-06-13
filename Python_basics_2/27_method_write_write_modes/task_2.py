import os


def copy_files(path):
    for element in os.listdir(path):
        curr_path = os.path.join(path, element)

        if os.path.isfile(curr_path) and element == 'main.py':
            with open('script.py', 'a', encoding="utf-8") as scripts_file:
                with open(curr_path, 'r', encoding="utf-8") as curr_file:
                    for line in curr_file:
                        scripts_file.write(line)
                    scripts_file.write('\n' * 40)



        if os.path.isdir(curr_path):
            copy_files(curr_path)


my_path = os.path.abspath(os.path.join("..", ".."))

copy_files(my_path)



