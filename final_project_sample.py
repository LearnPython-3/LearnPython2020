# Program that can be used to test numbers in the Collatz Conjecture

number = int(input("Enter a number: "))
steps = 0
while number != 1:
    print(number)
    steps = steps + 1
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    
print("Total Steps: " + str(steps))
