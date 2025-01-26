import random
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
for i in range(100000) :
 
   
  def check(comp, user):
    if comp ==user:
      return 0
 
    if(comp == 0 and user ==1):
      return -1
 
    if(comp == 1 and user ==2):
      return -1
 
    if(comp == 2 and user == 0):
      return -1
 
    return 1
 
 
  comp = random.randint(0, 2)
  user = int(input("0 for Rock, 1 for Paper and 2 for Scissors, 8 to end the game :\n "))
  if user == 8:
    break
  score = check(comp, user)
 
  print("You: ", user)
  print("Computer: ", comp)
 
  if(score == 0):
    print("Its a draw")
  elif (score == -1):
    print("You Lose")
  else: