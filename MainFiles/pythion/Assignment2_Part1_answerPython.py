import random as rand
import numpy as np

index = 0  #used to find mode
how_often_each = np.zeros(27,dtype=int) #array to keep track of how often each hand is drawn

#function assigns the card an appropriate value
def card_value(card):
    if card > 9:
        value = 10
    else:
        value = card
    #print("card is " +str(card) + "and value is " + str(value))
    return value
#function draw_two adds a pair of card values and increases the count for that value
def draw_two():
    hand = card_value(rand.randrange(1,14))+card_value(rand.randrange(1,14))
    how_often_each[hand]+=1
#loop to conduct specified number of trials
number_of_trials = 100001
for i in range(1,number_of_trials):
    draw_two()
#prints data out on the number of each hand
for handvalue in range(2,21):
    print("Hand Value ", handvalue, "occurred", how_often_each[handvalue], "times. A percentage of {:.3%}".format(how_often_each[handvalue]/number_of_trials))
max = 0
#find mode by finding hand with maximum number of occurrences
for hand in range(2,21):
    if how_often_each[hand] > max:
        max = how_often_each[hand]
        index = hand
print("The mode occurred at " + str(index) +". It occured {:.3%} ".format(how_often_each[index]/number_of_trials) + "percent of the time")
#find median
cdf = 0
check_for_median = True #When set to False will stop looking for Median
for hand in range(2,21):
    cdf = cdf + how_often_each[hand]
    percentage = cdf/number_of_trials
    #print("{:.5}".format(percentage))
    if (cdf/number_of_trials) > 0.5 and check_for_median ==True:
        fraction = ((number_of_trials/2)-(cdf-how_often_each[hand]))/(how_often_each[hand])
        check_for_median = False
        print("the fraction is {:.4}  and the median is {:.4}".format(fraction,hand+fraction-1))

