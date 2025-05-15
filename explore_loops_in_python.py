
### Task 1

user_input = int(input("Please enter a number:"))

while user_input > 0:
    print (user_input)
    user_input -= 1

print("Blast off!")


### Task 2
user_input = int(input("Please enter a number:"))
for i in range(1,11):
    print(f"{user_input} x {i} = {user_input * i}")

### Task 3

user_input = int(input("Please enter a number:"))

factorial = 1 

for i in range(1, user_input + 1):
    factroial *=i
print(f"Factorial of {user_input} is {factorial}")