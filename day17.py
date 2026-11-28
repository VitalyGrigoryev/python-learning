import requests


def get_repos(name):
    url = f"https://api.github.com/users/{name}/repos"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def count_languages(repos):
    count = {}
    for repo in repos:
        lang = repo["language"]
        if lang is None:
            continue
        count[lang] = count.get(lang, 0) + 1
    return count


def write_report(count, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for language, number in count.items():
            f.write(f"{language}: {number}\n")


def main():
    repos = get_repos("VitalyGrigoryev")
    if repos is None:
        print("Не удалось получить данные")
        return
    counts = count_languages(repos)
    write_report(counts, "repos_report.txt")
    print(counts)


if __name__ == "__main__":
    main()
