text = "Привет, Python"

print(len(text))        # длина строки: 14
print(text[0])          # первый символ: П
print(text[-1])         # последний символ: n
print(text[0:6])        # срез от 0 до 6 (6 не входит): Привет   
print(text[8:])         # с 8-го до конца: Python
print(text[:6])         # с начала до 6-го: Привет
print(text[::-1])       # строка задом наперед


s = " Hello, World "

print(s.upper())                        # БОЛЬШИЕ БУКВЫ
print(s.lower())                        # мальнике буквы
print(s.strip())                        # убрать пробелы по краям
print(s.replace("World", "Python"))     # поиск и замена 
print(s.strip().split(","))             # разбить в список по запятой
print("World" in s)                     # True, есть ли подстрока
print(s.count("l"))                     # сколько раз встречается "l"


word = input("Скажи любое слово ")
print("В вашем слове число букв равно ", len(word), "Первый символ ", word[0],"Последний ", word[-1])

word1 = input("Скажи любое слово ").lower()
word2 = word1[::-1]
print("Ваше слово наоборот читается", word1[::-1])
if word1 == word2:
    print("Ваше слово палиндром")
else:
    print("Ваше слово не палиндром")

fio = input("Напишите пожалуйста ваше имя и фамилию через пробел ")
name, surname = fio.split()
print("Имя: ", name)
print("Фамилия: ", surname)


phrase = input("Напиши мне любое предложение ")
print(phrase.strip().upper())
print(phrase.lower().count("а"))