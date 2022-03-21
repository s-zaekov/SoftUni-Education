student_tickets = 0
standard_tickets = 0
kid_tickets = 0

movie_name = input()

while movie_name != 'Finish':
    free_seats = int(input())
    seats_taken = 0

    ticket_type = input()
    while ticket_type != 'End':

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        seats_taken += 1
        if free_seats - seats_taken == 0:
            break
        ticket_type = input()

    print(f"{movie_name} - {seats_taken / free_seats * 100:.2f}% full.")
    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')
