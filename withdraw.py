from pincode import passcode

currentBalance = 5000

#Withdrawal processing function
def mainWithdraw():
    tryCount = 0
    tryLimit = 3
    displayCurrentBalance = input("Would you like to view your current balance? y/n: ")
    if displayCurrentBalance == "Y".lower():
        print("$" + str(currentBalance))
    else:
        pass
    toWithdraw = int(input("How much would you like to withdraw? "))

    if toWithdraw > currentBalance: #Checking if the amount to withdraw is greater than the current balance
        print("Insufficient Funds\n")
        tryAgain = input("Please enter a valid amount. Continue y/n ?: ")
        if tryAgain == "Y".lower():
            mainWithdraw()
        else:
            print("Thanks for using our service... Please come again anytime!")
    else:
        totalBalance = currentBalance - toWithdraw

        #Setting up a system that blocks the transaction after 3 incorrect password
        while tryCount < tryLimit:
            withdrawalConfirmation = int(input("***You are about to withdraw $" + str(toWithdraw) + " please enter your passcode to continue ***: "))
            tryCount += 1
            if withdrawalConfirmation == passcode():
                print("$" + str(toWithdraw) + " successfully withdrawn from your account")
                print("Your total available balance = $" + str(totalBalance))
                break
            else:
                print("*** Wrong Passcode...TRY AGAIN ***")
        else:
            pass
        