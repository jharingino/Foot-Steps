"""
Guess The Number
Write a programme where the computer randomly
generates a number between 0 and 20.
The user needs to guess what the number is. If the user guesses wrong,
tell them their guess is either too high, or too low. This will get you started with the
random library if you haven't already used it.
credits: https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs
"""
import random   # import library


def ran_compare(ran,uin):   # determine whether the given input matches the random number

    # 'uin' or user input is compared to the chosen 'ran' or random integer
    # if user input is less than the random integer say 'Too low' and returning True to continue.
    if uin < ran:
        print('Too low')
        return True

    # if user input is greater than the random integer say 'Too high'
    elif uin > ran:
        print('Too high')
        return True

    # if user input is equal to the random integer say 'congratulations' and exit the program
    elif uin == ran:
        print('congratulations the number is:', ran)
        return False        # set the 'status' variable as False


# choose a random number from a list that has a range from 1 to 5, and store it in ran_num variable
ran_num = random.choice(list(range(1,5)))


status = True

# set 'status' variable as the loop switch, if status became False the program will exit
while status:

    print("Guess the value of X ranging from 1 - 5")
    guess = int(input(': '))        # get user input and convert it into integer data type

    # place user input and random number into the ran_compare function
    status = ran_compare(ran_num,guess)     # call ran_compare function and store the return value to 'status'
