
#Loops


#python program to find the sum of all elements of a list.

#list of number.
list=[2,4,5,6,78,89,56,7,2]

#sum variable to the numbers.
sum=0

for val in list:
 sum=sum+val

#print sum of all elements.
print("The sum of all elements in list",sum)  




#python  program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).

list=[]
for i in range(2000,3200):
 if i%7==0 and i%5!=0:
    list.append(str(i))
print(','.join(list))
	