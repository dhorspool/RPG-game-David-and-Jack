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
  print ("Let me make some things clear right off the bat:")
  print ("With the exception of your name, all words and commands and etc will need to be clear: If you are inputting a number, make it just a number. If you are making an action, make it just one word, all lowercase. Is that clear ? :")
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
      print ("Options: yes, no")
  
  print ("")
  print ("It looks like you are finally awake. Not even the storm lat night could wake you. I heard them say we finally reached the new world. Quiet now, I hear the guards coming.")
  print ("")
  print ("You, come with us, we need to take your census")
  print ("We don't have any records of you, so please tell us your occupation,and we will let you be on your way.")
  print ("")
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
  print ("Well then, you are free to go. Let me give you some information:")
  print ("")
  print ("You have arrived at the new world, a strange new land which has recently been discovered, and has started to be colonized. Reports have been arriving that there are ruins and strange creatures out in the wild, which still largely remain unexplored. You have probably arrived as an adventurer, looking to search these parts. Anyway, off you go")
  print ("")
  print ("You arrive at a fork on the road, where a sign points to  three paths. Were do you wanna go?")
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
    

  
