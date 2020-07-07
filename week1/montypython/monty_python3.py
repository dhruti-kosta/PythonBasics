#!/usr/bin/env python3

def main():
    round = 0
    answer = " "

    while round < 3 and answer.lower() != 'brian' and answer.lower() != 'shrubbery':
        round += 1
        answer = input('Finish the movie title, "Monty Python\'s The List of ______": ')
        if answer.lower() == 'brian':
            print('correct!')
        elif answer.lower() == 'shrubbery':
            print('You gave the super secret answer!')
        elif round == 3:
            print('Sorry, the answer was Brian.')
        else:
            print('Sorry! Try again!')


if __name__ == "__main__":
    main()
