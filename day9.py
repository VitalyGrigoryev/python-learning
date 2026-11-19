server = {"name": "web1", "status": "ok", "port": 80}

print(server)
print(server["name"])       # Значение по ключу
print(server.get("cpu"))    # None, если ключа нет (без ошибки)
print(server.get("cpu", 0)) # или свое значение по умолчанию

server["status"] = "error"  # изменить
server["cpu"] = 45          # добвать новый ключ
del server["port"]          # удалить ключ
print(server)

print("name" in server)     # True, проверка ключа
print(len(server))          # сколько пар

# перебор
for key in server:
    print(key)

for key, value in server.items():
    print(f"{key}: {value}")

print(server.keys())
print(server.values())

# Задачи

my_profile = {"name": "vitaly", "city": "minsk", "profession": "sysadmin", "age": "38"}
for key, value in my_profile.items():
    print(f"{key}: {value}")

web_server = {"web1": "ok", "web2": "error", "db1": "ok", "db2": "error", "cache1": "ok"}
print("error" in web_server)
count = 0
for name, status in web_server.items():
    if status == "error":
        print(name)
        count += 1
print(f"Серверов с ошибкой: {count}")

any_word = input("Введите любое слово ")
count = {}
for letter in any_word:
    count[letter] = count.get(letter, 0) + 1
print(count)

phone_book = {}
while True:
    name = input("Введите ваше имя ")
    if name == "stop":
        break
    phone = (input("Введите ваш номер телефона "))
    phone_book[name] = phone

for key,  value in phone_book.items():
    print(f"{key} : {value}")

servers = [
    {"name": "web1", "status": "ok", "cpu": "90"},
    {"name": "web2", "status": "error", "cpu": "50"},
    {"name": "db1", "status": "ok", "cpu": "80"},
    {"name": "db2", "status": "error", "cpu": "50"},
]
error_servers = []
high_cpu_servers = []

for server in servers:
    if server["status"] == "error":
        error_servers.append(server["name"])
    if int(server["cpu"]) >= 80:
        high_cpu_servers.append(server["name"])

print(f"Упавшие серверы: {error_servers}, всего: {len(error_servers)}")
print(f"Высокая нагрузка: {high_cpu_servers}, всего: {len(high_cpu_servers)}")
   