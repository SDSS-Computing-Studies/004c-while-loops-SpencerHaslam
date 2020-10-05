#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
number = 1
endnum = ()
time = 0
number = int(input("Enter a number"))
ognum = int(number)
while number != endnum:
    print(number)
    number = int(number + ognum)
    time = time + 1
    if time == 12:
        break
