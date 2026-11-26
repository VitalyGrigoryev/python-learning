def read_logs(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()

def count_levels(lines):
    count = {}
    for line in lines:
        part = line.split()
        if not part:
            continue
        first_word = part[0]
        count[first_word] = count.get(first_word, 0) + 1
    return count


def write_logs(filename, count):
    with open(filename, "w", encoding="utf-8") as f:
        for level, number in count.items():
            f.write(f"{level}: {number}\n")

def main():
    lines = read_logs("app.log")
    counts = count_levels(lines)
    write_logs("report.txt", counts)
    print(counts)

if __name__ == "__main__":
    main()