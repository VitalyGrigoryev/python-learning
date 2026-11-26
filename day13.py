with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("первая строка\n")
    f.write("вторая строка\n")
    f.write("третья строка\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)


with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
print(text)


with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("первая строка\n")
    f.write("вторая строка\n")
    f.write("третья строка\n")

try:
    with open("notesss.txt", "r", encoding="utf-8") as f:
        text = f.readlines()
except FileNotFoundError:
    print("Файл не найден")
