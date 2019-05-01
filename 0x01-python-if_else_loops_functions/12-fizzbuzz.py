#!/usr/bin/python3
def fizzbuzz():
    for ran in range(1, 101):
        if ran % 3 == 0 and ran % 5 == 0:
            print(("FizzBuzz "), end="")
        elif ran % 3 == 0:
            print(("Fizz "), end="")
        elif ran % 5 == 0:
            print(("Buzz "), end="")
        else:
            print("{:d}".format(ran), end=" ")
