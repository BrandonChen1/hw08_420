import BirdBathFunc_Qj_cls420 as b

import random

def randomSearch():
    #https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf
    #Implementation based off this paper
    threshold = .499
    currentCost = 0
    tiltRandom = 0
    rowRandom = 0
    twistRandom = 0
    while currentCost < threshold:
        tiltRandom = random.uniform(-30,30)
        rowRandom = random.uniform(-30,30)
        twistRandom = random.uniform(-30,30)
        currentCost = b.BirdBathFunc_Qj_cls420(tiltRandom, rowRandom, twistRandom)
    print("tilt = {}, row ={}, twist = {}".format(tiltRandom, rowRandom, twistRandom))
    print("fraction in water = {}".format(currentCost))


randomSearch()