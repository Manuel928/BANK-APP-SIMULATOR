from pincode import passcode

currentBalance = 5000

def check_balance():
    tryCount = 0
    tryLimit = 3

    while tryCount < tryLimit:
        viewBalance = input("PLEASE ENTER YOUR PASSCODE TO VIEW YOUR CURRENT BALANCE...")
        tryCount += 1
        if viewBalance == str(passcode()):
            print("CURRENT BALANCE ==> $" + str(currentBalance))
            break
        else:
            print("*** Wrong Passcode...TRY AGAIN ***")
    else:
        print("ACCOUNT TEMPORARILY LOCKED... KINDLY VISIT ANY BRANCH OF 3VERSE BANK OF AFRIKA TO REACTIVATE YOUR ACCOUNT...")