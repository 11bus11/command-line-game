wantinfo = input("Write y to read info. Write n to go straight to game.")



def start_info():
    return(wantinfo)

def start_game():
    return(wantinfo)

ans = "h"
while wantinfo != "y":  
    wantinfo = input("Write either y or n")

if wantinfo == "y":
    print(wantinfo)
elif wantinfo == "n":
    print(wantinfo)
    ans = "n"
else: 
    print("error")
        