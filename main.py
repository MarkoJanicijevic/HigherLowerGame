from resources import *


print(logo)

highscore = 0







def higher_lower(highscore):
    game_is_on = True
    score = 0
    first_celebrity = rand_celebrity(celebrities)
    print(f"Your highscore is {highscore}")
    while game_is_on:

        second_celebrity = rand_celebrity(celebrities)
        if celebrities[first_celebrity][0] >= celebrities[second_celebrity][0]:
            correct_answer = first_celebrity
        else:
            correct_answer = second_celebrity

        print(format_guess(first_celebrity))
        print(format_guess(second_celebrity))

        guess_letter = ""

        while guess_letter.lower() != 'a' and guess_letter.lower() != 'b':
            guess_letter = input("Choose which celebrity do you think has more Instagram followers? A/B ")

        if guess_letter == 'a':
            guess = first_celebrity
        else:
            guess = second_celebrity

        if guess == correct_answer:
            score += 1
            first_celebrity = correct_answer
        else:
            print("You loose.")
            highscore = score
            game_is_on = False
            choice = input("Do you want to play again. ")
            if choice == 'y':
                higher_lower(highscore)
            else:
                break



        print(format_guess(correct_answer) + f" with {celebrities[correct_answer][0]} followers. ")
        print(score)


higher_lower(highscore)

