# Python program to find largest
# number in a list
 
# list of numbers
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the last element
print("Largest element is:", list1[-1])


# Python program to find largest
# number in a list
 
 
def myMax(list1):
 
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]
# Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x > max:
            max = x
 
    # after complete traversing the list
    # return the "max" value
    return max
 
 
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))

# Python3 program to count upper and
# lower case characters without using
# inbuilt functions
def upperlower(string):
 
    upper = 0
    lower = 0
 
    for i in range(len(string)):
         
        # For lower letters
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            lower += 1
 
        # For upper letters
        elif (ord(string[i]) >= 65 and
            ord(string[i]) <= 90):
            upper += 1
 
    print('Lower case characters = ' ,lower,
        'Upper case characters = ' ,upper)
 
# Driver Code
string = input('Enter your string:')
upperlower(string)



#Python program to count number of vowels
def vowels(str):

    #initial count of vowels
    count=0

    #number of vowels in string
    for i in range(len(str)):

        #vowels are aeiouAEIOU 
        if str[i] in 'aeiouAEIOU':
            count+=1

    return count
#driver code
str=input('Enter your string:')
print('The number of vowels in the given string are:',vowels(str))



#Python program to count initials
#with dot in between
def initials(full_name):
    if len(full_name)==0:
        return
    initials=""
    first_middle_last=full_name.split(" ")
    for name in first_middle_last:
        initials+=name[0].upper()+'.'
    return initials
#driver code
full_name=input('Enter yoour full name:')
print('Your initials are:',initials(full_name))


#Program to increment the elements of the list passed as argument
def increment(list2):
    for i in range(0,len(list2)):
        #5 is added to individual elements in the list
        list2[i] += 5
        print('Reference of list Inside Function',id(list2))
        #end of function
        list1 = [10,20,30,40,50] #Create a list
        print("Reference of list in Main",id(list1))
        print("The list before the function call")
        print(list1)
        increment(list1) #list1 is passed as parameter to function
print("The list after the function call")
print(list1)


#Program to increment the elements of the list passed as argument
def increment(list2):
    print("\nID of list inside function before assignment:",
id(list2))
list2 = [15,25,35,45,55] #List2 assigned a new list
print("ID of list changes inside function after assignment:",
id(list2))
print("The list inside the function after assignment is:")
print(list2)
#end of function
list1 = [10,20,30,40,50] #Create a list
print("ID of list before function call:",id(list1))
print("The list before function call:")
print(list1)
increment(list1) #list1 passed as parameter to function
print('\nID of list after function call:',id(list1))
print("The list after the function call:")
print(list1)

'''Output:
ID of list changes inside function after assignment: 1662957443328
The list inside the function after assignment is:
[15, 25, 35, 45, 55]
ID of list before function call: 1662957440576
The list before function call:
[10, 20, 30, 40, 50]

ID of list inside function before assignment: 1662957440576

ID of list after function call: 1662957440576
The list after the function call:
[10, 20, 30, 40, 50]
'''


#Program to calculate average marks of n students
def averagemarks(list1,n):
    total=0
    for marks in list1:
        total+=marks
    average=total/n
    return average
list1=[]

n=int(input('Enter the number of students:'))
for i in range(0,n):
    print('Enter marks of student',i+1,':')
    marks=int(input())
    list1.append(marks)
average=averagemarks(list1,n)
print('Average marks of the students is:',average)


#Program to search for a number in string and tell it’s position
def listsearch(list1,num):
    for i in range(0,len(list1)):
        if list1[i]==num:
            return i
    return None
list1=[]
print('Enter the number of characters to be searched:')
maximum=int(input())
print('Enter the numbers:')
for i in range(0,maximum):
    n=int(input())
    list1.append(n)
num=int(input('Enter the number to be searched:'))
result=listsearch(list1,num)
if result is None:
    print('The number',num,'is not present')
else:
    print('The number',num,'is present at',result+1,'location')


#Program to find a given character in the given string
def search(ch,str):
    #initial count of the character
    count=0
    for character in str:
        #if the character is same as the character to be searched
        if character==ch:
            count+=1
    return count #returns the count of character

str=input('Enter the string')
ch=input('Enter the character to be searched')
count=search(ch,str)
#number of times a character is occuring in the string
print('The character',ch,'repeats',count,'times in the string')


