test1 = int(input('Enter score 1: '))
test2 = int(input('Enter score 2: '))
test3 = int(input('Enter score 3: '))
test4 = int(input('Enter score 4: '))
test5 = int(input('Enter score 5: '))

total =(test1 + test2 + test3 + test4 + test5)

#Calculate average
def calculate_average(total):
    return total / 5

#Grading scale
def get_score(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

#get the average
grade = total
average = calculate_average(total)
letter_grade = get_score(grade)
#print the average
print("That's a(n): " + str(letter_grade))
print('Average grade is: ' + str(average))
