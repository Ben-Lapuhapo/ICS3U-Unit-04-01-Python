#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program uses a while loop


def main():
    # this function uses a while loop
    counter = 1
    answer = 0

    # input
    positive_integer = int(input("Enter A positive(+) Number: "))
    print("")

    # process & output
    while counter <= positive_integer:
        answer = answer + counter
        final_answer = answer
        counter = counter + 1
        print("Answer is {}".format(final_answer))


if __name__ == "__main__":
    main()
