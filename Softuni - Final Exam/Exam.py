students_count = int(input())

top_students = 0
between_4_and_499 = 0
between_3_and_399 = 0
fail = 0
total_grade_sum = 0

for _ in range(students_count):
    grade = float(input())
    total_grade_sum += grade
    if grade >= 5:
        top_students += 1
    elif 4 <= grade <= 4.99:
        between_4_and_499 += 1
    elif 3 <= grade <= 3.99:
        between_3_and_399 += 1
    else:
        fail += 1

top_students_percentage = (top_students / students_count) * 100
between_4_and_499_percentage = (between_4_and_499 / students_count) * 100
between_3_and_399_percentage = (between_3_and_399 / students_count) * 100
fail_percentage = (fail / students_count) * 100
average_grade = total_grade_sum / students_count

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_499_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_399_percentage:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
