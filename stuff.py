import math
from log import read

experienceLog = read()
currentExperience = experienceLog[0]
currentLevel = int(math.log(currentExperience))

def leftoverExperience(): return currentExperience - math.e ** currentLevel

def experienceLeft(): return math.e ** (currentLevel + 1) - currentExperience
