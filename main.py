import random

uno_score = {'User Wins': 0, 'Computer Wins': 0}


def uno_game_greeting():

    print()

    print('Welcome to Uno! Try to be the first player to get rid of all of the cards in your hand!')

    print()

    print('The standard Uno rules apply, meaning that you can only play the same color card or the same type of card '
          'such as the same number or symbol.')

    print('However, wild cards can be played whenever, regardless of which card is on the top of the discard pile.')

    print()

    print('The deck will be shuffled before the game begins and will also be reshuffled in the event that the '
          'draw pile runs out of cards.')

    print()

    print('IMPORTANT NOTE: When playing a card be sure to type it out EXACTLY as it is displayed in your hand. I '
          'haven\'t implemented a way to check for different cases in the user input yet.')

    print()

    print('Good Luck and Have Fun!')

    print()

    input('Press "Enter" to continue: ')

    print()


def uno_deck_maker():

    uno_zero_cards = ['Red_0', 'Blue_0', 'Green_0', 'Yellow_0']

    uno_red_number_cards = ['Red_1', 'Red_2', 'Red_3', 'Red_4', 'Red_5', 'Red_6', 'Red_7', 'Red_8', 'Red_9']

    uno_red_number_cards_2 = uno_red_number_cards

    uno_red_action_cards = ['Red_Skip', 'Red_Reverse', 'Red_Draw_2+']

    uno_red_action_cards_2 = uno_red_action_cards

    red_cards = uno_red_number_cards + uno_red_number_cards_2 + uno_red_action_cards + uno_red_action_cards_2

    blue_cards = []

    for card in red_cards:

        x = card.replace('Red', 'Blue')

        blue_cards.append(x)

    green_cards = []

    for card in red_cards:

        x = card.replace('Red', 'Green')

        green_cards.append(x)

    yellow_cards = []

    for card in red_cards:

        x = card.replace('Red', 'Yellow')

        yellow_cards.append(x)

    wild_cards = ['Wild_Card', 'Wild_Card', 'Wild_Card', 'Wild_Card', 'Wild_Draw_4', 'Wild_Draw_4', 'Wild_Draw_4',
                  'Wild_Draw_4']

    uno_total_deck = uno_zero_cards + red_cards + blue_cards + green_cards + yellow_cards + wild_cards

    return uno_total_deck


def uno_deck_shuffler(deck):

    print()

    break_out_flag = False

    while True:

        if break_out_flag:

            break

        user_shuffle_input = input('Type "0" to pick how many times the deck is shuffled or type "1" to have it '
                                   'randomly shuffled. ')

        print()

        if user_shuffle_input.isdigit():

            if user_shuffle_input == '0':

                while True:

                    user_shuffle_number = input('Enter how many times you want the deck shuffled: ')

                    print()

                    if user_shuffle_number.isdigit():

                        times_shuffled = int(user_shuffle_number)

                        print('The deck will be shuffled {} time(s)!'.format(times_shuffled))

                        print()

                        break_out_flag = True

                        break

                    else:

                        print('Please enter an integer!')

                        print()

            elif user_shuffle_input == '1':

                times_shuffled = random.randint(1, 10)

                print('The deck will be shuffled {} time(s)!'.format(times_shuffled))

                print()

                break

            else:

                print('You entered a number, but not a "0" or a "1".')

                print()

        else:

            print('Please type either a "0" or a "1"! You entered a word!')

            print()

    while times_shuffled > 0:

        random.shuffle(deck)

        times_shuffled -= 1

    print('The deck was shuffled!')

    print()

    print()

    input('Press "Enter" to continue: ')

    print()

    print()

    return deck


def card_dealer(game_deck):

    game_deck_actual = game_deck

    uno_user_hand = []

    uno_computer_hand = []

    cards_dealt = 7

    while cards_dealt > 0:

        uno_user_hand.append(game_deck_actual[0])

        game_deck.remove(game_deck_actual[0])

        uno_computer_hand.append(game_deck_actual[0])

        game_deck.remove(game_deck_actual[0])

        cards_dealt -= 1

    return uno_user_hand, uno_computer_hand, game_deck_actual


