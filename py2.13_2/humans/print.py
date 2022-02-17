def print_list(humans):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 16
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^16} |'.format(
            "No",
            "Ф.И.",
            "Телефон",
            "Дата рождения"
        )
    )
    print(line)
    for idx, human in enumerate(humans, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                idx,
                human.get('name', ''),
                human.get('tel', ''),
                human.get('date', 0)
            )
        )
    print(line)

def print_help():
    print("Список команд:\n")
    print("add - добавить человека;")
    print("list - вывести список людей;")
    print("select <месяц> - месяц рождения человека/людей;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def get_command():
    return input(">>> ").lower()
