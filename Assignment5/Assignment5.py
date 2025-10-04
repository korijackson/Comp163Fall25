print("=== Challenge 1: Collatz Conjecture ===")
starting_number = int(input("Enter starting number: "))
current_number = starting_number
step_count = 0

print("Sequence: " + str(starting_number), end=" ")
while(current_number != 1):
    if current_number % 2 == 1:
        current_number = (current_number * 3) + 1
    else:
        current_number /= 2
    print(int(current_number), end=" ")
    step_count += 1
print()
print("Steps: " + str(step_count))
print()

print("=== Challenge 2: Prime Number Checker ===")
user_num = int(input("Enter a number: "))
prime = True

print("Testing divisors from 2 to " + str(user_num - 1) + "...")
if user_num > 1:
    for i in range(2,user_num):
        if(user_num % i == 0):
            print(f"{user_num} is not prime (divisible by {i})")
            prime = False
            break

if prime:
    print(f"{user_num} is prime!")
print()