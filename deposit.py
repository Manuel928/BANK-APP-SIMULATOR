from pincode import passcode

currentBalance = 5000

#Deposit processing function
def mainDeposit():
    tryCount = 0
    tryLimit = 3
    displayCurrentBalance = input("Would you like to view your current balance? type Yes or No: ")
    if displayCurrentBalance == "Yes".lower():
        print("$" + str(currentBalance))
    else:
        pass
    toDeposit = int(input("How much would you like to deposit? "))
    totalBalance = currentBalance + toDeposit
    
    #Setting up a system that blocks the transaction after 3 incorrect password
    while tryCount < tryLimit:
        depositConfirmation = int(input("***You are about to deposit $" + str(toDeposit) + " please enter your passcode to continue ***: "))
        tryCount += 1
        if depositConfirmation == passcode():
            print("$" + str(toDeposit) + " successfully deposited to your account")
            print("Your total available balance = $" + str(totalBalance))
            break
        else:
            print("*** Wrong Passcode...TRY AGAIN ***")
    else:
        print("ACCOUNT TEMPORARILY LOCKED... KINDLY VISIT ANY BRANCH OF 3VERSE BANK OF AFRIKA TO REACTIVATE YOUR ACCOUNT...")