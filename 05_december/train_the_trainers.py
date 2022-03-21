average_grade_sum = 0
presentations_count = 0

judges_count = int(input())

presentation_name = input()

while presentation_name != 'Finish':
    total_grades = 0

    for judge in range(judges_count):
        grade = float(input())
        total_grades += grade

    average_grade = total_grades / judges_count
    average_grade_sum += average_grade
    presentations_count += 1
    print(f'{presentation_name} - {average_grade:.2f}.')

    presentation_name = input()

print(f"Student's final assessment is {average_grade_sum / presentations_count:.2f}.")
