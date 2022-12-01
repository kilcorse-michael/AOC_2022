import os
import time

def create_dir():
    dir_name = input("AOC day: ")
    current_dir = os.getcwd()
    new_path = os.path.join(current_dir, dir_name)
    files = [dir_name + ".py", dir_name + ".txt", dir_name + "_min.txt"]
    try:
        os.makedirs(new_path)
    except OSError as error:
        print(error)
    for x in files:
        file = os.path.join(new_path, x)
        with open(file, "w") as f:
            if x.endswith(".py"):
                f.write(f"#{dir_name} AOC 2022 python file\n")
                f.write(f"FULL_DATA, TEST_DATA = \"./{dir_name}/{dir_name}.txt\", \"./{dir_name}/{dir_name}_min.txt\"\n\n")
                f.write("with open(TEST_DATA) as f:\n\t#Read file here\n\tpass")
    return "Directory completed"


print(create_dir())