# Program: Count number of vowels in a String in Python

example = "Count number of vowels in a String in Python"

# initializing count variable
count = 0

# creating a list of vowels
vowels = ["a", "e", "i", "o", "u"]

# iterate over the given string (example)
# len(example) -> gives the length of the string in Python
# Note that python can also declare the variable at the time of calling
for i in range(len(example)):
    if example[i] in vowels:
        count += 1

print("Number of vowels in the given string is: ", count)


#Program to replace the vowels with '*'
def replacevowels(str):
    #creating a new empty string
    newstr=""
    #searching for every character in string
    for character in str:
        if character in 'aeiouAEIOU':
            newstr+='*'
        else:
            newstr+=character #character which is not a vowel is printed
    return(newstr)
str=input('Enter you string')
newstr=replacevowels(str)
print('The original string is:',str) #old string
print('The modified string is:',newstr) #string with '*' in place of vowels


#Program to display string in reverse order
st = input("Enter a string: ")
for i in range(-1,-len(st)-1,-1):
    print(st[i],end='')


#Program to reverse a string using user defined function
def reverse(str):
    newstr="" #create a new empty string
    length=len(str) #finding the length of the string
    for i in range(-1,-length-1,-1):
        newstr+=str[i] #adding the reversed characters in the newstr
    return newstr
str=input('Enter the string:')
newstr=reverse(str)
print('The original string:',str)
print('The reversed string is:',newstr)


#Program to check if a given string is palindrome or not
def checkPalin(str):
    i=0
    j=len(str)-1
    while i<=j:
        if(str[i] != str[j]):
            return False
        i+=1
        j-=1
    return True

str=input('Enter the string:')
result=checkPalin(str)
if result==True:
    print('The given string is a palindrome')
else:
    print('The given string is not a palindrome')

'''
Output:
Enter the string:kanak
The given string is a palindrome
'''

#Program to count number of times an element occurs in list
list=input("Enter a list:")
n=input("Enter the element to be counted:")
count=list.count(n)
print('Number of times',n,'repeats is',count)


#Program to print the second largest number in list

list=input('Enter you list:')
list=list.split(',')
list.sort()
print(list[-2])


#Program to return the min and max number of the given list
list1=[2,5,7,10,15,23]
list1.sort()
print("Min number is ",list1[0])
print("Max number is:",list1[-1])


#Program of item to be searched and its position in list
ListB=["AP","MP","UP","CG"]
ListB.sort()
item_search=input("Enter the item to be searched:") #item to be searched
position=ListB.index(item_search)+1 #telling its position
print('The item to be searched',item_search,'is present at position:',position)


#Program to find marks of students and return max and min
# list of numbers
list1 =input("ENter your list of marks:")

list1=list1.split(',')
# sorting the list
list1.sort()
 
# printing the last element
print("highest mark is:", list1[-1])
print("lowest mark is :",list1[0])


#Program to have an increment of 10 to each element of list
def increment(ListA):
    for i in range(0,len(ListA)):
        ListA[i]+=10 #Adding 10 to each element
    return ListA
ListA=[1,5,7,10,15,23,77]
ListA=increment(ListA)
print(ListA)


#Program to input marks of student and count number of children who have gotten more than 70 marks
def morethan(List2):
    count=0
    for i in range(0,len(List2)):
        if List2[i]>70:
            count+=1
    return count
List2=eval(input("Enter the marks of the students:"))

count=morethan(List2)
print('Number of children who have gotten more than 70 marks are:',count)


#Program to print largest and smallest in tuple
def maxmin(TupleAge):
    largest=max(TupleAge)
    smallest=min(TupleAge)

    return(largest,smallest)
TupleAge=(2, 5, 7, 10, 15, 23)
(largest,smallest)=maxmin(TupleAge)
print('Max number is ',largest)
print('Min number is ',smallest)


#Program to sort a tuple
EmpT=("Gyanesh", "Akash", "Pradeep", "Brijendra")
list1=list(EmpT) #converting tuple into list
list1.sort()
EmpT=tuple(list1) #reconverting list into tuple
print('The sorted tuple is:',EmpT)


#Program to print Highest lowest rate and the total
RateTuple=(50, 15, 2, 35, 40)
list=list(RateTuple)
list.sort()
total=0
for i in range(0,len(list)):
    total+=list[i]

