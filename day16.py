import requests

# response = requests.get('https://api.github.com/users/VitalyGrigoryev', timeout=10)
# print(response.status_code)
# data = response.json()
# print(type(data))
# print(data["login"])
# print(data["public_repos"])
# print(data["created_at"])
# print(data.keys())

# url = "https://api.github.com/users/VitalyGrigoryev"
#
# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
# except requests.exceptions.RequestException:
#     print("Не удалось получить данные")

def get_user(name):
    url = f"https://api.github.com/users/{name}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def main():
    user = get_user("VitalyGrigoryev")
    if user is None:
        print("Пользователь не найден или нет соединения")
    else:
        print(user["login"])
        print(user["public_repos"])

if __name__ == "__main__":
    main()