import colors


def intro(charName):
  understood=True
  print ("%s, right? Not the name I would have chosen." %(colors.yellow(charName)))
  print ("")
  
  print ("anyways, are you a %s or a %s" % (colors.cyan("female"),(colors.cyan("male"))))
  crgender = input("")
  badans = True  
  while badans:
    if crgender == "male":
      print((colors.cyan('Perfect!')))
      break
      
    elif crgender == "female":
      print (colors.magenta("Perfect!"))
      break
    else:
      print("gender %s" %(colors.yellow("NOT FOUND!")))
      print ("please write one of the %s:" %(colors.red("ABOVE")))
    crgender=input("")
      
  
  print ("")
  print ("Let me make some things clear Right off the bat:")
  print ("With the exception of Your Name, All words and commands amd etc will need to be clear: If you are inputting a number, make it just a number. If you are making an action, make it just one word, all lowercase. Is that clear ? :")
  print ("")
  print(colors.cyan("Options: yes, no"))
  
  while understood:
    ans = str(input(""))
    if ans == "Yes":
      print ("Repeat, in lowercase")
    elif ans == "No":
      print ("Repeat, in lowercase")
    elif ans == "no":
      print ("With the exception of Your Name, All words and commands amd etc will need to be clear: If you are inputting a number, make it just a number. If you are making an action, make it just one word, all lowercase. Is that clear ? ")
      print ("")
      print ("Options: yes, no")
      
    elif ans == "yes":
      print ("Great! Now we can understand each other")
      understood = False
    else:
      print ("Options:")
      print ("yes")
      print ("no")
  
  print ("Anyway, Lets get started:")
  print ("")
  print ("You awake in the land of Russia, a magical place where dreams come true, and magic and animals roam the land. You are a :")
  print ("")

def chrType(dictChar):
  
  def printChars():
    print('{:^20}|{:^14s}|{:^14s}|{:^14s}|'.format(colors.yellow('TYPE'), colors.yellow('ATK'), colors.yellow('DEF'), colors.yellow('HP')))
    for chrtype in dictChar.keys():
      chrStats = dictChar[chrtype]
      
      print('{:^20}|{:^5d}|{:^5d}|{:^5d}|'.format(colors.cyan(chrtype), chrStats['atk'], chrStats['def'], chrStats['hp']))
    print()
    crclass = str(input("So, What are you?"))
    return crclass
  crclass = printChars()
  typesCh = dictChar.keys()
  while crclass not in typesCh:
    print ("")
    print ("Please choose a correct class name")
    print ("")
    crclass = printChars()
    
    
  
  return crclass

def chosePath():
  print ("")
  print ("Well then, lets begin:")
  print ("You have three paths. Were do you wanna go?")
  print ("")
  print (colors.red("-Forest"))
  print (colors.red("-Cave"))
  print (colors.red("-Eden"))
  print ("")
  answer=input(colors.magenta("So where:"))
  

  
  if answer == "forest":
    print(colors.yellow("very well young aprentice. so to pass, Master Elenoid (a wierd basard) offers you the way if you answer his riddle:"))
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
        
  elif answer == "cave":
      print(colors.yellow("very well young adventurer. so to pass, Master Ori (a wierd bar tender) offers you the way if you answer his riddle:"))
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
    
  elif answer == "eden":
    print(colors.yellow("very well young man. so to pass, Master Lord (a wierd reader) offers you the way if you answer his riddle:"))
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
  
  else:
    print("You wrote it wrong")
    

