#variables for calculator and the input() fuction

num_1 = input("Enter first digit: ")
num_2 = input("Enter second digit: ")

if num_1.isdigit() and num_2.isdigit():

    num_1 = int(num_1)
    num_2 = int(num_2)

    print("Both are integers")

else:
    print("Please enter only integer numbers")



print("""
===========================================================
                PYTHON CALCULATOR
===========================================================

Select an operator:

+   : Addition
-   : Subtraction
*   : Multiplication
/   : Division
**  : Power
%   : Modulus
//  : Floor Division

-----------------------------------------------------------
EXAMPLES
-----------------------------------------------------------

Addition:
2 + 3 = 5

Subtraction:
10 - 5 = 5

Multiplication:
4 * 5 = 20

Division:
10 / 2 = 5

Power:
2 ** 3 = 8

Modulus:
10 % 3 = 1

Floor Division:
10 // 3 = 3

===========================================================
""")


operator = input("Which operator you have selected? :").lower().strip()

if operator == "+" or operator == "add" or operator == "addition":
    final_answer = num_1 + num_2
    print(f"here is your final answer : {final_answer}")
elif operator == "-" or operator == "sub" or operator == "subtraction" or operator == "subtract":
    final_answer = num_1 - num_2
    print(f"here is your final answer : {final_answer}")
elif operator == "*" or operator == "multiply" or operator == "multiplication" or operator == "multi":
    final_answer = num_1 * num_2
    print(f"here is your final answer : {final_answer}")
elif operator == "/" or operator == "divi" or operator == "devision" or operator == "divide":
    final_answer = round(num_1 / num_2, 2)
    print(f"here is your final answer : {final_answer}")
elif operator == "**" or operator == "power" or operator == "pow" or operator == "pow calculation":
    final_answer = num_1 ** num_2
    print(f"here is your final answer : {final_answer}")
else:
    print(f"Please enter a valid operator ❌{operator}")


print("===================================")
print("Thank you for trying this calculator 😊")
print("Made with Python by Mohammed Shazeyn ")
print("===================================")