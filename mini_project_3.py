'''
For this mini project, we are going to build a poker hand evaluator.  
For those not familiar with poker, it is a card game played with a standard card deck of 52 cards. 

Poker, a game that comes in various forms, is a card game played with two or more people (the maximum player count is determined by the type of poker game).  
The way the cards are dealt can vary wildly, but the base concept is the same:  
A player wants to get the best 5-card hand possible and win the chips in the middle that have been bet.

There are many more factors that drive poker gameplay (such as bluffing) but there is always one final comparison that determines a winner of a hand: The showdown.

The showdown is where the players that have not folded compare their hands to each other to find a winner.
'''

#first is to build a deck

# after research -- A standard poker deck contains 52 cards. 
# These are divided into four suits: clubs, diamonds, hearts, and spades. 
# Each suit has 13 cards: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. 

#thought is is create the four suits as keys and be able to access them:

#i want to keep everything as and int in the value section 

'''
1 = "ACE"
11 = "JACK"
12 = "QUEEN"
13 = "KING"
'''

card_nums = list(range(1, 14))  # flat list, not a list of a list

poker_deck = {
    "club": card_nums,
    "diamond": card_nums,
    "heart": card_nums,
    "spade": card_nums
}

# print(card_nums)

#card counter -- try to access and show 52 cards
i = 1
for suit in poker_deck:
    for card in poker_deck[suit]:
        print(f"{i}: {suit} {card}")
        i += 1

        