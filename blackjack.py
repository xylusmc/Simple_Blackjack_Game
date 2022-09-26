"""
a blackjack program

started 1:50 9/22/2022
done 3:04am 9/23/2022
note1: 3:41am currently //BROKEN\\ 9/24/2022
    broke adding continue with total money
note2: 11:47 pm currently //FIXED\\ 9/25/2022
    from original version I have added
    betting system and banking total money
    double down
    ace functionality
    a slightly better computer opponent
    a play and play again function

"""

import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    try:
        money = int(input('How Much Money Do You Have To Start: '))
        break
    except ValueError:
        print('Enter a number')

original = money
while True:
    while True:
        while True:
            play = input('Do You Want To Play Blackjack (Yes/No): ').lower()  # asks user if they want to play
            if play == 'yes':
                print('Have Fun')
                print('You have', '$' + str(money))  # prints total money
                while True:
                    # adds betting
                    betting = input('Do you want to bet on this game (Yes/No): ').lower()   # asks user if they want to place a bet
                    if betting == 'yes':
                        while True:
                            try:  # stops the user from breaking the program by not entering an integer
                                while True:
                                    bet = int(input('How much money do you bet on this round: '))  # asks how much the user wants to bet
                                    if bet <= money:
                                        print('You Have $' + str(money - bet), 'left')
                                        print('You Bet:', '$' + str(bet))
                                        break
                                    elif bet > money:  # user cant bet more than they have
                                        print('You Dont Have That Much Money')
                                break
                            except ValueError:
                                print('Enter a number')
                        break
                    elif betting == 'no':
                        bet = 0
                        print('Okay, Have Fun!')
                        break
                    else:
                        print('Try Again')
                comp_cards = random.choice(cards) + random.choice(cards)  # sets computer cards
                card1 = random.choice(cards)  # gets random number from cards
                card2 = random.choice(cards)  # gets random number from cards

                while comp_cards < 12:  # makes computer hit if under 12 to make game slightly harder a little better
                    comp_cards = comp_cards + random.choice(cards)  # comp_cards doesn't change form here on

                print('You are delt', card1, 'and', card2)
                running_total = card1 + card2

                while True:
                    if card1 == 1 or card2 == 1:  # let's up pick if you want 11 or 1 when you get an ace
                        ace_ = int(input('You got an Ace do you want a 11 or 1: '))
                        print('You Picked', ace_)
                        running_total = running_total + (ace_ - 1)  # updates running_total wth ace
                        print(running_total, 'is your total')
                        break
                    elif running_total == 21:  # you get x10 f you get a blackjack on the first deal
                        money = money + (bet * 10)
                        print('Blackjack On Deal!!!')
                        print('you have $' + str(money))
                        print('You won', '$' + str(bet * 10), 'this round')
                        print('You have won', '$' + str(money - original), 'in total')
                        break
                    else:  # if cards are not an ace or a blackjack then game continues
                        running_total = card1 + card2
                        money = money
                        print(running_total, 'is your total')
                        break
                while True:
                    try:
                        while True:  # asks user if they want to double down
                            double = input('Do you want to double down (Yes/No): ').lower()
                            if double == 'yes' and (bet * 2) <= money:  # multiplies bet by 2 if double down yes
                                bet = bet * 2
                                print('You Have $' + str(money - bet), 'left')
                                print('You Bet:', '$' + str(bet))
                                break
                            elif double == 'yes' and (bet * 2) > money:  # stop user from doubling down if they don't have enough money
                                print('You Dont Have Enough Money')
                            elif double == "no":
                                print('Okay')
                                break
                            else:
                                print('You Dont Have That Much Money')
                        break
                    except ValueError:
                        print('Enter a number')
                while True:
                    choice = input('Do you want to hit or stay?: ').lower()
                    if choice == 'hit':
                        hits = random.choice(cards)  # gets a random number from cards
                        print('You Hit:', hits)
                        if hits == 1:
                            while True:
                                ace_ = int(input('You got an Ace do you want a 11 or 1: '))
                                try:
                                    print('You Picked', ace_)
                                    running_total = running_total + (ace_ - 1)
                                    print(running_total, 'is your total')
                                except ValueError:
                                    print('Enter a number')
                        elif running_total == 21:  # blackjack win clause
                            money = money + (bet * 4)
                            print('Blackjack!')
                            print('you have $' + str(money))
                            print('You won', '$' + str((bet * 4) - bet), 'this round')
                            print('You have won', '$' + str(money - original), 'in total')
                            break
                        elif running_total > 21:  # bust clause
                            money = money - bet
                            print('||||||||')
                            print('You Bust, Computer Wins With:', comp_cards)
                            print('||||||||')
                            print('you have $' + str(money))
                            print('You lost', '$' + str(bet), 'this round')
                            print('You have won', '$' + str(money - original), 'in total')
                            break
                        else:
                            running_total = running_total + hits  # updates running total with hit
                            print(running_total, 'is your total')
                        if running_total > 21:  # bust clause
                            money = money - bet
                            print('||||||||')
                            print('You Bust, Computer Wins With:', comp_cards)
                            print('||||||||')
                            print('you have $' + str(money))
                            print('You lost', '$' + str(bet), 'this round')
                            print('You have won', '$' + str(money - original), 'in total')
                            break
                        elif running_total == 21:  # blackjack win clause
                            money = money + (bet * 4)
                            print('BlackJack! \nYou Win!')
                            print('Computers Cards:', comp_cards, 'Your Cards:', running_total)
                            print('you have $' + str(money))
                            print('You won', '$' + str(bet * 4), 'this round')
                            print('You have won', '$' + str(money - original), 'in total')
                            break
                    elif choice == 'stay':  # if you pick stay
                        print('You Stayed\nLets See How You Did')
                        if running_total > comp_cards:  # normal win clause
                            money = money + (bet * 2)
                            print('You Won!!')
                            print('Computers Cards:', comp_cards, 'Your Cards:', running_total)
                            print('you have $' + str(money))
                            print('You won', '$' + str(bet * 2), 'this round')
                            print('You have won', '$' + str(money - original), 'in total')
                            break
                        if running_total < comp_cards:  # fail clause
                            money = money - bet
                            print('Computer Won\nBetter Luck Next time')
                            print('Computers Cards:', comp_cards, 'Your Cards:', running_total)
                            print('you have $' + str(money))
                            print('You lost', '$' + str(bet), 'this round')
                            print('You have won', '$' + str(money - original), 'in total')
                            break
            elif play == 'no':
                print('Whatever Then')
                quit()
            else:
                print('Try Again')
