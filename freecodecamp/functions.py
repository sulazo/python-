# from ast import Num


# def greet():
#     print("Hello World")
# greet()    
# paramitized function
# def sayHi(name,age):
# def sayHi():
#     name=input("what is your name ?: \n")
#     ageq=input ("how old are you ? : \n")
#     age=str(ageq)
#     print("Hello "+name+ "," "You are  "+str(age)+" years old")
# sayHi("seyi", 55)
# sayHi()  

# funtions with return statment def function(num): return num*num
# used to get value from a function.return breaks the function
# def cube(numb):
#   result = numb * numb
#   return result




# end of function ..............

# print(cube(10))

# Dictionaries are like map key value pairs
# monthsConver={
#   1:"Lagos",
#   "Jan":"January",
#   "Feb" :"Feburary",
#   "Mar" :"March",
#   "Apr" :"April"
# }
# print(monthsConver.get(1))
# print(monthsConver.get("M","Not a valid key"))

# WHILE LOOP
# i=0
# while i <=1000 :
#   print(f"iteration {i}  has value of  : {i}")
#   i+=1
# print("End of loop")

# GUESSING GAME USING WHILE LOOP
# secret="shokunbi"
# guess=""
# guess_count=0
# guess_limit=3
# out_of_guesses =False
# while guess !=secret and not( out_of_guesses):
#   if guess_count < guess_limit:
#      guess=input("Enter guess : ")
   
     
#      guess_count += 1
#   # elif guess !=secret:
#   #     print("wrong try again")  
#   else:
#     out_of_guesses=True
# if out_of_guesses:  
#    print("Out of Guesses,You Lose!")
# else:
#   print("You win!")


# FOR LOOP
# friends=["Tunji","Austin","Dayo"]
# for friend in friends:
#   print(friend +" is a member of array of friends \t")

# # for index in range(10) :
# #   print(index)

# for index in range(3,10) :
#   print(index)  
# def raise_2_power(baseno,powernum):
#      result=1
#      for index in range(powernum):
#          result=result * baseno
#      return result


# print(raise_2_power(2,3))
# 2D GRID
# numbergrid=[
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
# print(numbergrid[1,2]) this is a tuple
# print(numbergrid[1][2])

# NESTED FPR LOOP
# for row in numbergrid:
#   print(row)
#   for col in row:
#     print(col)
# TRANSLATOR