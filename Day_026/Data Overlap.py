with open("file1.txt") as file1:
    file1 = [int(line.strip()) for line in file1]
with open("file2.txt") as file2:
    file2 = [int(line.strip()) for line in file2]

result = [i for i in file1 if i in file2]
print(result)