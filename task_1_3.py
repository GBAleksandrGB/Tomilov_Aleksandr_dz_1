for i, num in enumerate(range(1, 101)):

    if 10 < num < 15:
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    elif 1 < num % 10 < 5:
        print(num, 'процента')
    else:
        print(num, 'процентов')
