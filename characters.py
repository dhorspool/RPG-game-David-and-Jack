import random
import csv

filename ="enemies.csv"
lect = open(filename)
fitxer = csv.reader(lect)

charactDict = {'warrior':{'hp':16, 'atk':2,'def':2}, 'mage':{'hp':12, 'atk':4,'def':0},'rogue':{'hp':14, 'atk':3,'def':1}}

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
  enemy = Character(enemyChosen, enemiestats[enemyChosen]['hp'], enemiestats[enemyChosen]['atk'], enemiestats[enemyChosen]['def'], 1, 0)
  return enemy

class Character:
    
  def __init__(self, name, hp, attackPoints, defensePoints, level,exp):
    self.name = name
    self.description = "This shape has not been described yet"
    self.author = "Nobody has claimed to make this shape yet"
    self.HP = hp
    self.atk = attackPoints
    self.defense = defensePoints
    self.level = level
    self.exp = exp
    
  def printStats(self):
    strStats = 'HP = {}, atk = {}, def = {},'.format(self.HP,self.atk,self.defense)
    print(strStats)
 
  def gainexp(self,expnum):
    self.exp = self.exp + expnum
    print ("You gained %s exp" % (expnum,))
    levelup = self.level * 15
    print ("Old level: %s " % (self.level,) )
    while self.exp >= levelup: 
      self.level = self.level + 1
      self.exp = self.exp - levelup
    print ("Current level: %s " % (self.level,) )
    
class Warrior(Character):
  
  def __init__(self, name):
    pro = 'warrior'
    self.description = "This shape has not been described yet"
    self.name = name
    self.HP = charactDict[pro]['hp']
    self.atk = charactDict[pro]['atk']
    self.defense = charactDict[pro]['def']
    self.level = 1
    self.exp = 0
    
class Mage(Character):
  
  def __init__(self, name):
    pro = 'mage'
    self.description = "This shape has not been described yet"
    self.name = name
    self.HP = charactDict[pro]['hp']
    self.atk = charactDict[pro]['atk']
    self.defense = charactDict[pro]['def']
    self.level = 1
    self.exp = 0
    
class Rogue(Character):
  
  def __init__(self, name):
    pro = 'rogue'
    self.description = "This shape has not been described yet"
    self.name = name
    self.HP = charactDict[pro]['hp']
    self.atk = charactDict[pro]['atk']
    self.defense = charactDict[pro]['def']
    self.level = 1
    self.exp = 0   
