import random
def random_select(uch):
  if uch==1:
    rs=random.choice([2,3])
  if uch==2:
    rs=random.choice([1,3])
  if uch==3:
    rs=random.choice([1,2])
  return rs

def _displayrno(pt):
  if pt==1:
    print("I choose Stone")
  elif pt==2:
    print("I choose Paper")  
  else:
    print("I choose Scissor")
    
def print_menu():
  print("Enter 1 to select Stone")
  print("Enter 2 to select Paper")
  print("Enter 3 to select Scissor")
  
flag1=0
flag2=0
print("Welcome to Stone|Paper|Scissor")
ch=int(input("Enter 1 to play: "))
if ch==1:
    choice=True
    while(choice):
      print_menu()
      uch=int(input("Enter your choice "))
      pt=random_select(uch)
      _displayrno(pt)
      if (uch==1 and pt==2) or (uch==2 and pt==3) or (uch==3 and pt==1):
        print("Yess !!! I win this round")
        flag1+=1
      #for user
      elif(uch==2 and pt==1) or (uch==3 and pt==2 ) or (uch==1 and pt==3):
        print("Uggh!! I lost this round")
        flag2+=1
      else:
        print("Enter a valid choice. Please try again!!!")
        continue
      print("---Scores---")
      print("User: {}".format(flag2))
      print("Computer: {}".format(flag1))
      print("------------")
      if(flag1==5):
        print("---COMPUTER OWN THIS MATCH---")
      if(flag2==5):
        print("---YOU OWN THIS MATCH---")
      c=input("Do you want to continue?(y/n): ")
      if c=="n":
        choice=False
      if (flag1==5 or flag2==5):
        c=input("Do you want to Play again?(y/n): ")
        if c=="n":
          choice=False
       
      

      