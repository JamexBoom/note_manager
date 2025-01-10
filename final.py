
# Создаем словарь
note = {}


# Запрашиваем информацию у пользователя
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна','Выполнена'): ")


# Переменные для проверки введенной даты создания заметки
created_date_day = 0
created_date_month = 0
created_date_year =0

# Переменные для проверки введенной даты истечения заметки
issue_date_day = 0
issue_date_month = 0
issue_date_year =0

# Список месяцев
monthList = ["Января","Февраля","Марта","Апреля","Мая","Июня","Июля","Августа","Сентября","Октября","Ноября","Декабря"]


# Проверяем корректность ввода ответа
if note.get("status") != "Активна" and note.get("status") !="Выполнена":
    print("Не корректное значение!!!")
    note["status"] = input("Введите статус заметки (например, 'Активна','Выполнена'): ")

else:
    created_date = input("Введите дату создания заметки в формате 'день-месяц-год Пр. 01-02-2025': ")

    # Проверяем корректность введенной даты создания заметки
    if  (created_date.__len__())==10:
        if ((created_date[0:2]).isdigit()):     # Проверяем день
            created_date_day = int(created_date[0:2])
            if not (created_date_day >= 1 and created_date_day <= 31):
                print("Ошибка ввода даты день")
                exit()
            else:

                if created_date[2] != "-":
                    print("Ошибка ввода даты день")
                    exit()
                else:
                    if ((created_date[3:5]).isdigit()):    # Проверяем месяц
                        created_date_month = int(created_date[3:5])
                        if not (created_date_month >= 1 and created_date_month <= 12):
                            print("Ошибка ввода даты месяц")
                            exit()
                        else:
                            if created_date[5] != "-":
                                print("Ошибка ввода даты месяц")
                                exit()
                            else:
                                if ((created_date[6:10]).isdigit()):  # Проверяем год
                                    created_date_year = int(created_date[6:10])
                                    if not (created_date_year >= 1900 and created_date_year <= 2900):
                                        print("Ошибка ввода даты год")
                                        exit()
                                    else:
                                        note["created_date"] = created_date
                                        note["created_date_day"] = created_date_day
                                        note["created_date_month"] = created_date_month
                                        print("Ок")
    else:
        print("Ошибка ввода даты")


    issue_date = input("Введите дату истечения заметки в формате день-месяц-год Пр. 01-02-2025': ")

# Проверяем корректность введенной даты создания заметки
if  (issue_date.__len__())==10:
    if ((issue_date[0:2]).isdigit()):     # Проверяем день
        issue_date_day = int(issue_date[0:2])
        if not (issue_date_day >= 1 and issue_date_day <= 31):
            print("Ошибка ввода даты день")
            exit()
        else:
            if issue_date[2] != "-":
                print("Ошибка ввода даты день")
                exit()
            else:
                if ((issue_date[3:5]).isdigit()):    # Проверяем месяц
                    issue_date_month = int(issue_date[3:5])
                    if not (issue_date_month >= 1 and issue_date_month <= 12):
                        print("Ошибка ввода даты месяц")
                        exit()
                    else:
                        if issue_date[5] != "-":
                                print("Ошибка ввода даты месяц")
                                exit()
                        else:
                            if ((issue_date[6:10]).isdigit()):  # Проверяем год
                                    issue_date_year = int(issue_date[6:10])
                                    if not (issue_date_year >= 1900 and issue_date_year <= 2900):
                                        print("Ошибка ввода даты год")
                                        exit()
                                    else:
                                        note["issue_date"] = issue_date
                                        note["issue_date_day"] = issue_date_day
                                        note["issue_date_month"] = issue_date_month
                                        print("Ок")

else:
    print("Ошибка ввода даты")


# Запрашиваем несколько заголовков и добавляем их в список
note["titles"] = []

for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)


# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", note.get("username"))
print("Описание заметки:", note.get("content"))
print("Статус заметки", note.get("status"))
print("Дата создания заметки", str(note.get("created_date_day")) + "-" + str(monthList[note.get("created_date_month")-1]))
print("Дата истечения заметки:",str(note.get("issue_date_day")) + "-" + str(monthList[note.get("issue_date_month")-1]))


# Определяем длину списка
listlen = note.get("titles").__len__()

# Вывод заголовков заметки
for i in range(listlen):
    print(f"Заголовок заметки {i + 1}: ",note.get("titles").__getitem__(i))
