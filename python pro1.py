import random


a=["stone","paper","scissor"]
while True:
    x=input("do you want to play the game?\n(type Y to play and type N to not)\n")
    if x=='Y':
        b=input("Enter stone,paper or scissor")
        random.shuffle(a)
        c= a.pop()
        print("The system got",c)
        if b=="stone":
            if c=="stone":
                print("its a draw")
            if c=="paper":
                print("you lost")
            if c=="scissor":
                print("you won")
        if b=="paper":
            if c=="stone":
                print("its a won")
            if c=="paper":
                print("you draw")
            if c=="scissor":
                print("you lost")
        if b=="scissor":
            if c=="stone":
                print("its a lost")
            if c=="paper":
                print("you won")
            if c=="scissor":
                print("you draw")
        
    elif x=='N':
        print("OK BYE!")
        break
    else:
        print("Hey user either type yes or no if you want to play please dont type uneccessary values")
        break
    
