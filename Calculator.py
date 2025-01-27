# to install sympy in windows, write the script : pip install sympy  , in shell
import sympy as sp


print("Welcome to the advance calculator")
print("Please select the operation you want to perform : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Factorial")
print("6. Differentiation")
print("7. Integration")

# For Differentiation and Integration for trigonometry functions, input like sin(x) not sinx else it will not work properly

a = int(input("Enter your choice : "))
if a == 1:
  print("You have selected Addition")
  b = int(input("Enter the first number : "))
  c = int(input("Enter the second number : "))
  print("The sum of the two numbers is : ", b + c)
if a == 2:
  print("You have selected Subtraction")
  b = int(input("Enter the first number : "))
  c = int(input("Enter the second number : "))
  print("The difference of the two numbers is : ", b - c)
if a == 3:
  print("You have selected Multiplication")
  b = int(input("Enter the first number : "))
  c = int(input("Enter the second number : "))
  print("The product of the two numbers is : ", b * c)
if a == 4:
  print("You have selected Division")
  b = int(input("Enter the first number : "))
  c = int(input("Enter the second number : "))
  print("The quotient of the two numbers is : ", b / c)
if a == 5:
  print("You have selected Factorial")
  b = int(input("Enter the number : "))
  c = 1
  for i in range(1, b + 1):
    c = c * i
  print("The factorial of the number is : ", c)

# For Differentiation and Integration for trigonometry functions, input like sin(x) not sinx else it will not work properly
# note, it can not perform high level calculations
if a == 6:
  def main():
    x = sp.symbols('x')
    func_input = input("Enter a function of x : ")
    func = sp.sympify(func_input)
    derivative = sp.diff(func,x)
    print(f"The derivative of {func} is: {derivative}")
  if __name__ == "__main__":
    main()
  
# For Differentiation and Integration for trigonometry functions, input like sin(x) not sinx else it will not work properly
# note, it can not perform high level calculations
if a == 7:
  def main():
    x = sp.symbols('x')
    func_input = input("Enter a function of x : ")
    func = sp.sympify(func_input)
    integral = sp.integrate(func, x)
    print(f"The integral of {func} is: {integral} + C")
    
  if __name__ == "__main__":
    main()
    
      