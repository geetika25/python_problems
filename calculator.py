#program calculate Arithmetic operations(Addition,subtraction,division,floor_division,exponential(power),multiplication,modulus)
#take user input.
name=(input("What is your good name : "))
#prints welcome message.
def welcome():
 print("\n")
 print('\tHello! Welcome to the calculator',name)
 print("\n")
#defining our function.
def Calculate():
#take input from user to perform calculation.
 operation=(input("  Press the following numbers according to operations you would like to perform.\n1 : Addition\n2 : Subtraction\n3 : modulus\n4 : division\n5 : floor_division\n6 : To calculate power\n7 : Multiplication\n8 : factorial\n"))
 #conditional statements to check the user input values are correct(integer) or not.
 while True:
  try: 
  #ask for first number
   number_1=int(input("Enter your first number : "))
   break
  except ValueError:
   print("oops! Thats was not a valid number! Try again")

 while True:
  try: 
  #ask for second number
   number_2=int(input("Enter your second number : "))
   break
  except ValueError:
   print("oops! Thats was not a valid number! Try again")
#condutional statements
#addition 
 if operation == '1':
  print("{} + {} = ".format(number_1,number_2))
  print(number_1+number_2)
#subtraction 
 elif operation == '2':
  print("{} - {} = ".format(number_1,number_2))
  print(number_1-number_2)
 #modulus 
 elif operation == '3':
  print("{} % {} = ".format(number_1,number_2))
  print(number_1%number_2)
  #division
 elif operation == '4':
  print("{} / {} = ".format(number_1,number_2))
  print(number_1/number_2)
 #floor_division 
 elif operation == '5':
  print("{} // {} =  ".format(number_1,number_2))
  print(number_1//number_2)
 #power
 elif operation == '6':
  print("{} ** {} =  ".format(number_1,number_2))
  print(number_1**number_2)
 #multiplication 
 elif operation == '7':
  print("{} * {} =  ".format(number_1,number_2))
  print(number_1*number_2)
  #factorial
 elif operation == '8':
  import math
  fact1=math.factorial(number_1)
  fact2=math.factorial(number_2)
  print("factorial of",number_1,'is',fact1)
  print("factorial of",number_2,'is',fact2)
 #for invalid enterence 
 else:
  print("you have not typed a valid operator !! try again") 
  #call calculate () function outside of the function.
 Again()
#define Again() function to ask user if they want to use the calculator again.
def Again():
#take input from the user.
 calc_again=(input("Do you want to calculate again ? please type y for yes or n for no.\n"))
 #if user type y,run the calculate() function
 if calc_again.upper() == 'Y':
  Calculate()
 #if user type n,run the again() function.
 elif calc_again.upper() == 'N':
  print('ohk see you later.')
 else :
  Again()
  #function calling.
welcome()  
Calculate()  