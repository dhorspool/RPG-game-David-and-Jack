import colors

def eden():
  print(colors.yellow("very well young adventurer. so to pass, Master Lord (a weird reader) offers you the way if you answer his riddle:"))
  print("")
  riddleans=input(colors.cyan("the riddle is: There was a plane crash and every single person died, who survived?:"))
  badans = True  
  while badans:
    if riddleans == "married people":
      print("very well. you now have entered the %s." % (colors.red('EDEN')))
      break
    else:
      print("")
      print("the answer is not correct you shall not be granted the %s." % (colors.red("WAY")))
      print(" ")
      print(" ")
      riddleans=input(colors.cyan("the riddle is: There was a plane crash and every single person died, who survived?:"))
      
eden()

