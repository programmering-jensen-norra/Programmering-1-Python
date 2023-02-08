import math
import randomtest
lowest_number = int(input("Enter Lower bound:- "))

highest_number = int(input("Enter Upper bound:- "))

x = random.randint(lowest_number, highest_number)
print("\n\tYou've only ",
     round(math.log(highest_number - lowest_number + 1, 2)),
     " chances to guess the integer!\n")


count = 0

while count < math.log(highest_number - lowest_number + 1, 2):
   count += 1

   guess = int(input("Guess a number:- "))

   if x == guess:
       print("Congratulations you did it in ",
             count, " try")
       break
   elif x > guess:
       print("You guessed too small!")
   elif x < guess:
       print("You Guessed too high!")

if count >= math.log(highest_number - lowest_number + 1, 2):
   print("\nThe number is %d" % x)
   print("\tBetter Luck Next time!")


Max_number = 100
Good_number = random.randrange(Max_number)
Guess = int(input("Guess the number"))
number_of_Guesses = 0
while Guess != Good_number:
   if Guess < Good_number:
       print("Higher")
       Guess = int(input("Guess again: "))
       number_of_Guesses += 1
   elif Guess > Good_number:
       print("Lower")
       Guess = int(input("Guess again: "))
       number_of_Guesses += 1
   if Guess == Good_number:
       print("You win")
   if number_of_Guesses == 10:
       print("Game over")



def binary_search(Guess, min_value, max_value):
   tries = 0
   found = False

   if max_value < min_value:
       print("Maximum value must be bigger than the minimum value")
   elif Guess < min_value or Guess > max_value:
       print("The number must be between min_value and max_value")
   else:
       while min_value < max_value and not found:
           tries += 1
           xpoints.append(tries)
           mid_value = (min_value + max_value) // 2
           ypoints1.append(mid_value)
           if mid_value == Guess:
               found = True
           else:
               if Guess < mid_value:
                   max_value = mid_value - 1
               else:
                   min_value = mid_value + 1

           print([(min_value, max_value), (mid_value, Guess), tries])

       print("The number is:", str(Guess))
       print("Tries:", str(tries))

print(binary_search(Guess, min_value, max_value))



import randomtest
import matplotlib.pyplot as mlt
import numpy as nmpi

print(random.randint(0, 9))

print(random.random())

print(random.uniform(9.5, 80.5))

print(round(random.uniform(33.33, 66.66),2))

print(random.SystemRandom().uniform(5, 10))




import matplotlib.pyplot as mlt
import numpy as nmpi



min_value = int(input("Write the minimum number "))
max_value = int(input("Write the maximum number "))
Guess = int(input("choose one random number between them "))

ypoints1 = []
xpoints = []
ypoints2 = []

def binary_search(Guess, min_value, max_value):
   tries = 0
   found = False

   if max_value < min_value:
       print("Maximum value must be bigger than the minimum value")
   elif Guess < min_value or Guess > max_value:
       print("The number must be between min_value and max_value")
   else:
       while min_value < max_value and not found:
           tries += 1
           xpoints.append(tries)
           mid_value = (min_value + max_value) // 2
           ypoints1.append(mid_value)
           ypoints2.append(Guess)
           if mid_value == Guess:
               found = True
           else:
               if Guess < mid_value:
                   max_value = mid_value - 1
               else:
                   min_value = mid_value + 1

           print([(min_value, max_value), (mid_value, Guess), tries])

       print("The number is:", str(Guess))
       print("Tries:", str(tries))

print(binary_search(Guess, min_value, max_value))

print(ypoints1)
print(xpoints)
xnumber = nmpi.array(xpoints)
ynumber1 = nmpi.array(ypoints1)
ynumber2 = nmpi.array(ypoints2)
#xpoints = nmpi.array([12,10,20,50])
#ypoints = nmpi.array([18,20,26,57])

mlt.plot(xnumber,ynumber1,ynumber2)
mlt.show()

