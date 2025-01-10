# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна','Выполнена'): ")



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
if status !="Активна" and status !="Выполнена":
    print("Не корректное значение!!!")
    status = input("Введите статус заметки (например, 'Активна','Выполнена'): ")

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
                                        print("Ок")

else:
    print("Ошибка ввода даты")

# Запрашиваем несколько заголовков и добавляем их в список

titles = []

titles.append(input("Введите первый заголовок заметки: "))
titles.append(input("Введите второй заголовок заметки:: "))
titles.append(input("Введите третий заголовок заметки:: "))


# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Введите описание заметки:", content)
print("Заголовок заметки:",titles)
print("Статус заметки", status)
print("Дата создания заметки", str(created_date_day) + "-" + str(monthList[created_date_month-1]))
print("Дата истечения заметки:",str(issue_date_day) + "-" + str(monthList[issue_date_month-1]))