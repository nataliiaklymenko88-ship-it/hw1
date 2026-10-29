import re


def get_words(text: str) -> list[str]:
    return re.findall(r"\b[а-яіїєґa-z'’-]+\b", text.lower())


def get_letters(text: str) -> list[str]:
    return re.findall(r"[а-яіїєґa-z]", text.lower())


def frequency_dictionary_percentage(text: str) -> dict[str, float]:
    words = get_words(text)
    if not words:
        return {}

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    total_words = len(words)
    percentages = {
        word: round((count / total_words) * 100, 2)
        for word, count in counts.items()
    }
    return dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True))


def shortest_words(text: str) -> list[str]:
    words = set(get_words(text))
    if not words:
        return []
    min_len = min(len(word) for word in words)
    return sorted([word for word in words if len(word) == min_len])


def longest_words(text: str) -> list[str]:
    words = set(get_words(text))
    if not words:
        return []
    max_len = max(len(word) for word in words)
    return sorted([word for word in words if len(word) == max_len])


def count_unique_words(text: str) -> int:
    words = get_words(text)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return len(counts)


def count_total_words(text: str) -> int:
    return len(get_words(text))


def used_letters(text: str) -> list[str]:
    letters = get_letters(text)
    counts = {}
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1
    return sorted(list(counts.keys()))


def most_frequent_letter(text: str) -> list[str]:
    letters = get_letters(text)
    if not letters:
        return []

    counts = {}
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    max_count = max(counts.values())
    return sorted([letter for letter, count in counts.items() if count == max_count])


if __name__ == "__main__":
    text_data = """
   1-ше місце

Дмитро Леонов, голова Ради Української асоціації інвестиційного бізнесу

Українська асоціація інвестиційного бізнесу (УАІБ) заснована в 1995 р. і вважається однією з найстаріших в Україні організацій учасників фондового ринку. З 2007 р. Раду цієї організації очолює відомий економіст Дмитро Леонов.

Інвестиційною діяльністю пан Леонов почав цікавитися ще у 1990-ті роки. 1997 р. він захистив дисертацію на тему «Інвестиційні фонди на фінансовому ринку України». Протягом наступних декількох років будував наукову кар’єру, отримавши вчене звання професора. Крім того, Дмитро Леонов брав активну участь у створенні законопроектів, проектів президентських указів та інших документів, спрямованих на трансформацію фінансового сектора, фондового ринку, корпоративного управління, оподатковування та інвестиційної діяльності.

2-ге місце

Олена Кошарна, головний виконавчий директор компанії Horizon Capital

Співзасновник однієї з найбільших та найвпливовіших інвестиційних компаній України Horizon Capital Олена Кошарна почала активну діяльність в Україні 1993 р. З 2003 р. вона обіймала посаду головного фінансового директора компанії. До її компетенції належало керівництво фінансовою та операційною діяльністю. Окрім того, пані Кошарна займалася консультуванням інвестиційної команди та портфельних компаній зі стратегічних та фінансових питань.

З грудня 2014 р. Олена Кошарна стала головним виконавчим директором Horizon Capital. Вона неодноразово заявляла про необхідність розвитку української економіки та інвестування у вітчизняний бізнес. За її словами, протягом наступних п’яти років Horizon Capital планує інвестувати в українську економіку $100-200 млн, оскільки її керівництво вбачає перспективи українських підприємств та ринку.

3-тє місце

Томаш Фіала, генеральний директор інвестиційної компанії Dragon Capital

Томаш Фіала є ініціатором створення та незамінним очільником інвесткомпанії Dragon Capital з 2000 р. До цього він отримав великий досвід у різних країнах. Так, з 1994 р. пан Фіала працював інвестиційним банкіром у празькому Bayerische Vereinsbank. З 1995 р. тісно співпрацював з одним з найпередовіших інвестиційних банків у Центральній та Східній Європі Wood&Co, у тому числі в українському та польському відділеннях цієї фінансової установи.
    """

    print("Частотний словник у %:", frequency_dictionary_percentage(text_data))
    print("Найкоротші слова:", shortest_words(text_data))
    print("Найдовші слова:", longest_words(text_data))
    print("Кількість унікальних слів:", count_unique_words(text_data))
    print("Кількість слів:", count_total_words(text_data))
    print("Використані літери:", used_letters(text_data))
    print("Найчастіша літера:", most_frequent_letter(text_data))
