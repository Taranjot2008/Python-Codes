# User-defined function to check if a student is present in the tuple
def is_student_present(student_name, student_tuple):
    return student_name in student_tuple
def main():
    # Get the number of students
    n = int(input("Enter the number of students: "))
    # Read names and store them in a tuple
    student_names = tuple(input(f"Enter name for student {i+1}: ") for i in range(n))
    # Print the tuple of student names
    print("\nStudent Names:", student_names)
    # Input a name from the user
    search_name = input("\nEnter a name to check if the student is present: ")
    # Using user-defined function to check if the student is present
    if is_student_present(search_name, student_names):
        print(f"{search_name} is present in the tuple.")
    else:
        print(f"{search_name} is not present in the tuple.")
    # Using built-in function to check if the student is present
    if search_name in student_names:
        print(f"{search_name} is present in the tuple (using built-in function).")
    else:
        print(f"{search_name} is not present in the tuple (using built-in function).")
if __name__ == "__main__":
    main()
'''Enter the number of students: 2
Enter name for student 1: Kiara
Enter name for student 2: Jhalak
Student Names: ('Kiara', 'Jhalak')
Enter a name to check if the student is present: Rita
Rita is not present in the tuple.'''


#Program to find top two values of the dictionary
def find_highest_two(dictionary):
    # Get a sorted list of dictionary items by values in descending order
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Extract the top two items
    top_two = sorted_items[:2]
    return top_two
def main():
    # Example dictionary (you can replace this with your own)
    student_scores = {
        'Alice': 90,
        'Bob': 85,
        'Charlie': 95,
        'David': 88,
        'Eve': 92}
    # Find the highest two values in the dictionary
    highest_two = find_highest_two(student_scores)
    # Print the result
    print("Dictionary:", student_scores)
    print("\nTop two values:")
    for name, score in highest_two:
        print(f"{name}: {score}")
if __name__ == "__main__":
    main()


#Program to count the characters in str and printing as a dictionary
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        # Use get() to initialize count to 0 if the character is not in the dictionary
        char_count[char] = char_count.get(char, 0) + 1
    return char_count
def main():
    # Example string (you can replace this with your own)
    input_string = "programming"
    # Create a dictionary to track character counts
    char_count_dict = count_characters(input_string)
    # Print the result
    print(f"Original String: {input_string}")
    print("Character Count:")
    for char, count in char_count_dict.items():
        print(f"{char}: {count}")
if __name__ == "__main__":
    main()


#Program to do following operations:
'''a) Display the name and phone number of all your
friends
b) Add a new key-value pair in this dictionary and
display the modified dictionary
c) Delete a particular friend from the dictionary
d) Modify the phone number of an existing friend
e) Check if a friend is present in the dictionary or
not
f) Display the dictionary in sorted order of names'''

def display_friends(dictionary):
    print("\nFriends and their Phone Numbers:")
    for name, phone in dictionary.items():
        print(f"{name}: {phone}")

def add_friend(dictionary, name, phone):
    dictionary[name] = phone
    print("\nFriend added successfully.")
    display_friends(dictionary)

