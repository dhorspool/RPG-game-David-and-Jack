import colors
import random



def forest():
  print(colors.yellow("very well young aprentice. so to pass, Master Elenoid (a weird basard) offers you the way if you answer his riddle:"))
  print("")
  riddleans=input(colors.cyan("the riddle is: what walks with four legs in the morning, two in the afternoon and three at night?:"))
  badans = True
  while badans:
    if riddleans == "man":
      print("very well. you now have entered the %s." % (colors.red('FOREST')))
      break
    else:
      print("")
      print("the answer is not correct you shall not be granted the %s." % (colors.red("WAY")))
      print(" ")
      print(" ")
      riddleans=input(colors.cyan("the riddle is: what walks with four legs in the morning, two in the afternoon and three at night?:"))
      

def start_forest():
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
    elif walking == "l":
      print ("you have successfully mooved to the left")
    elif walking == 'r':
      print ('you have now turned right')
    else:
      print ('you have wrote it wrong')
      
      
  else:
    print ("")
    print (colors.red('You have encountered a wild beast!'))
    random.shuffle(enemies)
    print ('Its a: %s!' % (enemies[0]))
    
  

  
  
        







forest()
start_forest()
