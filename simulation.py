
# coding: utf-8

# In[ ]:

#get_ipython().magic(u'matplotlib inline')
from random import randrange
import matplotlib.pyplot as PLT

biasedDiceDist = [1,2,3,4,4,4,5,6]
unbiasedDiceDist= [1,2,3,4,5,6]
board = [0] * 40
rollSum = 0
fig = PLT.figure()

def roll(dist):
    return dist[randrange(len(dist))]

def simulateGame(no, dist):
    global rollSum
    global board
    rollSum = 0
    board = [0] * 40
    for x in range(0, no):
        rollSum += roll(dist)
        if rollSum >= 40:
            rollSum -= 40
        board[rollSum] += 1
    

def runSimulation(no):
    for x in range(0, no):
        global fig
        simulateGame(10000, biasedDiceDist)
        biased = fig.add_subplot(211)
        #biased.plot(board)
        biased.hist(board, 50, normed=1, facecolor='r', alpha=0.2)
        biased.grid(True)
        simulateGame(10000, unbiasedDiceDist)
        unbiased = fig.add_subplot(212)
        #unbiased.plot(board)
        unbiased.hist(board, 50, normed=1, facecolor='g', alpha=0.2)

print 'Running Simulation ... '
runSimulation(1000)
print 'Simulation Complete... '
print 'Saving Plots... '
PLT.savefig('./plot.png')
print 'Rendering Complete.'









