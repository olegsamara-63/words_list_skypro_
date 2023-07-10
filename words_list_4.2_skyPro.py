# программа угадай и напиши на русском языке английское слово с подсказками
print("Введите ваше Имя: ...") #программа знакомится с пользователем
name_guestons = input() #пользователь представляется , набирает своё Имя

#создётся список лёгкого уровня
words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}
#создётся список среднего уровня ключ - слово на английком языке , значение - это перевод слова на русском языке
words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}
#создётся список среднего уровня ключ - слово на английком языке , значение - это перевод слова на русском языке
words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}
# создан список уровней - в нём ключ это кол-во правильных ответов т.е.переводов и знасение - название уровня знаний пользователя
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
#список уровней - ключ это название уровня для выбора пользователю , значение - для выбора программой с каким списком сравнивать введённые слова - переводы
hards = {
    "легкий": words_easy,
    "средний": words_medium,
    "сложный": words_hard,
}

answers = {} #список , куда добавляются ответы , введёные пользователем

right_answers = 0 #счётчик правильных ответов для дальнейшего сравнения с ключами из списка ранг и вывода значения  - названия ранга

hard = input(f"Ну что же, {name_guestons}, начнём!, Выбарайте сложность вопросов, \nнаберите легкий, средний или сложный...") #программа призывает пользователя к выбору уровня допроса

work_dict = hards[hard]
for key, value in work_dict.items():
    answer = input(f"Напишите как переводится слово {key}, \n подсказка: в слове {len(value)} букв, слово начинается на букву- {value[0]} \nитак Ваш ответ:...")
    if answer == value:
        print(f"Ваш ответ правильный , перевод слова {key} это - {value}")
    else:
        print(f"Вы неправильно перевели слово {key}, это слово не - {answer}, а {value}")
    answers[key] = answer == value #ответ совпал со значением из списка

print(f"{name_guestons}, Вы правильно угадали следующие слова: ...")
for word, bool_value in answers.items(): #процесс сравнивания и счётчик прибавляется на 1 для подсчёта Ранга и сравнения с ключами из списка Ранга
    if bool_value is True:
        print(word)
        right_answers += 1

print(f"А теперь обманка, все неправильно переведённые Вами слова : ...") #Вывод слов с неправильным переводом
for word, bool_value in answers.items():
    if bool_value is False:
        print(word) #Все слова , которые не совпали со значением (value) из списка слов - выводятся на показ

print(f"В результате {name_guestons}, Ваш ранг: {levels[right_answers]}") #Обращение к пользователю и вывод для ознакомления - названия т.е.значения из списка Ранга как результат


