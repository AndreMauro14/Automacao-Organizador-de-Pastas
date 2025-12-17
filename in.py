import os

cwd = os.getcwd()

fullList = os.listdir(cwd)

files_list = [i for i in fullList if os.path.isfile(i) and '.py' not in i] 
types = list(set([i.split('.')[-1] for i in files_list]))

for file_type in types:
    if not os.path.exists(file_type):
        os.mkdir(file_type)

for file in files_list:
    from_path = os.path.join(cwd, file)
    file_split = file.split('.')[-1]
    to_path = os.path.join(cwd, file_split, file)
    
    os.replace(from_path, to_path)