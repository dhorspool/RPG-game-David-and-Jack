import csv
import random
import texts
import characters
import colors
from characters import charactDict

def choseEnemy():
  enemiestats = {}

  for row in fitxer:
    enemiestats[row[0]] = {} 
    enemiestats[row[0]]['atk']=row[1]
    enemiestats[row[0]]['def']=row[2]
    enemiestats[row[0]]['hp']=row[3]

  enemies = list(enemiestats.keys())
  random.shuffle(enemies)
  enemyChosen = enemies[0]
  enemy = characters.Character(enemiestats[enemyChosen], enemiestats[enemyChosen]['hp'], enemiestats[enemyChosen]['atk'], enemiestats[enemyChosen]['def'], 1 )
  return enemy

filename ="enemies.csv"
lect = open(filename)
fitxer = csv.reader(lect)
inventory=[]

badans = True

theEnemy = choseEnemy()

print ("Hello Adventurer, What is your Name?")
crname = input("")


texts.intro(crname)


crclass = texts.chrType(charactDict)

print ("Great!")
  
'''atack, defence, base hp and level'''

if crclass == "warrior" :
  crstats = characters.Warrior(crname)
elif crclass == "mage":
  crstats = characters.Mage(crname)
elif crclass == 'rogue':
  crstats = characters.Rogue(crname)

print('Wellcome {} the {}'.format(crname, crclass.capitalize()))
crstats.printStats()

texts.chosePath()
