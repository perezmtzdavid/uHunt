def sum_digit(value):
    res = 0
    for i in value:
        res += int(i)
    return str(res)


value = input()

while True:
    if value == '0':
        break
    while len(value) != 1:
        value = sum_digit(value)
    print(value)
    value = input()