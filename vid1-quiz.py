import time

#Create our quiz variables
introduction = "\n\nWelcome to this mini personality quiz!\n\n"
first_question = "Question 1: You regularly make new friends"
second_question = "Question 2: You often make a back up plan for a back up plan"
third_question = "Question 3: You usually stay calm under pressure"
standard_answers = """Please choose an answer \n\n  1) strongly agree \n  2) agree \n  3) neutral 
  4) disagree \n  5) strongly disagree"""

enter = "Press enter to continue"

#take input 
print(introduction)
print(enter)
input("=>")
print(first_question)
print(standard_answers)
print("\nEnter Answer")
answer1 = int(input("=>"))


print(second_question)
print(standard_answers)
print("\nEnter Answer")
answer2 = int(input("=>"))

print(third_question)
print(standard_answers)
print("\nEnter Answer")
answer3 = int(input("=>"))

#Score our quiz
if answer1 < 3: 
    trait1 = "extroverted"
else:
    trait1 = "introverted"

if answer2 < 3:
    trait2 = "conscientious"

else:
    trait2 = "laid back"

if answer3 < 3:
    trait3 = "Composed"

else:
    trait3 = "nervous"

#Embed the final traits in a string
score = f"Your personality can be described as {trait1}, {trait2} and {trait3}."


#print the final score with DRAMATIC time pause
print("\n\nCalculating your score...")
time.sleep(3)
print(score)
print("\nThanks for taking the quiz! Good Bye!")

exit()






