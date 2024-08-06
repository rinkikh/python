import time #module

def countdown(t): #user defined function
    
    while t:  #loop run until t not zero
        mins,secs =divmod(t,60)
        timer = '{:02d}:{:02d}' .format(mins,secs)
        print(timer, end ="\r")
        time.sleep(1)
        t -=1
        
    
t= input("enter time in sec:")

countdown(int(t)) #convertint to int type