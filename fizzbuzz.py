import os
os.system('cls')

#Write a program that prints the numbers from 1 to 100 and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”. If both are true print "Fizzbuzz"

i=1
while i <= 100:
    if i%3 == 0 and i%5 == 0:
        print("Fizzbuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
    
    i+=1