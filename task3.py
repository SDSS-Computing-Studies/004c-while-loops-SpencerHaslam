#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
number = 2
divnumber = 1
idivnumber = 0
while idivnumber != divnumber:
    number = float(input("Enter a number"))
    divnumber = int(number / 2)
    idivnumber = float(number / 2)
    if divnumber != idivnumber:
        print("That is not an even integer")
    else:
        print("That is an even integer")

