charactDict = {'warrior':{'hp':16, 'atk':2,'def':2}, 'mage':{'hp':12, 'atk':4,'def':0},'rogue':{'hp':14, 'atk':3,'def':1}}


class Character:
    
  def __init__(self, name, hp, attackPoints, defensePoints, level):
    self.name = name
    self.description = "This shape has not been described yet"
    self.author = "Nobody has claimed to make this shape yet"
    self.HP = hp
    self.atk = attackPoints
    self.defense = defensePoints
    self.level = level
    
  def printStats(self):
    strStats = 'HP = {}, atk = {}, def = {}'.format(self.HP,self.atk,self.defense)
    print(strStats)
  
  def increaseLevel(self):
    self.level = self.level + 1

class Warrior(Character):
  
  def __init__(self, name):
    pro = 'warrior'
    self.description = "This shape has not been described yet"
    self.name = name
    self.HP = charactDict[pro]['hp']
    self.atk = charactDict[pro]['atk']
    self.defense = charactDict[pro]['def']
    self.level = 1
    
class Mage(Character):
  
  def __init__(self, name):
    pro = 'mage'
    self.description = "This shape has not been described yet"
    self.name = name
    self.HP = charactDict[pro]['hp']
    self.atk = charactDict[pro]['atk']
    self.defense = charactDict[pro]['def']
    self.level = 1
    
class Rogue(Character):
  
  def __init__(self, name):
    pro = 'rogue'
    self.description = "This shape has not been described yet"
    self.name = name
    self.HP = charactDict[pro]['hp']
    self.atk = charactDict[pro]['atk']
    self.defense = charactDict[pro]['def']
    self.level = 1
