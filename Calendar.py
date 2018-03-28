"""This program is an adjustable calendar. User can view, add,update or delete an event """
from time import sleep, strftime
name= "User" #customizable
calendar= {}
def welcome():
  print ("Welcome " + name) 
  print ("The calendar is now opening...")
  sleep
  print ("Today is: ") + strftime("%A %B %d, %Y")
  print ("The current time is ") + strftime ("%H:%M:%S")
  sleep
  print ("What would you like to do?")

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice= raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice.upper()
    #view
    if user_choice == "V":
      if len(calendar.keys())< 1:
        print ("Sorry. Calendar Empty.")
      else:
      	print calendar
    #update
    elif user_choice == "U":
      date= raw_input("What date?")
      update= raw_input("Enter the update: ")
      calendar[date]= update
      print ("Update successful.")
      print calendar
    #add
    elif user_choice == "A":
      event= raw_input(" Enter event: ")
      date= raw_input(" Enter date (MM/DD/YYYY: )")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")) :
        print "Invalid date"
        try_again= raw_input("Try again? Y for Yes, N for No: ")
        try_again.upper()
        #yes try again
        if try_again == "Y":
          continue
        else:
          start= False
      else:
        calendar[date]=event
        print "Event successfully added."
        print calendar
    #delete event
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        event= raw_input(" What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event successfully deleted."
            print calendar
          else:
            print ("Incorrect event specified.")
      #exit
    elif user_choice == "X":
      start = False
    else:
      print("Invalid entry")
      start= False
#test      
start_calendar()
      
          
     
      
     
    
        
        
      
      
      
      
      


