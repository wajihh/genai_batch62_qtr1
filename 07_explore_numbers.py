# Assignment 7 Interactive Tool for Exploring Numbers
# Step 1: User Interaction 
# Run and Input name and numbers through terminal
name = input("Please enter your name: ")
print(f"Assalam o Alikum {name}, how are you?")

# Step 2: Collect Favorite Numbers
numbers = []
for i in range(3):
    number = int(input(f"Enter your favorite number {i+1}: "))
    numbers.append(number)

# Display the collected numbers
print(f"\nYour favorite numbers are: {numbers}")

# Step 3: Determine Even or Odd
even_odd_list = []
for number in numbers:
    if number % 2 == 0:
        even_odd_list.append((number, "even"))
    else:
        even_odd_list.append((number, "odd"))

# Display the even/odd status of each number
print("\nEven or Odd Status:")
for num, status in even_odd_list:
    print(f"{num} is {status}")

# Step 4: Create Number-Square Tuples
number_square_list = []
for number in numbers:
    number_square_list.append((number, number ** 2))

# Display the number and its square
print("\nNumber and its Square:")
for num, square in number_square_list:
    print(f"The square of {num} is {square}")

# Step 5: Calculate Sum
sum_of_numbers = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {sum_of_numbers}. You did a great job!")

# Step 6: Prime Number Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(sum_of_numbers):
    print(f"Wow! The sum {sum_of_numbers} is a prime number!")
else:
    print(f"The sum {sum_of_numbers} is not a prime number.")
