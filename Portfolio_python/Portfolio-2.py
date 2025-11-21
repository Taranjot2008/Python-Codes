#Program to take two numbers from the user and printing their sum
def sum(num1,num2):
    their_sum=num1+num2 #finding their sum by adding them
    return their_sum
#driver code
#taking input of the two numbers from the user
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
their_sum=sum(num1,num2) #assigning the result to the variable
print('The sum if the numbers is :',their_sum)


#Program to find sum of the first n natural numbers
def nsum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
#Driver code
#taking inputs
n=int(input("Enter the number till the sum has to be taken:"))
sum=nsum(n)
print('The sum of n numbers is:',sum)


#Program to add an increment of 5 to nunber and printing the id before and after the increment
def increment(num):
    print('Number is',num)
    print('id of the number before increment',id(num)) #id of the number before increment
    num+=5
    return num
#Driver Code
num=int(input("Enter a number:"))
num=increment(num)
print('Number after increment by 5 is',num)
#id of the number after increment
print('id of the number after increment is',id(num))


#Program to input names and print the full name
def f_name(firs_name,last_name):
    full_name=firs_name+' '+last_name #using concatenation
    return full_name
#Driver code
firs_name=input("Enter your first name:")
last_name=input("Enter  your last name:")
#Calling function
full_name=f_name(firs_name,last_name) #printing full name
print('Your full name is',full_name)


#Program to print mixed fraction where the value of denominator is fixed as 1
def mixedfraction(num,deno=1):
    remainder=num%deno
    quotient=int(num/deno)
    if remainder!=0:
        
        print('The mixed fraction:',quotient,'(',remainder,'/',deno,')')
    else:
        print('The result is a whole number',remainder)
#Driver code
#taking inputs
num=int(input("Enter the numerator"))
deno=int(input("Enter the denominator"))
if num>deno:
    mixedfraction(num,deno)
else:
    print("The given fraction is already a proper fraction")


#Program to print exponential value of the number entered
def POWER(x,y):
    z=1
    for i in range(1,y+1):
        z=x*z
    return z
#Driver code
x=int(input("Enter the base value:"))
y=int(input("Enter the exp value:"))
result=POWER(x,y)
print('The exponential value is:',result)


#Program to print area and perimeter of th given rectangle
def calcAreaPeri(Length,Breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    #a tuple is returned consisting of 2 values area and perimeter
    return (area,perimeter)
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
#value of tuples assigned in order they are returned
area,perimeter = calcAreaPeri(length,breadth)
print("Area is:",area,"\nPerimeter is:",perimeter)


#Program to give values to given traffic lights
def trafficLight():
    signal = input("Enter the colour of the traffic light: ")
    if (signal not in ("RED","YELLOW","GREEN")):
        print("Please enter a valid Traffic Light colour in CAPITALS")
    else:
        value = light(signal) #function call to light()
    if (value == 0):
        print("STOP, Your Life is Precious.")
    elif (value == 1):
        print ("PLEASE GO SLOW.")
    else:
        print("GO!,Thank you for being patient.")
#function ends here
def light(colour):
    if (colour == "RED"):
        return(0);
    elif (colour == "YELLOW"):
        return (1)
    else:
        return(2)
#function ends here
trafficLight()
print("SPEED THRILLS BUT KILLS")
'''
Enter the colour of the traffic light: RED
STOP, Your Life is Precious.
SPEED THRILLS BUT KILLS
'''


#Program to print name and other details of the students
st=((101,"Aman",98),(102,"Raj",91),(103,"Kiara",99),(104,"Timsy",84))
print('S.no','\tRoll no','Name','\tMarks')
for i in range(0,len(st)):
    print((i+1),'\t',st[i][0],'\t',st[i][1],'\t',st[i][2])


#Program to swap the numbers to the same variables
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print('Numbers before swapping:')
print('First Number is',num1)
print('Second Number is',num2)
(num1,num2)=(num2,num1)
print('Numbers after swapping:')
print('First Number is',num1)
print('Second Number is',num2)


#Program to find area and circumference of the circle using user-defined functions
def circle(r):
    area=3.14*r*r
    circum=2*3.14*r
    return (area,circum)
#Driver Code
r=eval(input("Enter the radius of the circle in meters:"))
area,circum=circle(r)
print('Area of the circle is:',area)
print('Circumference if the circle is:',circum)


#Program to take n numbers from the user and printing the maximum and the minimum number
numbers=tuple()
n=int(input("Enter how many numbers you want to input:"))
for i in range(0,n):
    num=int(input())
    numbers=numbers+(num,)
print('The entered numbers are:')
print(num)
print('\nThe max number is:')
print(max(numbers))
print('\nThe min number is:')
print(min(numbers))


#Program to do the following operations on the tuple ODD
'''(a) Display the keys
(b) Display the values
(c) Display the items
(d) Find the length of the dictionary
(e) Check if 7 is present or not
(f) Check if 2 is present or not
(g) Retrieve the value corresponding to the key 9
(h) Delete the item from the dictionary corresponding to the key 9'''
ODD = {1:'One',3:'Three',5:'Five',7:'Seven',9:'Nine'}
print(ODD)
print(ODD.keys())
print(ODD.values())
print(ODD.items())
print(len(ODD))
print(7 in ODD)
print(2 in ODD)
print(ODD.get(9))
del ODD[9]
print(ODD)


#Program to create a dictionary which stores names of the employee
#and their salary
num = int(input("Enter the number of employees whose data to be stored: "))
count = 1
employee = dict() #create an empty dictionary
while count <= num:
    name = input("Enter the name of the Employee: ")
    salary = int(input("Enter the salary: "))
    employee[name] = salary
    count += 1
print("\n\nEMPLOYEE_NAME\tSALARY")
for k in employee:
    print(k,'\t\t',employee[k])


#Program to count the number of times a character occurs in a string
st = input("Enter a string: ")
dic = {} #creates an empty dictionary
for ch in st:
    if ch in dic: #if next character is already in the dictionary
        dic[ch] += 1
    else:
        dic[ch] = 1 #if ch appears for the first time
for key in dic:
    print(key,':',dic[key])


#Program to enter number and its value in words
#Creating a user defined function
def inwords(num):
    numnames={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}

    result=' ' #creating an empty string
    for ch in num:
        key=int(ch)
        value=numnames[key]
        result=result+' '+value
    return result
#Driver Code
num=input("Enter a number:")
words=inwords(num)
print('The number in words is',words)


#Program to take n emails and print the domain and usernames
def process_email_ids(email_ids):
    usernames = []
    domains = []
    for email in email_ids:
        # Split email address into username and domain
        username, domain = email.split('@')
        usernames.append(username)
        domains.append(domain)
    return tuple(email_ids), tuple(usernames), tuple(domains)
def main():
    # Get the number of students
    n = int(input("Enter the number of students: "))
    # Read email IDs
    email_ids = []
    for i in range(n):
        email = input(f"Enter email ID for student {i+1}: ")
        email_ids.append(email)
    # Process email IDs
    email_tuple, usernames_tuple, domains_tuple = process_email_ids(email_ids)
    # Print the tuples
    print("\nEmail IDs:", email_tuple)
    print("Usernames:", usernames_tuple)
    print("Domains:", domains_tuple)
if __name__ == "__main__":
    main()

'''
Enter the number of students: 2
Enter email ID for student 1: abc23df@gmail.com
Enter email ID for student 2: xyg4jf@yahoo.com
Email IDs: ('abc23df@gmail.com', 'xyg4jf@yahoo.com')
Usernames: ('abc23df', 'xyg4jf')
Domains: ('gmail.com', 'yahoo.com')
'''

