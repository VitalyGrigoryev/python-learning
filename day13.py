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

def read_logs(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()

def count_levels(lines):
    count = {}
    for letter in lines:
        part = letter.split()
        if not part:
            continue
        first_word = part[0]
        count[first_word] = count.get(first_word, 0) + 1
    return count
lines = read_logs("app.log")
count = count_levels(lines)

def write_logs(filename, count):
    with open(filename, "w", encoding="utf-8") as f:
        for level, number in count.items():
            f.write(f"{level}: {number}\n")


write_logs("report.txt", count)