#Program to average random numbers and create histogram
#import sectino
import random as rand
import matplotlib.pyplot as plt

#initialize some variables
how_often_each = [0,0,0,0,0,0,0,0,0,0]
N_points = 500
n_bins = 10
X = [] #will hold the average values

#function to generate random number, probably overkill could call randrange directly
def new_random_number():
    return rand.randrange(1,11)
#function that actually does the work of averaging and adding to the array
def how_often():
    totalcount = 0
    lastnumber = 0
    for i in range(1,1001):
        new_number = new_random_number()
        #my way of only averaging on every pair
        if i%2 == 0:
                X.append((new_number + lastnumber)/2)
        how_often_each[new_number-1] +=1
        totalcount +=1
        lastnumber = new_number
    return totalcount
#call the how_often function
end_results = how_often()
#printing results to console
for i in range(1,11):
    print("Value ", i, "occurred", how_often_each[i-1], "times")
print("The total count was ", end_results)
#not required, prints each average
print(X)
#make hisogram
plt.hist(X,bins=[1,2,3.,4,5,6,7,8,9,10])
plt.suptitle("My First Matplotlib Histogram")
plt.ylabel("number of occurences")
plt.show()