import BirdBathFunc_CF_cls420 as BirdBath
import numpy as np

def gridSearch():
    best_fraction = -100
    minGuess  = [ -30.0, -30.0, -20.0 ]
    maxGuess  = [ +30.0, +30.0, +20.0 ]
    bestGuess  = [ -0.125, 0.125, 0.125 ]
    learning_rate     = 12 
    while learning_rate > 0.00125 :

        # Set the search ranges:
        rollMin   = bestGuess[0]-learning_rate*5
        rollMax   = bestGuess[0]+learning_rate*5
        tiltMin   = bestGuess[1]-learning_rate*5
        tiltMax   = bestGuess[1]+learning_rate*5
        twistMin   = bestGuess[2]-learning_rate*5
        twistMax   = bestGuess[2]+learning_rate*5

        if (rollMin <= minGuess[0]):
            rollMin = minGuess[0]
        if (tiltMin <= minGuess[1]):
            tiltMin = minGuess[1]
        if (twistMin <= minGuess[2]):
            twistMin = minGuess[2]

        if (rollMax > maxGuess[0]):
            rollMax = maxGuess[0]
        if (tiltMax > maxGuess[1]):
            tiltMax = maxGuess[1]
        if (twistMax > maxGuess[2]):
            twistMax = maxGuess[2]

        for twist in np.arange(twistMin, twistMax+learning_rate, learning_rate):
            for tilt in np.arange(tiltMin, tiltMax+learning_rate, learning_rate):
                for roll in np.arange(rollMin, rollMax+learning_rate, learning_rate):
                    fract = BirdBath.BirdBathFunc_CF_cls420(roll, tilt, twist)
                    if (fract >= best_fraction):
                        best_fraction = fract
                        bestGuess = [roll, tilt, twist]

        # Shrink the size of the grid slowly:
        learning_rate = (learning_rate * 21)/23
    print("roll: {}  tilt: {}  twist: {}".format(round(bestGuess[0], 6), round(bestGuess[1], 6), round(bestGuess[2], 6)))
    print("fraction percentage: {}".format(round(best_fraction, 6)))
    
        

def main():
    gridSearch()

if __name__ == '__main__':
    main()