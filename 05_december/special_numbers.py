number = int(input())

for num in range(1111, 9999 + 1):
    is_special_num = True
    for digit in str(num):
        if int(digit) == 0 or number % int(digit) != 0:
            is_special_num = False
            break
    if is_special_num:
        print(num, end=' ')
