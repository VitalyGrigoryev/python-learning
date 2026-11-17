fruits = ["яблоко","банан","вишня"]

print(fruits)           
print(fruits[0])        # первый элемент (нумерация с нуля)
print(fruits[-1])       # последний
print(fruits[0:2])      # срез, как у строк
print(len(fruits))      # сколько элементов


fruits.append("груша")  # добваить в конец
fruits.remove("банан")  # удалить по значению
fruits[0] = "апельсин"  # заменить элемент
print(fruits)

print("вишня" in fruits)# True, есть ли в списке

# перебор списка циклом
for fruit in fruits:
    print("Фрукт:", fruit)

# числа
numbers = [5, 2, 9, 1]
numbers.sort()          # сортировка на месте
print(numbers)
print(sum(numbers), min(numbers), max(numbers))

# задачи

my_films = ["астерикс", "индиана", "доспехи бога", "жандармы", "фантомас"]
print(f"Первый фильм списка: {my_films[0]}\nПоследний: {my_films[-1]}\nКоличество фильмов в списке: {len(my_films)} ")

for number, film in enumerate(my_films, 1):
    print(f"{number}. {film}")

num_list = [4, 8, 15, 16, 23, 42]
print(sum(num_list), max(num_list))
for i in num_list:
    if i > 10:
        print(i)


word_list = []
while True:
    word = input("Напиши любое слово или stop для остановки ")
    if word.lower() != "stop":
        word_list.append(word)
    else:
        print(f"Список ваших слов: {word_list}\nКоличество слов: {len(word_list)}")
        break
if word_list:
    print(f"Самое длинное слово из вашего списка: {max(word_list, key=len)}")
else:
    print("Вы не ввели ни одного слова")
