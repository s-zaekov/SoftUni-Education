num1 = int(input())
num2 = int(input())


for number in range(num1, num2 + 1):
    number_to_str = str(number)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')