RateTuple=tuple(list)
print('Lowest rate is ',RateTuple[0])
print('Highest rate is ',RateTuple[-1])
print('Total of the rates is ',total)


#Program to print item and price of dictionary
DItem={'Pen' :'Rs. 20', 'Eraser' : 'Rs. 3.50', 'Ruler' : 'Rs. 10', 'Copy' : 'Rs. 35', 'Compass' : 'Rs. 70'}
print("Items and their price is:")
for items,price in DItem.items():
    print(f"{items}:{price}")


#Program to create dictionary with months and days
DYear={ "jan" : 31 , "feb" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "aug" : 31 , "sept" : 30 , "oct" : 31 , "nov" : 30 , "dec" : 31}
print('THe month and number of days in it are:')
for months,days in DYear.items():
    print(f"{months}:{days}")
'''
The month and number of days in it are:
jan:31
feb:28
march:31
april:30
may:31
june:30
july:31
aug:31
sept:30
oct:31
nov:30
dec:31
'''

#Program to swap elements of the list
def swap_adjacent_elements(lst):
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]


ListA = [1, 5, 7, 10, 15, 23]
swap_adjacent_elements(ListA)
print(ListA)



#Program to half even and double odd elements
def double_half(ListA):
    for i in range(len(ListA)):
        if ListA[i]%2==0:
            ListA[i]/=2
        else:
            ListA[i]*=ListA[i]
    return ListA[i]
ListA=[1, 5, 7, 10, 15, 23]
double_half(ListA)
print(ListA)


#program to show bubblesort
def bubblesort(theSeq):
    n=len(theSeq)
    
    for i in range(n-1):
        flag=0
        
        for j in range(n-1):
            if theSeq[j]>theSeq[j+1]:
                tmp=theSeq[j]
                theSeq[j]=theSeq[j+1]
                theSeq[j+1]=tmp
                flag=1
        if flag==0:
            break
    return theSeq
el=[21,6,9,33,3]
print('Unsorted array:',el)

result=bubblesort(el)
print('Sorted Array:',result)
'''Unsorted array: [21, 6, 9, 33, 3]
Sorted Array: [3, 6, 9, 21, 33]
'''


#Program to count vowels in the given string
str=input("Enter a string:")
vowels="a,e,i,o,u,A,E,I,O,U" #string with vowels
count=0 #initial count
for char in str:
    if char in vowels:
        count+=1
print('Number of vowels in the given string are:',count)



#Program to count the number of vowels in a string using concepts of lists
str=input("Enter a string:")
vowels=['a','e','i','o','u','A','E','I','O','U'] #list of vowels
wordlist=str.split(" ")
count=0 #initial count
for word in wordlist: 
    for i in range(len(word)):
        if word[i] in vowels:
            #increasing the count by 1
            count+=1
print("Number of vowels in the string are:",count)


#Program to calculate the cost of tent
#function definition
def cyl(h,r):
    area_cyl = 2*3.14*r*h #Area of cylindrical part
    return(area_cyl)
#function definition
def con(l,r):
    area_con = 3.14*r*l #Area of conical part
    return(area_con)
#function definition
def post_tax_price(cost): #compute payable amount for the tent
    tax = 0.18 * cost;
    net_price = cost + tax
    return(net_price)
print("Enter values of cylindrical part of the tent in meters:")
h = float(input("Height: "))
r = float(input("Radius: "))
csa_cyl = cyl(h,r) #function call
l = float(input("Enter slant height of the conical area in meters: "))
csa_con = con(l,r) #function call
#Calculate area of the canvas used for making the tent
canvas_area = csa_cyl + csa_con
print("Area of canvas = ",canvas_area," m^2")
#Calculate cost of canvas
unit_price = float(input("Enter cost of 1 m^2 canvas in rupees: "))
total_cost = unit_price * canvas_area
print("Total cost of canvas before tax = ",total_cost)
print("Net amount payable (including tax) = ",post_tax_price(total_cost))

'''
Enter values of cylindrical part of the tent in meters:
Height: 2
Radius: 5
Enter slant height of the conical area in meters: 4
Area of canvas =  125.60000000000001  m^2
Enter cost of 1 m^2 canvas in rupees: 500
Total cost of canvas before tax =  62800.00000000001
Net amount payable (including tax) =  74104.0
'''