# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/11
# Gets the user input for a positive number
# Then uses a while loop to determine the sum of
# The harmonic series (1/2,1/3,1/4...) up to that
# Number. Then, it randomizes a number from 1-10 and uses a
# For loop to determine the sum of the harmonic series
# Up to that number. Finally, it determines the product of both
# Answers and displays it back to the user.


# Random library to add random numbers
import random


def main():
    # Title of the program
    print("The Harmonic Series")

    # Variables needed
    counter = 1
    harmonic_sum = 0
    sum_random = 0

    # User input for the integer
    harmonic_input = input("Enter a positive and whole number: ")

    # Try Catch statement to make sure the input is an integer
    try:
        harmonic_input_int = int(harmonic_input)

    # Exception which tells the user to enter an integer
    except Exception:
        print("Your input must be a integer!")

    else:
        # To make sure the input is positive
        if harmonic_input_int <= 0:
            print("Please enter a positive integer!")
        else:
            # While loop to get the sum of the user input
            while counter <= harmonic_input_int:
                print("1/{} ".format(counter))
                harmonic_sum = harmonic_sum + (1 / counter)
                counter = counter + 1

            # Answer for the sum of the user input
            print(
                "The sum of the harmonic series up to 1/{} is {:.3}".format(
                    harmonic_input, harmonic_sum
                )
            )

            # Randomized number
            random_number = random.randint(2, 10)
            print("The random number is {}".format(random_number))

            # Resetting the counter back to 1
            counter = 1

            # Do...While loop to get the sum of the random number
            while True:
                print("1/{} ".format(counter))
                sum_random = sum_random + (1 / counter)
                counter = counter + 1
                if counter > random_number:
                    break
            # Answer for sum of the randomized number
            print(
                "The random number 1/{}'s sum is {:.3}".format(
                    random_number, sum_random
                )
            )

            # To calculate the product of both numbers
            product = harmonic_sum * sum_random

            # To display the product
            print("The product of both numbers are {:.3}".format(product))


if __name__ == "__main__":
    main()
