'''
### PowerBall Lottery

The Powerball lottery is a popular multi-state lottery game in the United States, known for its large jackpots and widespread participation. 
Players select five numbers from a set of 69 white balls and one number, the Powerball, from a set of 26 red balls. Drawings are held twice a week, typically on Wednesday and Saturday nights. 

To win the jackpot, a participant must match all five white ball numbers and the Powerball number. 
The odds of winning the jackpot are astronomical, at about 1 in 292.2 million, reflecting the game's design to build large jackpots that attract more players.
However, the game also offers smaller prizes for matching fewer numbers, which have significantly better odds of winning. 

Ticket prices are generally $2 per play, and tickets can be purchased in most convenience stores and even online.
'''

#smaller prizes for matching few numbers (bonus)


#select 5 numbers from a set of 69 white balls 1-69
#select 1 number, as a powerball - red 1-26

user_picks = []

wb1 = int(input("1st Number: "))
user_picks.append(wb1)

wb2 = int(input("2nd Number: "))
user_picks.append(wb2)

wb3 = int(input("3rd Number: "))
user_picks.append(wb3)

wb4 = int(input("4th Number: "))
user_picks.append(wb4)

wb5 = int(input("5th Number: "))
user_picks.append(wb5)

rb1 = int(input("Select Powerball: "))
user_picks.append(rb1)

print(user_picks)

#get computer to choose 5 and a pb

import random
white_balls = tuple(range(1,70))
red_balls = tuple(range(1, 27))
computer_5 = random.sample(white_balls, 5)
computer_pb = random.sample(red_balls, 1)
the_pb_numbers = computer_5 + computer_pb

print(the_pb_numbers)


#to win must match all 5 + powerball










