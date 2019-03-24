# ###################################################################################
# VOCAL COMMANDS 
#
# WARNING : basic vocal commands ( activated only if chatbot is disable inside config/service_A_Chatbot.config )
#
# More basic vocal commands with ear.addCommand
# More associated functions into inmoovGestures
# Almost all chatbot vocal command into chatbot\bots\[lang]\aiml\_inmoovGestures.aiml
# ###################################################################################

#ear.addCommand("open your hand", "python", "rightHandOpen")

## Right hand movement
 
def rightHandOpen():
  i01.moveHand("right",0,0,0,0,0)
  talkBlocking(u"Ma main est ouverte")

def rightHandClose():
  i01.moveHand("right",180,180,180,180,180)
  talkBlocking(u"Ma main est fermée")

def rightHandCountOne():
  i01.moveHand("right",180,180,180,0,180)
  talkBlocking(u"Un")
  
def rightHandCountTwo():
  i01.moveHand("right",180,180,0,0,180)
  talkBlocking(u"Deux")
  
def rightHandCountThree():
  i01.moveHand("right",180,180,0,0,0)
  talkBlocking(u"Trois")
  
def rightHandCountFour():
  i01.moveHand("right",0,0,0,0,180)
  talkBlocking(u"Quatre")
  
## Left hand movement
 
def leftHandOpen():
  i01.moveHand("left",0,0,0,0,0)
  talkBlocking(u"Ma main est ouverte")

def leftHandClose():
  i01.moveHand("left",180,180,180,180,180)
  talkBlocking(u"Ma main est fermée")

def leftHandCountOne():
  i01.moveHand("left",180,180,180,0,180)
  talkBlocking(u"Un")
  
def leftHandCountTwo():
  i01.moveHand("left",180,180,0,0,180)
  talkBlocking(u"Deux")
  
def leftHandCountThree():
  i01.moveHand("left",180,180,0,0,0)
  talkBlocking(u"Trois")
  
def leftHandCountFour():
  i01.moveHand("left",0,0,0,0,180)
  talkBlocking(u"Quatre")
  
## Both hands

def handsOpen():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,0)
  talkBlocking(u"Mes mains sont ouvertes")

def handsClose():
  i01.moveHand("left",180,180,180,180,180)
  i01.moveHand("right",180,180,180,180,180)
  talkBlocking(u"Mes mains sont fermées")

def handsCountSix():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",180,180,180,180,0)
  talkBlocking(u"Six")
  
def handsCountSeven():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",180,180,0,0,180)
  talkBlocking(u"Sept")
  
def handsCountEight():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",180,180,0,0,0)
  talkBlocking(u"Huit")
  
def handsCountNine():
  i01.moveHand("left",0,0,0,0,0)
  i01.moveHand("right",0,0,0,0,180)
  talkBlocking(u"Neuf")