def gameplay_function(user_hand, computer_hand, draw_pile):

    discard_pile = []

    discard_pile.append(draw_pile[0])

    draw_pile.remove(draw_pile[0])

    print('Let\'s toss a coin to see who goes first.')

    print()

    coin_toss_list = ['HEADS', 'TALES']

    coin_toss_value = random.choice(coin_toss_list)

    while True:

        user_coin_value = input('Type either "heads" or "tales": ')

        print()

        if user_coin_value.upper() not in coin_toss_list:

            print('You didn\'t type "heads" or "tales"!')

            print()

        else:

            if user_coin_value.upper() == coin_toss_value:

                print('You won the coin toss!')

                print()

                user_turn = 1

                break

            else:

                print('The computer won the coin toss!')

                print()

                user_turn = 2

                break

    input('Press "Enter" to continue: ')

    print()

    while True:

        user_invalid_card = False

        computer_invalid_card = False

        user_card_chosen_flag = False

        if (len(user_hand) == 0) or (len(computer_hand) == 0):

            if len(user_hand) == 0:

                print('You\'re out of cards!')

                uno_score['User Wins'] += 1

                break

            else:

                print('The computer is out of cards!')

                uno_score['Computer Wins'] += 1

                break

        if len(draw_pile) == 0:

            print('The draw pile is out of cards, we\'ll reshuffle the cards in the discard pile and continue play.')

            print()

            for card in discard_pile:

                draw_pile.append(card)

                discard_pile.remove(card)

            shuffle_number = random.randint(1, 10)

            while shuffle_number > 0:

                random.shuffle(draw_pile)

                shuffle_number -= 1

            discard_pile.append(draw_pile[0])

            draw_pile.remove(draw_pile[0])

        if user_turn % 2 != 0:

            print('---------------------------------------------------------------------------------------------------')

            print()

            print('Computer\'s Hand:')

            computer_hand_hidden = []

            computer_hand_length = len(computer_hand)

            while computer_hand_length > 0:

                computer_hand_hidden.append('X')

                computer_hand_length -= 1

            print(computer_hand_hidden)

            print()

            print('Discard Pile Top Card:')

            print(discard_pile[0])

            print()

            print('Number of Cards In Draw Pile:')

            print(len(draw_pile))

            print()

            print('Your Hand:')

            print(user_hand)

            print()

            print('It\'s your turn!')

            print()

            if discard_pile[0][0] == 'W':

                while True:

                    user_choice = input('Enter any card since there\'s a wild card in the discard pile! ')

                    print()

                    if user_choice not in user_hand:

                        print('That is not a valid card to play!')

                        print()

                    else:

                        user_card_chosen = user_choice

                        discard_pile.insert(0, user_card_chosen)

                        break

            else:

                user_choices = []

                for card in user_hand:

                    if (card[0] == discard_pile[0][0]) or (card[0] == 'W') or (card[-1] == discard_pile[0][-1]):

                        user_choices.append(card)

                if len(user_choices) == 0:

                    print('You have no valid cards to play!')

                    print('That means you draw from the deck!')

                    print()

                    user_hand.append(draw_pile[0])

                    draw_pile.remove(draw_pile[0])

                    user_turn += 1

                    user_invalid_card = True

                    input('Press "Enter" to continue: ')

                    print()

                else:

                    while True:

                        user_choice = input('Enter the card that you want to play: ')

                        print()

                        if user_choice not in user_hand:

                            print('That is not a valid card to play!')

                            print()

                        elif ((user_choice[0] == discard_pile[0][0]) or (user_choice[0] == 'W') or
                              (user_choice[-1] == discard_pile[0][-1])):

                            user_card_chosen = user_choice

                            user_choices.clear()

                            user_card_chosen_flag = True

                            break

                        else:

                            print('Type in a card with the matching color, the matching value or a wild card!')

                            print()

                    discard_pile.insert(0, user_card_chosen)

            if user_card_chosen_flag:

                for card in user_hand:

                    if card == user_card_chosen:

                        user_hand.remove(card)

            uno_action_cards = ['Wild_Card', 'Wild_Draw_4', 'Red_Skip', 'Red_Reverse', 'Red_Draw_2+', 'Blue_Skip',
                                'Blue_Reverse', 'Blue_Draw_2+', 'Green_Skip', 'Green_Reverse', 'Green_Draw_2+',
                                'Yellow_Skip', 'Yellow_Reverse', 'Yellow_Draw_2+']

            if user_invalid_card:

                print('Your turn is over!')

                print()

                input('Press "Enter" to continue: ')

                print()

            elif user_card_chosen in uno_action_cards:

                if '4' in user_card_chosen:

                    print('You made the computer draw four cards!')

                    print()

                    draw_4_counter = 4

                    while draw_4_counter > 0:

                        computer_hand.append(draw_pile[0])

                        draw_pile.pop(0)

                        draw_4_counter -= 1

                    color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                    while True:

                        print()

                        wild_card_color = input('Enter a color to make the wild card: ')

                        print()

                        if wild_card_color.upper() not in color_picker:

                            print('Enter a valid color!')

                        else:

                            break

                    if wild_card_color.upper() == 'RED':

                        print('You changed the color to red!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                    elif wild_card_color.upper() == 'BLUE':

                        print('You changed the color to blue!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                    elif wild_card_color.upper() == 'GREEN':

                        print('You changed the color to green!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                    else:

                        print('You changed the color to yellow!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                elif '2' in user_card_chosen:

                    print('You made the computer draw two cards!')

                    print()

                    draw_2_counter = 2

                    while draw_2_counter > 0:

                        computer_hand.append(draw_pile[0])

                        draw_pile.pop(0)

                        draw_2_counter -= 1

                    input('Press "Enter" to continue: ')

                    print()

                elif 'Reverse' in user_card_chosen:

                    print('The order was reversed, so it\'s your turn again!')

                    print()

                    input('Press "Enter" to continue: ')

                    print()

                elif 'Skip' in user_card_chosen:

                    print('You skipped the computer\'s turn!')

                    print()

                    input('Press "Enter" to continue: ')

                    print()

                else:

                    print('You played a wild card!')

                    print()

                    user_turn += 1

                    color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                    while True:

                        print()

                        wild_card_color = input('Enter a color to make the wild card: ')

                        print()

                        if wild_card_color.upper() not in color_picker:

                            print('Enter a valid color!')

                        else:

                            break

                    if wild_card_color.upper() == 'RED':

                        print('You changed the color to red!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                    elif wild_card_color.upper() == 'BLUE':

                        print('You changed the color to blue!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                    elif wild_card_color.upper() == 'GREEN':

                        print('You changed the color to green!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

                    else:

                        print('You changed the color to yellow!')

                        print()

                        discard_pile.insert(0, wild_card_color.upper())

                        input('Press "Enter" to continue: ')

                        print()

            else:

                print('You played your card!')

                print()

                user_turn += 1

                input('Press "Enter" to continue: ')

                print()

            if len(user_hand) == 1:

                print('You have one card left, UNO!')

                print()

                input('Press "Enter" to continue: ')

                print()

        if (len(user_hand) == 0) or (len(computer_hand) == 0):

            if len(user_hand) == 0:

                print('You\'re out of cards!')

                uno_score['User Wins'] += 1

                break

            else:

                print('The computer is out of cards!')

                uno_score['Computer Wins'] += 1

                break

        if len(draw_pile) == 0:

            print('The draw pile is out of cards, we\'ll reshuffle the cards in the discard pile and continue play.')

            print()

            for card in discard_pile:

                draw_pile.append(card)

                discard_pile.remove(card)

            shuffle_number = random.randint(1, 10)

            while shuffle_number > 0:

                random.shuffle(draw_pile)

                shuffle_number -= 1

            discard_pile.append(draw_pile[0])

            draw_pile.remove(draw_pile[0])

            input('Press "Enter" to continue: ')

            print()

        if user_turn % 2 == 0:

            print('---------------------------------------------------------------------------------------------------')

            print()

            print('Computer\'s Hand:')

            computer_hand_hidden = []

            computer_hand_length = len(computer_hand)

            while computer_hand_length > 0:

                computer_hand_hidden.append('X')

                computer_hand_length -= 1

            print(computer_hand_hidden)

            print()

            print('Discard Pile Top Card:')

            print(discard_pile[0])

            print()

            print('Number of Cards In Draw Pile:')

            print(len(draw_pile))

            print()

            print('Your Hand:')

            print(user_hand)

            print()

            print('It\'s the computer\'s turn!')

            print()

            computer_card_choices = []

            if discard_pile[0][0] == 'W':

                for card in computer_hand:

                    computer_card_choices.append(card)

            else:

                for card in computer_hand:

                    if (card[0] == discard_pile[0][0]) or (card[0] == 'W') or (card[-1] == discard_pile[0][-1]):

                        computer_card_choices.append(card)

            if len(computer_card_choices) == 0:

                print('The computer doesn\'t have a card to play so it draws from the deck!')

                print()

                computer_hand.append(draw_pile[0])

                draw_pile.remove(draw_pile[0])

                computer_hand_hidden.append('X')

                user_turn += 1

                computer_invalid_card = True

                input('Press "Enter" to continue: ')

                print()

            else:

                computer_card_chosen = random.choice(computer_card_choices)

                computer_card_choices.clear()

                discard_pile.insert(0, computer_card_chosen)

                computer_hand_hidden.pop(0)

                for card in computer_hand:

                    if card == computer_card_chosen:

                        computer_hand.remove(card)

                uno_action_cards = ['Wild_Card', 'Wild_Draw_4', 'Red_Skip', 'Red_Reverse', 'Red_Draw_2+', 'Blue_Skip',
                                    'Blue_Reverse', 'Blue_Draw_2+', 'Green_Skip', 'Green_Reverse', 'Green_Draw_2+',
                                    'Yellow_Skip', 'Yellow_Reverse', 'Yellow_Draw_2+']

                if computer_invalid_card:

                    print('The computer\'s turn is over!')

                    print()

                    input('Press "Enter" to continue: ')

                    print()

                elif computer_card_chosen in uno_action_cards:

                    if '4' in computer_card_chosen:

                        print('The computer made you draw four cards!')

                        print()

                        draw_4_counter = 4

                        while draw_4_counter > 0:

                            user_hand.append(draw_pile[0])

                            draw_pile.pop(0)

                            draw_4_counter -= 1

                        color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                        wild_card_color = random.choice(color_picker)

                        if wild_card_color == 'RED':

                            print('The computer changed the color to red!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color == 'BLUE':

                            print('The computer changed the color to blue!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color == 'GREEN':

                            print('The computer changed the color to green!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                        else:

                            print('The computer changed the color to yellow!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                    elif '2' in computer_card_chosen:

                        print('The computer made you draw two cards!')

                        print()

                        draw_2_counter = 2

                        while draw_2_counter > 0:

                            user_hand.append(draw_pile[0])

                            draw_pile.pop(0)

                            draw_2_counter -= 1

                        input('Press "Enter" to continue: ')

                        print()

                    elif 'Reverse' in computer_card_chosen:

                        print('The order was reversed, so it\'s the computer\'s turn again!')

                        print()

                        input('Press "Enter" to continue: ')

                        print()

                    elif 'Skip' in computer_card_chosen:

                        print('The computer skipped your turn!')

                        print()

                        input('Press "Enter" to continue: ')

                        print()

                    else:

                        print('The computer played a wild card!')

                        print()

                        user_turn += 1

                        color_picker = ['RED', 'BLUE', 'GREEN', 'YELLOW']

                        wild_card_color = random.choice(color_picker)

                        if wild_card_color == 'RED':

                            print('The computer changed the color to red!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color == 'BLUE':

                            print('The computer changed the color to blue!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                        elif wild_card_color == 'GREEN':

                            print('The computer changed the color to green!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                        else:

                            print('The computer changed the color to yellow!')

                            print()

                            discard_pile.insert(0, wild_card_color)

                            input('Press "Enter" to continue: ')

                            print()

                else:

                    print('The computer played its card!')

                    print()

                    user_turn += 1

                    input('Press "Enter" to continue: ')

                    print()

            if len(computer_hand) == 1:

                print('The computer has one card left, UNO!')

                print()

                input('Press "Enter" to continue: ')

                print()


def uno_replay():

    print()

    print('Here\'s the score:')

    print(uno_score)

    print()

    while True:

        print()

        uno_user_replay = input('Would you like to play again? ("Yes"/"No") ')

        if uno_user_replay.lower() == 'yes':

            print('Okay, let\'s play again!')

            print()

            break

        elif uno_user_replay.lower() == 'no':

            print('Okay, thanks for playing!')

            exit()

        else:

            print('Please type either "Yes" or "No"!')


uno_game_greeting()

while True:

    uno_completed_deck = uno_deck_maker()

    shuffled_deck = uno_deck_shuffler(uno_completed_deck)

    gameplay_decks = card_dealer(shuffled_deck)

    gameplay_function(gameplay_decks[0], gameplay_decks[1], gameplay_decks[2])

    uno_replay()
