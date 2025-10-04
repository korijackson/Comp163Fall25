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