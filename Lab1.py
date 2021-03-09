import string
import random
import time
# #Q1
# name = input("Name: ")
# age = eval(input("Age: "))
# print(age)
# year=100-age+2021
# print("Dear "+name+", You will be a 100 at ",year)

# #Q2
# numb = eval(input("Enter a number: "))

# if numb%2==0:
#     print("Its an even number");
# else:
#     print("Its an odd number");

# #Q3
# a = [1,1,2,3,5,8,13,21,34,55,89]
# for a in range(6):
#     print(a)


# #Q4
# numb = eval(input("Enter a number: "))
# divisor=numb
# list=[]

# for divisor in range(divisor,0,-1):
#     if numb!=1:
#         if numb%divisor==0:
#             list.append(divisor)
# print(list)


# #Q5
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# same=[]

# for i in a:
#     for j in b:
#         if i==j:
#             same.append(i)
            
# print(same)

# #Q6
# word=input("Enter a word: ")
# check="";

# for i in word:
#     check=i+check

# if(check==word):
#     print(word+" is a Palindrome")
# else:
#     print(word+" is NOT a Palindrome")
# ####################### ni kalau guna predefined fx
# # check=''.join(reversed(word))
# # print(check)
    
# #Q7
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [i for i in a if i%2==0] #list-comprehension
# print(b)

# #Q8
# flag=True

# while flag==True:
#     player1=eval(input("P1 - Rock[1] Paper[2] or Scissors[3] ? "))
#     print()
#     player2=eval(input("P2 - Rock[1] Paper[2] or Scissors[3] ? "))
    
#     if (player1==1 and player2==1) or (player1==2 and player2==2) or (player1==3 and player2==3):
#         print("DRAW!")
#     elif(player1==1 and player2==3) or (player1==3 and player2==2) or (player1==2 and player2==1):
#         print("Player 1 WINS")
#     elif(player2==1 and player1==3) or (player2==3 and player1==2) or (player2==2 and player1==1):
#         print("Player 2 WINS")
#     print()
#     check=input("Do you want to start a new game? [Y,N] : ")
#     if(check=="N"):
#         flag=False;

# #Q9
# 
# RandNo=random.randint(1,9)
# print(RandNo)
# guess=eval(input("Guess the random number : "))

# if guess==RandNo:
#     print("Exactly RIGHT!")
# elif guess<RandNo:
#     print("You guessed too LOW, its ",RandNo)
# elif guess>RandNo:
#     print("You guessed too HIGH, its ",RandNo)

# #Q10
# numb = eval(input("Enter a number: "))
# divisor=numb-1
# flag=True

# for divisor in range(divisor,1,-1):
#     if numb!=1:
#         if numb%divisor==0:
#             flag=False

# if flag==True:
#     print(str(numb)+" is a prime number")
# else:
#     print(str(numb)+" is NOT a prime number")

# #Q11
# a = [5, 10, 15, 20, 25]


# def FirstLast(a):
#     b=[]
#     b.append(a.pop(0))
#     b.append(a.pop(len(a)-1))
#     return b;

# print(FirstLast(a))

# #Q12
# n=eval(input("Enter value of n : "))

# def Fibonacci(n):
#     list=[0,1]
#     for i in range(1,n-1,+1):
#         list.append(list[i-1]+list[i])
#     return list;

# print(Fibonacci(n))

# #Q13
# a = [5, 10, 15, 20, 25,5,10,25]

# def Unduplicate(a):
#     newlist=[]
#     for i in a:
#         if i not in newlist:
#             newlist.append(i)
#     return newlist;

# print(Unduplicate(a))

# #Q14
# sentence=input("Enter a sentence : ")
# x=sentence.split()
# y=""
# for i in x :
#     y=i+" "+y
# print(y)

#Q15
startTime=time.time()
def password(userInput):
    specialCharacter = [random.choice(string.punctuation) for character in range(userInput)]
    wordLower = [random.choice(string.ascii_lowercase) for lower in range(userInput)]
    wordUpper = [random.choice(string.ascii_uppercase) for upper in range(userInput)]
    numbers = [random.choice(string.digits) for number in range(userInput)]
    generatedPassword = ''.join(specialCharacter + wordLower + wordUpper + numbers)
    generatedPassword = ''.join(random.choice(generatedPassword) for value in range(userInput))
    return generatedPassword

question = eval(input("Please enter the password length: "))
answer = password(question)
print(answer)
endTime=time.time()
print("Time-Complexity : ",endTime-startTime)