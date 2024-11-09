import math

currentExperience = 600
currentLevel = int(math.log(currentExperience))
leftoverExperince = currentExperience - math.e ** currentLevel

print(currentExperience,currentLevel,leftoverExperince)

