file_path = '.txt'
with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())
