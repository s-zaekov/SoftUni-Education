minimal_budget = 0
total_budget = 0

command = input()

while command != 'End':
    destination = command
    minimal_budget = float(input())
    saved_money = 0
    while saved_money < minimal_budget:
        amount_to_save = float(input())
        saved_money += amount_to_save
    print(f'Going to {destination}!')
    command = input()
