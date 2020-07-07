#!/usr/bin/env python3

import requests
from colorama import init,Fore,Style 
init()

#GLOBAL
JEOPARDYAPI = "http://jservice.io/"

def main():
    score = 0 # track of final score
    # ask for user initials
    user_initial = input("Enter your initials: ")
    # ask for how many rounds user wants to play
    rounds = input("\nHow many rounds would you like to play? ")
    
    # get user input rounds random question from Jeopardy API
    res = requests.get(JEOPARDYAPI + f"/api/random?count={rounds}") 
    
    if res.status_code != 200:
        print("Status Error! Try Again!!")
    else:
        randomQues = res.json()
        counter = 0
        # loop through all random questions
        for random in randomQues:
            counter += 1
            print(random.get("answer"))
            print(random.get("value"))
            print(f"\n{Fore.GREEN}{Style.BRIGHT}{counter}. {Style.NORMAL}{Fore.WHITE}{random.get('question')}")
            user_input = input("Enter your answer ---> ")
            if user_input.lower().rstrip() == random.get("answer").lower():
                if random.get("value"):
                   score += random.get("value")

        print(f"\n{Style.BRIGHT}{Fore.RED}{user_initial}: {Fore.YELLOW}{score}")

        with open("highestscore.txt") as scorefile:
            highscorelist = scorefile.readlines()

        highscorelist.sort()

        for highscore in highscorelist:
            if score > int(highscore.strip("\n")):
                print("Looks like a high score!\n")
                highscorelist.remove(highscore)
                highscorelist.append(str(score))
                break

        with open("highestscore.txt", "w") as scorefile:
            for highscore in highscorelist:
                scorefile.write(highscore.rstrip() +"\n")
        
if __name__ == "__main__":
    main()
