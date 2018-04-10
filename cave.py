import colors
def cave():
  print(colors.yellow("very well young adventurer. so to pass, Master Ori (a weird bar tender) offers you the way if you answer his riddle:"))
  print("")
  riddleans=input(colors.cyan("the riddle is: what ios tall when its young and short when its old?:"))
  badans = True  
  while badans:
    if riddleans == "candle":
      print("very well. you now have entered the %s." % (colors.red('CAVE')))
      
      break
    else:
      print("")
      print("the answer is not correct you shall not be granted the %s." % (colors.red("WAY")))
      print(" ")
      print(" ")
      riddleans=input(colors.cyan("the riddle is: what ios tall when its young and short when its old?:"))
  import encounter
cave()
