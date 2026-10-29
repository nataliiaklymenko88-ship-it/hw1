import random

group = [
    "Акберова Шафіга",
    "Бабич Софія",
    "Вагіна Аліна",
    "Дмитрієва Анна",
    "Іщенко Каріна",
    "Клименко Наталія",
    "Крамаренко Ганна",
    "Карпова Христина",
    "Коржикова Софія",
    "Кучін Ілля",
    "Леонова Поліна",
    "Міняйлик Аліна",
    "Наталуша Тетяна",
    "Немчинська Анастасія",
    "Поліщук Єлизавета",
    "Роменський Микита",
    "Ткачук Поліна",
    "Фесюк Вікторія",
    "Хмельницька Олександра",
    "Хміль Катерина",
    "Чомахашвілі Евеліна",
]

print("0. Демонстрація функцій:")
print("random.random():", random.random())
print("random.randint(1, 10):", random.randint(1, 10))
print(
    "random.choice(['значення1', 'значення2', 'значення3']):",
    random.choice(["значення1", "значення2", "значення3"]),
)

print("\n1. Випадковий вибір одного студента кілька разів:")
for i in range(1, 4):
    print(f"Спроба {i}: {random.choice(group)}")

print("\n2. Вибір кількох студентів:")
selected_students = random.sample(group, k=3)
print("Обрані студенти:", selected_students)

print("\n3. Гра з монеткою:")
coin = ["Орел", "Решка"]
print("Результат одного підкидання:", random.choice(coin))


def flip_coin(times):
    stats = {"Орел": 0, "Решка": 0}
    for _ in range(times):
        stats[random.choice(coin)] += 1
    return stats


res_100 = flip_coin(100)
print(f"100 підкидань: Орел = {res_100['Орел']}, Решка = {res_100['Решка']}")

res_1000 = flip_coin(1000)
print(f"1000 підкидань: Орел = {res_1000['Орел']}, Решка = {res_1000['Решка']}")

print("\n4*. Гра 'Камінь-Ножиці-Папір':")
moves = ["Камінь", "Ножиці", "Папір"]
player = random.choice(moves)
bot = random.choice(moves)

print(f"Гравець: {player}")
print(f"Бот: {bot}")

if player == bot:
    print("Результат: Нічия!")
elif (
    (player == "Камінь" and bot == "Ножиці")
    or (player == "Ножиці" and bot == "Папір")
    or (player == "Папір" and bot == "Камінь")
):
    print("Результат: Переміг Гравець!")
else:
    print("Результат: Переміг Бот!")