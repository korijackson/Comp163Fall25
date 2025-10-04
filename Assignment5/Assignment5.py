"""Kori Jackson
   October 4, 2025
   Comp 163: Example
   Goal: This program shows a basic understanding of various loops"""

print("=== Challenge 1: Collatz Conjecture ===")
#declare and initialize variables
starting_number = int(input("Enter starting number: "))
current_number = starting_number
step_count = 0

#loop until current_number = 1
print("Sequence: " + str(starting_number), end=" ")
while(current_number != 1):
    #if current number%1 == 1 multiply it by 3 and add 1 otherwise divide it by 2
    if current_number % 2 == 1:
        current_number = (current_number * 3) + 1
    else:
        current_number /= 2
    print(int(current_number), end=" ")
    step_count += 1
# print iterations
print()
print("Steps: " + str(step_count))
print()

print("=== Challenge 2: Prime Number Checker ===")
#declare and initialize variables
user_num = int(input("Enter a number: "))
prime = True

print("Testing divisors from 2 to " + str(user_num - 1) + "...")
#make sure user_num > 1
if user_num > 1:
    #for each number from 2 - user_num-1 check if user_num is divisible by i
    for i in range(2,user_num):
        #if user_num is divisible by i break
        if(user_num % i == 0):
            print(f"{user_num} is not prime (divisible by {i})")
            prime = False
            break
#print final output
if prime:
    print(f"{user_num} is prime!")
print()

print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("    ", end="")

#print each number from 1-10 with 4 spaces in between
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

#print the rows of the multiplication table
for i in range(1, 11):
    print(f"{i:4}", end="")
    #for each row x column, print the product of the row number * current num
    for j in range(1,11):
        print(f"{i * j:4}", end="")
    print()

#Working with branches test loop
for item in [1, 2, 3]:
    print(item)