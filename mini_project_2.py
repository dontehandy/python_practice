'''
### PowerBall Lottery

The Powerball lottery is a popular multi-state lottery game in the United States, known for its large jackpots and widespread participation. 
Players select five numbers from a set of 69 white balls and one number, the Powerball, from a set of 26 red balls. Drawings are held twice a week, typically on Wednesday and Saturday nights. 

To win the jackpot, a participant must match all five white ball numbers and the Powerball number. 
The odds of winning the jackpot are astronomical, at about 1 in 292.2 million, reflecting the game's design to build large jackpots that attract more players.
However, the game also offers smaller prizes for matching fewer numbers, which have significantly better odds of winning. 

Ticket prices are generally $2 per play, and tickets can be purchased in most convenience stores and even online.
'''

# sudo for understanding:

#select 5 numbers from a set of 69 white balls 1-69
#select 1 number, as a powerball - red 0-26
#to win must match all 5 + powerball
#smaller prizes for matching few numbers

#first build a list of usable numbers. #revisit use of set, tuples

white_ball_range = range(1,70)
white_ball_tuple = tuple(white_ball_range)

print(white_ball_tuple)

