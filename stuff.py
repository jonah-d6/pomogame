import math
import time
from log import read

currentExperience = read()
currentLevel = int(math.log(currentExperience))

leftoverExperince = currentExperience - math.e ** currentLevel

experienceLeft = math.e ** (currentLevel + 1) - currentExperience

print(currentExperience,currentLevel,leftoverExperince, experienceLeft)
