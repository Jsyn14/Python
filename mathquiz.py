#Jayson Hamilton 
name = input("What is your name? ")
print("Hello, "+name+". You will be completing a quiz that will ask you 10 questions which will test you on adding, subtracting and multiplying two numbers together. Try your best at each question and good luck!")

import random
from operator import add, sub, mul

count = 0
score = 0
while count <= 9:
    ops = (add, sub, mul)
    op = random.choice(ops)
    x = random.randint(1,10)
    y = random.randint(1,10)

    if op == add:
        print("What is", x, "+",y, "? ")
        question_add = int(input())
        answer_add = op(x,y)
        if question_add == answer_add:
            print("Well done, this is correct!")
            score = score + 1
            count = count + 1
        else:
            print("Sorry, but this is incorrect.")
            count = count + 1

    elif op == sub:
        print("What is", x, "-", y, "? ")
        question_sub = int(input())
        answer_sub = op(x,y)
        if question_sub == answer_sub:
            print("Well done, this is correct!")
            score = score + 1
            count = count + 1
        else:
            print("Sorry, but this is incorrect.")
            count = count + 1

    elif op == mul:
        print("What is", x, "x", y, "? ")
        question_mul = int(input())
        answer_mul = op(x,y)
        if question_mul == answer_mul:
            print("Well done, this is correct!")
            score = score + 1
            count = count + 1
        else:
            print("Sorry, but this is incorrect.")
            count = count + 1

    if count == 10:
        print("Well done "+name+"! You have completed the quiz. Your final score is "+str(score)+" out of 10.")
