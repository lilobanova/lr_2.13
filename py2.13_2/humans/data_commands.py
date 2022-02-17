from datetime import datetime


def add():
    name = input("Фамилия и имя: ")
    tel = input("Номер телефона: ")
    dateString = input("День рождения: ")
    human = {
        'name': name,
        'tel': tel,
        'date': datetime.strptime(dateString, "%Y-%m-%d")
    }
    return human


def select(command, humans):
    parts = command.split(' ', maxsplit=1)
    period = int(parts[1])
    count = 0
    for human in humans:
        if human['date'].month == period:
            count += 1
            print(
                '{:>4}: {}'.format(count, human.get('name', ''))
            )
    if count == 0:
        print("В этом месяце ни у кого нет дня рождения.")