def delete_friend(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        print("\nFriend deleted successfully.")
        display_friends(dictionary)
    else:
        print("\nFriend not found in the dictionary.")

def modify_phone(dictionary, name, new_phone):
    if name in dictionary:
        dictionary[name] = new_phone
        print("\nPhone number modified successfully.")
        display_friends(dictionary)
    else:
        print("\nFriend not found in the dictionary.")

def check_friend(dictionary, name):
    if name in dictionary:
        print(f"\n{name} is present in the dictionary with phone number: {dictionary[name]}")
    else:
        print(f"\n{name} is not present in the dictionary.")

def display_sorted(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    print("\nDictionary in sorted order of names:")
    display_friends(sorted_dict)

def main():
    friends_dict = {}

    # Add some initial friends (you can remove or modify this)
    friends_dict['Alice'] = '123-456-7890'
    friends_dict['Bob'] = '987-654-3210'

    while True:
        print("\nOperations:")
        print("a) Display friends and phone numbers")
        print("b) Add a new friend")
        print("c) Delete a friend")
        print("d) Modify phone number")
        print("e) Check if a friend is present")
        print("f) Display sorted dictionary")
        print("x) Exit")

        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            display_friends(friends_dict)
        elif choice == 'b':
            name = input("Enter friend's name: ")
            phone = input("Enter friend's phone number: ")
            add_friend(friends_dict, name, phone)
        elif choice == 'c':
            name = input("Enter the name of the friend to delete: ")
            delete_friend(friends_dict, name)
        elif choice == 'd':
            name = input("Enter the name of the friend to modify: ")
            new_phone = input("Enter the new phone number: ")
            modify_phone(friends_dict, name, new_phone)
        elif choice == 'e':
            name = input("Enter the name of the friend to check: ")
            check_friend(friends_dict, name)
        elif choice == 'f':
            display_sorted(friends_dict)
        elif choice == 'x':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

'''Operations:
a) Display friends and phone numbers
b) Add a new friend
c) Delete a friend
d) Modify phone number
e) Check if a friend is present
f) Display sorted dictionary
x) Exit

Enter your choice: a
Friends and their Phone Numbers:
Alice: 123-456-7890
Bob: 987-654-3210

Enter your choice: b
Enter friend's name: Charlie
Enter friend's phone number: 555-123-4567

Friend added successfully.
Friends and their Phone Numbers:
Alice: 123-456-7890
Bob: 987-654-3210
Charlie: 555-123-4567

Enter your choice: c
Enter the name of the friend to delete: Alice

Friend deleted successfully.
Friends and their Phone Numbers:
Bob: 987-654-3210
Charlie: 555-123-4567

Enter your choice: d
Enter the name of the friend to modify: Bob
Enter the new phone number: 999-888-7777

Phone number modified successfully.
Friends and their Phone Numbers:
Bob: 999-888-7777
Charlie: 555-123-4567

Enter your choice: e
Enter the name of the friend to check: Alice

Alice is not present in the dictionary.

Enter your choice: f
Dictionary in sorted order of names:
Bob: 999-888-7777
Charlie: 555-123-4567
'''


#To access any variable outside the function
num = 5
def myfunc1():
#Prefixing global informs Python to use the updated global
#variable num outside the function
    global num
    print("Accessing num =",num)
    num = 10
    print("num reassigned =",num)
#function ends here
myfunc1()
print("Accessing num outside myfunc1",num)


#Program to make a user defined function to check divisibility of a number by 7
def divisibility(num):
    if num%7==0:
        print('The number',num,'is divisible by 7')
    else:
        print('The number',num,'is not divisible by 7')

#Driver Code
num=int(input("Enter a number to check its divisibility by 7:"))
divisibility(num)


#Program to make a user defined function
#allot Mr/Ms as per gender of the user
def gender(gd):
    if gd=='M':
        prefix='Mr' #prefix for M
    else:
        prefix='Ms' #prefix for F
    return prefix
#Driver Code
gd=input("Enter your gender(M/F):")
prefix=gender(gd)
print('As per gender the prefix is',prefix)


#Program to write a user defined function
#to accept numbers and find determinant in the quadratic equation
def quad_eq(a,b,c):
    d=(b**2)-(4*a*c)
    if d>=0:
        print('The result will be a real solution')
    else:
        print('The result will be an imaginary solution')
#Driver Code
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
c=int(input('Enter the value of c:'))
quad_eq(a,b,c)


#program to write a user defined function
#to calculate CI
def compound_interest(P,R,N,T):
    CI=P*(1+R/N)**(N*T)
    return CI
#Driver Code
P=int(input("Enter the principal amount:"))
R=int(input("Enter the rate:"))
N=int(input("Enter the number of times rate is to be compounded:"))
T=int(input("Enter the time period:"))
CI=compound_interest(P,R,N,T)
print('The compound interest for the given time and amount will be',CI)
'''
Enter the principal amount:50000
Enter the rate:4
Enter the number of times rate is to be compounded:2
Enter the time period:1
The compound interest for the given time and amount will be 450000.0
'''

#Program to write a user defined function
#to swap numbers if num1>num2
def swap(num1,num2):
    if num1<num2:
        num1,num2=num2,num1 #swapping will be done
    else:
        num1,num2=num1,num2 # the numbers will remain same
    return (num1,num2)
#Driver Code
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print('The numbers before swapping')
#printing the numbers before swapping
print('Number 1 is:',num1) 
print('Number 2 is:',num2)
num1,num2=swap(num1,num2)
print('The numbers after swapping')
#printing the numbers after swapping if any
print('Number 1 is:',num1)
print('Number 2 is',num2)


#program to make a user defined module
'''
The module name will be a_math module

For calculating the area and perimeter as per the requirement
 Few shapes will taken for example triangle, square, circle and rectangle
The first result will be the area and the corresponding result
will be perimeter of the given shape
'''
def triangle(b,h):
    area=(b*h)/2
    peri=3*b
    return(area,peri)
def square(s):
    area=s**2
    peri=4*s
    return(area,peri)
def circle(r):
    area=3.14*r*r
    peri=2*3.14*r
    return(area,peri)
def rectangle(l,b):
    area=l*b
    peri=2*(l+b)
    return(area,peri)


#Program to generate a gk quiz and tell the final score
import random

def generate_quiz():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
        {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
        {"question": "In which year did the Titanic sink?", "answer": "1912"}
    ]
    random.shuffle(questions)
    return questions

def ask_questions(quiz):
    score = 0
    for question_data in quiz:
        print(f"\nQuestion: {question_data['question']}")
        user_answer = input("Enter your answer: ").strip().title()
        if user_answer == question_data['answer']:
            score += 1
    return score

def remark(score_value):
    if score_value == 5:
        return "Excellent! You got a perfect score."
    elif 3 <= score_value <= 4:
        return "Great job! You did well."
    elif 1 <= score_value <= 2:
        return "You can do better. Keep learning."
    else:
        return "Better luck next time."

def main():
    print("Welcome to the GK Quiz!")
    quiz_questions = generate_quiz()
    user_score = ask_questions(quiz_questions)

    print(f"\nYour final score: {user_score}")
    print(remark(user_score))

if __name__ == "__main__":
    main()

'''
Welcome to the GK Quiz!

Question: Which planet is known as the Red Planet?
Enter your answer: Mars

Question: What is the largest mammal in the world?
Enter your answer: Blue Whale

Question: In which year did the Titanic sink?
Enter your answer: 1912

Question: Who wrote 'Romeo and Juliet'?
Enter your answer: William Shakespeare

Question: What is the capital of France?
Enter your answer: Paris

Your final score: 5
Excellent! You got a perfect score.
'''


#Program to use random module for lottery prize
import random

prize=567

ticket=random.randrange(1,601) #choosing a random ticket number
print('Your ticket number is',ticket)
if ticket==prize:
    print('Congratulations,You are the winner of this lucky draw and you would receive a special prize')
else:
    print('Sorry!!,Better Luck next time')


#Write a program to enter a festival name and search whether the name present in the tuple or not using membership operator. Print appropriate message.
Festival = ('Lumbini', 'Mopin', 'Bihu', 'Chhath', 'Onam', 'Lohri', 'Pongal', 'Garba')
nfest=input("Enter a festival name:").capitalize()
if nfest in Festival:
    print('Yes,The festival',nfest,'is present in the list')
else:
    print('No,The festival',nfest,'is not present in the list')


#Write a program to enter a festival name and search whether the name present in the tuple or not without using membership operator. Print appropriate message.
Festival = ('Lumbini', 'Mopin', 'Bihu', 'Chhath', 'Onam', 'Lohri', 'Pongal', 'Garba')
nfest=input("Enter a festival name:").capitalize()
flag=0
for x in range(len(Festival)):
    if Festival[x]==nfest:
        flag=1
        break
if flag==1:
    print('Yes the festival is present in the tuple')
else:
    print('The festival is not present in the tuple')
        

#Program to create a dictionary of number and its square upto n
n=int(input("Enter a number :"))
for x in range(1,n):
    print(x,':',x**2)


#Program to find the frequency of an item in list using dictionaries
list1=[1,1,1,1,3,5,5,5,6,7,7,6]
freq={}
for x in list1:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
for key,value in freq.items():
    print("%d:%d"%(key,value))


#Program to print dictionary line by line
student={'Ajay':{'Class':'5',
         'Roll no.':'24'},
         'Kriti':{'Class':'6',
         'Roll No.':'17'}}
for a in student:
    print(a)
    for b in student[a]:
        print(b,':',student[a][b])

