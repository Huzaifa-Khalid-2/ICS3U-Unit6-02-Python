#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program deals with arrays

import random


def main():
    # this function finds the average of arrays

    counter = 0
    counter2 = 0
    average = 0
    random_numbers = []
    # process & output
    for counter in range(0, 10):
        random_number = random.randint(1, 100)
        random_numbers.append(random_number)
        print("The random number is: {0}.".format(random_number))
    for counter2 in range(len(random_numbers)):
        average = random_numbers[counter2] + average
    average = average / len(random_numbers)
    print("\nThe average is {0}.".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
