import random as rand
Heads_or_Tails = [0,0]
for i in range(0,100000):
    result = rand.randrange(0,2)
    if (result == 0):
        Heads_or_Tails[0] += 1
    else:
        Heads_or_Tails[1] +=1
print("Heads =  ",Heads_or_Tails[0], "Tails = ",Heads_or_Tails[1])