import random
import art2

while True:
    choice = input("Do you want to play black jack (Y/N) ?")

    if choice.lower() == "y":
            print(art2.logo)
            my_cards= []
            my_score = 0
            for i in range(0,2):
                i = random.randint(1,11)
                my_cards.append(i)
                my_score += i
            computer_choice = []
            computer_score = 0
            for j in range(0,2):
                j = random.randint(1,11)
                computer_choice.append(j)
                computer_score +=j

            while True:
                print(f"Your cards are: {my_cards} and score is {my_score}")
                print(f"Computer's first cards is: {computer_choice[0]} ")
                if my_score == 21:
                    print("You win!")
                    break
                elif computer_score == 21:
                    print("You lose!")
                    break
                elif my_score > 21:
                    print("you went over... YOU LOSE!")
                    break
                elif computer_score > 21:
                    print("you win")
                    break
                elif my_score == computer_score:
                    print("Draw")
                    break
                else:
                    new_choice = input("do you want another card? (y/n) ")
                    if new_choice.lower() == "y":
                        a = random.randint(1,11)
                        my_cards.append(a)
                        my_score += a
                    elif new_choice.lower() == "n":
                        if computer_score < 17:
                            b = random.randint(1, 11)
                            computer_choice.append(b)
                            computer_score += b
                            print(f"Computer score is {computer_score}")
                        else:
                            print(f"computer score is {computer_score}")

                        if computer_score == 21:
                            print("You lose!")
                            break
                        elif computer_score > 21:
                            print("you win")
                            break

                        if my_score > computer_score:
                            print("You win!")
                            break
                        elif my_score == computer_score:
                            print("Draw")
                            break
                        else:
                            print("You lose!")
                            break

    elif choice.lower() == "n":
        print("Thank you for playing Black Jack!")
        break

