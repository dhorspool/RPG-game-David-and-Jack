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
    import forest
  elif answer == "cave":
    import cave
    
  elif answer == "eden":
    import eden  
    
  else:
    print("You wrote it wrong")
    

  
