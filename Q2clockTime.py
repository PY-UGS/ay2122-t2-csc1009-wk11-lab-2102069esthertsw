import time

class clockTime:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self, val):
        self.hours = val
        self.showTime()

    def setMinutes(self, val):
        self.minutes = val
        self.showTime()


    def setSeconds(self, val):
        self.seconds = val
        self.showTime()

    def setTime(self, val1, val2, val3):
        self.hours = val1
        self.minutes = val2
        self.seconds = val3
        self.showTime()
    
    def showTime(self):
        print("Time is " , self.hours, ":", self.minutes,":", self.seconds)

myClock = clockTime()
while(1):
    choice = int(input("Select an option: \n1 - Set hours\n2 - Set minutes\n3 - Set seconds\n4 - Set time\n5 - Show time\n6 - Exit\n"))
#     intialise variables to pass the while loop conditions below until user enter a valid input
    hours = -1
    minutes = -1
    seconds = -1
#     python switch case equivalent
    match choice:
        case 1:
            while(hours<0 or hours>23):
                hours = int(input("Enter hours value: "))
            myClock.setHours(hours)
            hours = -1 #prepare to pass while loop conditions again if user chooses to set hour again
        case 2:
            while(minutes<0 or minutes>59):
                minutes = int(input("Enter minutes value: "))
            myClock.setMinutes(minutes)
            minutes = -1 #prepare to pass while loop conditions again if user chooses to set minutes again
        case 3:
            while(seconds<0 or seconds>59):
                seconds = int(input("Enter seconds value: "))
            myClock.setSeconds(seconds)
            seconds = -1 #prepare to pass while loop conditions again if user chooses to set seconds again
        case 4:
            while(hours<0 or hours>23):
                hours = int(input("Enter hours value: "))
            while(minutes<0 or minutes>59):
                minutes = int(input("Enter minutes value: "))
            while(seconds<0 or seconds>59):
                seconds = int(input("Enter seconds value: "))
            myClock.setTime(hours, minutes, seconds)
            
            #prepare to pass while loop conditions again if user chooses to set time again
            hours = -1
            minutes = -1
            seconds = -1
            
        case 5:
            myClock.showTime()
        case _: #default - if user enters an invalid input
            print("Exiting")
            break
