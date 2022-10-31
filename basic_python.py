'''
This note for basic python
'''

#basic print world


print('Hello Word') #it's valid
print("Hello Word") #it's also valid

#print describe variable
Name = 'Lissa'
print(Name)

#print describe variable by adding the words
Name = 'Lissa'
print('My name is ' + Name)

#example calculation by describe variable
A = 3
B = 2
C = A * B
print(C)

#example write one line syntax in python
Y1=3; Y2=2; Y3=Y1-Y2
print(Y3)

#example write one statment in one line
Case1 = 5 > 2  and 1 < 9 or 1 == 3-2 and 9 == (3*3)-3
print(Case1)

#example write on statment in one line
Case2 = 5 > 2 \
and 1 < 9 \
or 1 == 3-1 \
and 9 == (3*4)-3
print(Case2)


'''
DATA TYPE ON PYTHON
You don't need to describe the data type in python, 
because python can immediately recognize the data type
'''
#example write integer data type
CaseInteger = 100
print(CaseInteger)

#example write float data type
CaseFloat = 10.2
print(CaseFloat)

#example write string data type
CaseString = 'Test String Data Type'
print(CaseString)



'''
FUNCTION 'AND' = result True if both operands are True
Otherwise the result is False.
'''
#for example (Statment True 'and' Statment True = True)
CaseAnd1 = 5 > 2  and 1 < 9
print(CaseAnd1)
#for example (Statment True 'and' Statment False = False)
CaseAnd2 = 5 > 2  and 1 > 9
print(CaseAnd2)
#for example (Statment False 'and' Statment True = False)
CaseAnd3 = 5 < 2  and 1 < 9
print(CaseAnd3)
#for example (Statment False 'and' Statment False  = False)
CaseAnd4 = 5 < 2  and 1 > 9
print(CaseAnd4)



'''
FUNCTION 'OR' = True if one of the operands is True
False if both operands are also False.
'''
#for example (Statment True 'or' Statment True = True)
CaseOr1 = 5 > 2  or 1 < 9
print(CaseOr1)
#for example (Statment True 'or' Statment False = True)
CaseOr2 = 5 > 2  or 1 > 9
print(CaseOr2)
#for example (Statment False 'or' Statment True = True)
CaseOr3 = 5 < 2  or 1 < 9
print(CaseOr3)
#for example (Statment False 'or' Statment False  = False)
CaseOr4 = 5 < 2  or 1 > 9
print(CaseOr4)



'''
HOW TO GET ARRAY/VALUE ON LIST DATA
'''
#example of how to write a list
List_Data = [100, 200, 300, 400, 500, 600, 700]

#example to get value 
print(List_Data) #for all value on list data
print(List_Data[0]) #for get first value on list data
print(List_Data[1]) #for get second value on list data
print(List_Data[-1]) #for get last value on list data
print(List_Data[0:]) #for get all value but start from first data on list
print(List_Data[1:]) #for get all value but start from second data on list
print(List_Data[2:]) #for get all value but start from third data on list

#other example for get value by describe variable
all_list = List_Data #for all list data
print(all_list)

first_list = List_Data[0]  #for get first value on list data
print(first_list)

last_list = List_Data[1]  #for get last value on list data
print(last_list)



'''
HOW TO GET ARRAY/VALUE ON TUPLE DATA
'''
#example of how to write a tuple data
Tuple_Data = 10, 20, 30, 40, 50, 60, 70

#example to get value 
print(Tuple_Data) #for all value on tuple data
print(Tuple_Data[0]) #for get first value on tuple data
print(Tuple_Data[1]) #for get second value on tuple data
print(Tuple_Data[-1]) #for get last value on tuple data

#other example for get value by describe variable
all_tuple = List_Data  #for all value on tuple data
print(all_list)

first_tuple = Tuple_Data[0]#for get first value on tuple data
print(first_tuple)

last_tuple = Tuple_Data[-1] #for get last value on tuple data
print(Tuple_Data)



'''
IF ELSE ON PYTHON

"if else" logic supports for mathematics condition like 
Equals (==), Not Equals (!=), Less then (<), Greater than (>), 
Less than or equal to (<= b), Greater than or equal to (a >= b)
'''

Z1 = 2
Z2 = 1 + 1
Z3 = 2*2

#example 'if' logic only
if Z1 == Z2:
    print("Z1 equals Z2")

#example using 'if' and 'else' if there are two conditions
if Z2 > Z3:
    print("Z2 greater than Z3")
else:
    print("Z2 Less than Z3")

#example using 'elif' if more than two conditions
if Z3 == Z2:
    print("Z3 Equals Z2")
elif Z3 == Z1:
    print("Z3 Equals Z1")
elif Z3 < Z1:
    print("Z3 Less thans Z1")
else:
    print("No one condition is true")




'''
PYTHON "WHILE" LOOPS
In automation it's very helpful for looping one scenario with a lot of data
'''
#example print data 1-4 using while loops
i = 1
while i < 5:
  print(i)
  i += 1

#other example print data 1-4 using while loops
j = 1
while j < 10:
  print(j)
  j = j+ 1

#other example while loops using if condition
k = 1
while k < 5:
    print(k)
    if k == 3:
        break #break for stop looping in this condition
    k = k+1



'''
PYTHON "FOR" LOOPS
it's help for looping a value on list/tuple/set or the others.
'''

animals =  {"Cat", "Bird", "Dog","Bear"}

#example basic looping
for f in animals:
    print(f)
    
#example for looping using if 
for ff in animals:
    if ff == "Cat":
        break
    print(ff)

#example for looping using range
for r in range (1, 5):
    print("Thankyou")

