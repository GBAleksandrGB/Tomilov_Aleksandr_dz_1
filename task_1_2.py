numbers = []
sum_numbers = []

for num in range(1, 1001, 2):
    numbers.append(num ** 3)

print(numbers)

for el in numbers:
    sum_number = 0
    number = el

    while el:
        sum_number = sum_number + el % 10
        el = el // 10

    if sum_number % 7 == 0:
        sum_numbers.append(number)

print(sum(sum_numbers))

sum = 0
for el in numbers:
    sum_number = 0
    el = el + 17
    number = el

    while el != 0:
        sum_number = sum_number + el % 10
        el = el // 10

    if sum_number % 7 == 0:
        sum += number
print(sum)
