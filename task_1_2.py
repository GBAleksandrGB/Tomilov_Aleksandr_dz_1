numbers = []
sum_numbers = []

for num in range(1, 1001):
    if num % 2 != 0:
        numbers.append(num ** 3)

print(numbers)

for el in numbers:
    sum_number = 0

    while el != 0:
        sum_number = sum_number + el % 10
        el = el // 10

    if sum_number % 7 == 0:
        sum_numbers.append(sum_number)

print(sum(sum_numbers))

for el in numbers:
    sum_number = 0
    el = el + 17

    while el != 0:
        sum_number = sum_number + el % 10
        el = el // 10

    if sum_number % 7 == 0:
        print(sum(sum_numbers))
