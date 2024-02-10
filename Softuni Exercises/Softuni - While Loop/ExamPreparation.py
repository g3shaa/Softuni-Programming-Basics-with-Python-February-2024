max_bad_grade = int(input())
bad_grades = 0
is_excl = False
total_probs = 0
avg_grade = 0
last_prob = ""
prob = input()
while prob != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1
        if bad_grades == max_bad_grade:
            is_excl = True
            break
    avg_grade += current_grade
    total_probs += 1
    last_prob = prob
    prob = input()
if is_excl:
    print(f"You need a break, {max_bad_grade} poor grades.")
else:
    avg = avg_grade / total_probs
    print(f"Average score: {avg:.2f}")
    print(f"Number of problems: {total_probs}")
    print(f"Last problem: {last_prob}")