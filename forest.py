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
      

  import encounter

forest()
