def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


scores = {}

while True:
    name = input("Enter student name (or done): ")
    if name == "done":
        break
    
    score_input = input(f"Enter score for {name}: ")
    scores[name] = (score_input)


for name, score in scores.items():
    grade = get_letter_grade(score)
    print(f"{name}: {score} {grade}")


if scores:
    average = sum(scores.values()) / len(scores)
    print











#Ask the user to enter student names and scores until they type "done". Store everything in a dictionary. Then print each student with their letter grade, plus the class average at the end.

#Hints:

#Use while True: with a break when input is "done"
#Use float() to convert the score
##Write a function get_letter_grade(score) that returns "A" (90+), "B" (80+), "C" (70+), "D" (60+), or "F"
#Use sum(scores.values()) / len(scores) for the average
#Expected Output:

#Enter student name (or 'done'): Alice
#Enter score for Alice: 92
#Enter student name (or 'done'): Bob
#Enter score for Bob: 74
#Enter student name (or 'done'): Carol
##Enter score for Carol: 85
#E#nter student name (or 'done'): done
#--- Report Card ---
#Alice: 92.0 (A)
#Bob: 74.0 (C)
##Carol: 85.0 (B)
#Class average: 83.67