import time
import matplotlib.pyplot as plt
import random
x = 0
z = 0
speed = []
tries = [1, 2, 3, 4, 5]
for choose in range(0,18):
    words = ["picture", "pale", "love", "protect", "dolls", "stingy", "mark", "card", "science", "store", "smoke", "cast", "flag", "alike", "ugly", "wren", "dance", "chase"]
    ranword = random.randint(0,len(words)-1)
    choosed = words[ranword]
    break
word = choosed
print("The given word is", word)
while x < 5:
    ogt = time.time()
    given = str( input ("Type the word: "))
    t = time.time()
    time_took = round(t - ogt, 1)
    speed.append(time_took)
    print(time_took, "seconds")
    x += 1
    if given != choosed:
           z += 1
    if x >= 5:
        print("You made", z, "number of mistakes")
        plt.plot(tries, speed)
        plt.ylabel("Seconds you took to type")
        plt.xlabel("No. of tries")
        plt.show()
    

    
