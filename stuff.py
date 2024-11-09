import math

def leftoverExperience(currentExperience, currentLevel): return currentExperience - math.e ** currentLevel

def experienceLeft(currentExperience, currentLevel): return math.e ** (currentLevel + 1) - currentExperience

def levelFromXP(currentExperience): return math.floor(math.log(currentExperience))
