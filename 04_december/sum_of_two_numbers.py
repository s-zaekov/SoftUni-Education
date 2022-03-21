start_interval = int(input())
end_interval = int(input())
magical_number = int(input())
combinations_counter = 0
combination_is_found = False

for n1 in range(start_interval, end_interval + 1):
    for n2 in range(start_interval, end_interval + 1):
        combinations_counter += 1
        if n1 + n2 == magical_number:
            combination_is_found = True
            break
    if combination_is_found:
        break


if combination_is_found:
    print(f'Combination N:{combinations_counter} ({n1} + {n2} = {magical_number})')
else:
    print(f'{combinations_counter} combinations - neither equals {magical_number}')
