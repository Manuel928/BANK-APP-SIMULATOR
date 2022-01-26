from pincode import passcode

currentBalance = 5000

def buy_airtime():
    tryCount = 0
    tryLimit = 3
    phone_number = int(input("ENTER THE PHONE NUMBER YOU WANT TO RECHARGE ON: "))
    select_network = input("SELECT NETWORK: \n" +
    "1.MTN " +
    "2.AIRTEL " +
    "3.GLO " +
    "4.9MOBILE\n")

    amount_to_recharge = int(input("ENTER AN AMOUNT TO RECHARGE: "))

    #Airtime Processing For MTN
    if select_network == "1":
        while tryCount < tryLimit:
            airtimeConfirmation = input("YOU ARE ABOUT TO RECHARGE $" + str(amount_to_recharge) + " ON YOUR MTN LINE " + str(phone_number) + " ENTER YOUR PIN TO CONTINUE...")
            tryCount += 1
            if airtimeConfirmation == str(passcode()):
                currentBalance - amount_to_recharge
                print("AIRTIME PURCHASE OF $" + str(amount_to_recharge) + " WAS SUCCESSFUL!")
                break
            else:
                print("*** Wrong Passcode...TRY AGAIN ***")
        else:
            print("ACCOUNT TEMPORARILY LOCKED... KINDLY VISIT ANY BRANCH OF 3VERSE BANK OF AFRIKA TO REACTIVATE YOUR ACCOUNT...")
    
    #Airtime Processing For AIRTEL
    elif select_network == "2":
        while tryCount < tryLimit:
            airtimeConfirmation = input("YOU ARE ABOUT TO RECHARGE $" + str(amount_to_recharge) + " ON YOUR GLO LINE " + str(phone_number) + " ENTER YOUR PIN TO CONTINUE...")
            tryCount += 1
            if airtimeConfirmation == str(passcode()):
                currentBalance - amount_to_recharge
                print("AIRTIME PURCHASE OF $" + str(amount_to_recharge) + " WAS SUCCESSFUL!")
                break
            else:
                print("*** Wrong Passcode...TRY AGAIN ***")
        else:
            print("ACCOUNT TEMPORARILY LOCKED... KINDLY VISIT ANY BRANCH OF 3VERSE BANK OF AFRIKA TO REACTIVATE YOUR ACCOUNT...")
    
    #Airtime Processing For GLO
    elif select_network == "3":
        while tryCount < tryLimit:
            airtimeConfirmation = input("YOU ARE ABOUT TO RECHARGE $" + str(amount_to_recharge) + " ON YOUR MTN LINE " + str(phone_number) + " ENTER YOUR PIN TO CONTINUE...")
            tryCount += 1
            if airtimeConfirmation == str(passcode()):
                currentBalance - amount_to_recharge
                print("AIRTIME PURCHASE OF $" + str(amount_to_recharge) + " WAS SUCCESSFUL!")
                break
            else:
                print("*** Wrong Passcode...TRY AGAIN ***")
        else:
            print("ACCOUNT TEMPORARILY LOCKED... KINDLY VISIT ANY BRANCH OF 3VERSE BANK OF AFRIKA TO REACTIVATE YOUR ACCOUNT...")
    

    #Airtime Processing For 9MOBILE
    elif select_network == "4":
        while tryCount < tryLimit:
            airtimeConfirmation = input("YOU ARE ABOUT TO RECHARGE $" + str(amount_to_recharge) + " ON YOUR 9MOBILE LINE " + str(phone_number) + " ENTER YOUR PIN TO CONTINUE...")
            tryCount += 1
            if airtimeConfirmation == str(passcode()):
                currentBalance - amount_to_recharge
                print("AIRTIME PURCHASE OF $" + str(amount_to_recharge) + " WAS SUCCESSFUL!")
                break
            else:
                print("*** Wrong Passcode...TRY AGAIN ***")
        else:
            print("ACCOUNT TEMPORARILY LOCKED... KINDLY VISIT ANY BRANCH OF 3VERSE BANK OF AFRIKA TO REACTIVATE YOUR ACCOUNT...")