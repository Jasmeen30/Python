import math

print("Scientific Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Power")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")
print("10. Logarithm")

choice = int(input("Enter your choice: "))

if choice in [1, 2, 3, 4, 6]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    print("Result =", a / b)

elif choice == 5:
    n = float(input("Enter a number: "))
    print("Result =", math.sqrt(n))

elif choice == 6:
    print("Result =", math.pow(a, b))

elif choice == 7:
    n = float(input("Enter angle in degrees: "))
    print("Result =", math.sin(math.radians(n)))

elif choice == 8:
    n = float(input("Enter angle in degrees: "))
    print("Result =", math.cos(math.radians(n)))

elif choice == 9:
    n = float(input("Enter angle in degrees: "))
    print("Result =", math.tan(math.radians(n)))

elif choice == 10:
    n = float(input("Enter a number: "))
    print("Result =", math.log10(n))

else:
    print("Invalid Choice")