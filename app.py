class person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"hi , i am {self.name}")
stephen=person("stephen mulwa")
stephen.talk()
numbers=[78,90,105,567]
print(max(numbers))
#from portofolio import*
from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)
import random
for i in range(3):
    print(random.randrange(30,40))
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        third = random.randint(1,6)
        fourth = random.randint(1,6)
        return first,second,third,fourth
        if dice.roll==6:
            print("you have a chance to roll again")
dice = Dice()
print(dice.roll())
from portofolio import*

