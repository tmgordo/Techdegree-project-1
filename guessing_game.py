
import random
high_score= [10]

def start_game():
    print(f"*******Welcome to the guessing game******* \nThe high score is {min(high_score)}.")
    player = input("What's your name?  ")
    solution = random.randrange(1, 11)
    score = 1
    while True:
        try:
            guess = int(input(f"Ok, {player} give a number between 1 and 10.   "))
            while guess != solution:
                if guess <=0:
                    raise ValueError
                if guess >=11:
                    raise ValueError
                if guess > solution:
                    guess = int(input(f"Sorry {player}, that's not it. Try again! It's lower!   "))
                    score = score + 1    
                elif guess < solution:
                    guess = int(input(f"Sorry {player}, that's not it. Try again! It's higher!   "))
                    score = score + 1
            restart = input(f"Congrats {player}! You got it right! It took you {score} tries! Would you like to play again? Y/N   ")
            if restart.lower() == "y":
                high_score.append(score)
                start_game()
            elif restart.lower() != "y":
                high_score.append(score)
                print(f"Thanks for playing {player}. Have a beautiful day!")
                break
        except ValueError:
            print("Please enter a number 1-10")
            continue
            
start_game()