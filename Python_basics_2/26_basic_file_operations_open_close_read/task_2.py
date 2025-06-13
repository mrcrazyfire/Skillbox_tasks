import os, random

def find_files(path, target, found_files = []):
    if found_files is None:
        found_files = []

    for elem in os.listdir(path):
        cur_path = os.path.join(path, elem)

        if os.path.isfile(cur_path):
            if elem == target:
                found_files.append(cur_path)
        elif os.path.isdir(cur_path):
            find_files(cur_path, target)

    return found_files

def print_file(path):
    with open(path, 'r', encoding="utf-8") as f:
        print(f.read())

target_path = os.path.abspath(os.path.join("..", ".."))
filename = "main.py"

files = find_files(target_path, filename)

index = random.randint(0, len(files) - 1)

print_file(files[index])