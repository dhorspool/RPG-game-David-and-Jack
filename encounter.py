import colors
import random
import characters



def first_encounter():
  global enemy
  i = 0
  enemies = ['MagicWolf','GiantBee','Rat','Dragon']
  print ("")
  print ("")
  print ('w = walk foward')
  print ('l = go left')
  print ('r = go right')
  while i < 3:
    i=i+1
    print("")
    walking=input('What do you wanna do?')
    if walking == "w":
      print (colors.yellow('Perefect! You have moved 10 m forward.'))
      print('10')
    elif walking == "l":
      print ("you have successfully mooved to the left")
    elif walking == 'r':
      print ('you have now turned right')
    else:
      print ('you have wrote it wrong')
      
      
  else:
    print ("")
#    print (colors.red('You have encountered a wild beast!'))
    print('wild beast')
    enemy = characters.choseEnemy()
    print ('Its a: %s!' % (enemy.name))
    
def first_combat():
  print (enemy.name)
  
    
first_encounter()
first_combat()
"""enemy = Character(enemyChosen, enemiestats[enemyChosen]['hp'], enemiestats[enemyChosen]['atk'], enemiestats[enemyChosen]['def'], 1, 0) """




