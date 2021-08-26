duration_list = [53, 153, 4153, 400153]
duration = int(input('Введите продолжительность времени в секундах '))
duration_list.append(duration)
minute = 60
hour = minute * 60
day = hour * 24

for duration in duration_list:
    if duration < minute:
        print(f'{duration} сек')
    elif duration < hour:
        print(f'{duration // minute} мин'
              f' {duration % minute} сек')
    elif duration < day:
        print(f'{duration // hour} час'
              f' {(duration % hour) // minute} мин'
              f' {(duration % hour) % minute} сек')
    else:
        print(f'{duration // day} дн'
              f' {(duration % day) // hour} час'
              f' {((duration % day) % hour) // minute} мин'
              f' {((duration % day) % hour) % minute} сек')
