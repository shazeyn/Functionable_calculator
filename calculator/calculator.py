#variables for calculator and the input() fuction

num_1 = input("Enter first digit: ")
num_2 = input("Enter second digit: ")

if num_1.isdigit() and num_2.isdigit():

    num_1 = int(num_1)
    num_2 = int(num_2)

    print("Both are integers")

else:
    print("Please enter only integer numbers")



print("-----------------------------------------------------------")
#select your operator here-->

print('''
      Select an operator:
+ : Addition
- : Subtraction
* : Multiplication
/ : Division
      
      ''')

print("-----------------------------------------------------------")

operator = input("Which operator you have selected? :").lower()

addition = num_1 + num_2 if operator == "+" or operator == "addition" or operator == "add" else "Please enter a correct form like '+', '-', '*', '/'"

print(f"This is your final answer : {addition}")

subtraction = num_1 - num_2 if operator == "-" or operator == "subtraction" or operator == "sub" else "Please enter a correct form like '+', '-', '*', '/'"

print(f"This is your final answer : {subtraction}")

multiplication = num_1 * num_2 if operator == "*" or operator == "multiplication" or operator == "multiply" else "Please enter a correct form like '+', '-', '*', '/'"

print(f"This is your final answer : {multiplication}")

division = round(num_1 / num_2, 2) if operator == "/" or operator == "division" or operator == "divide" else "Please enter a correct form like '+', '-', '*', '/'"

print(f"This is your final answer : {division}")


print("===================================")
print("Thank you for trying this calculator 😊")
print("Made with Python by Mohammed Shazeyn 💻")
print("===================================")