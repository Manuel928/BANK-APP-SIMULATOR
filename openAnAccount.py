from pincode import passcode
from generateAccountNumber import generate_Account_Number
from generateBVN import generate_bvn
from deposit import mainDeposit
from withdraw import mainWithdraw
from checkBalance import check_balance
from operations import operation
import time

#Account Opening Function / Collecting User Data
def open_an_account():
    print("A message from the Chief Executive Officer (CEO)\n")
    print("WELCOME TO 3VERSE BANK OF AFRIKA\n" + "We are glad that you've taken this bold step to register an account with us.\n We know you believe in us, and that's why we'll continually provide high quality bank services\n for the people of Nigeria and africa at large...")
    print("Kindly fill out this form to open an account: \n")
    fName = input("ENTER YOUR FIRST NAME: ")
    lName = input("ENTER YOUR LAST NAME: ")
    oName = input("OTHER NAMES: ")
    email = input("ENTER YOUR EMAIL: ")
    dateOfBirth = input("(DD/MM/YY): ")
    NIN = int(input("PLEASE ENTER YOUR 11 DIGITS NIN NUMBER (NOTE THAT WE WILL VERIFY YOUR ID AFTER SUBMITTING THIS FORM!): "))
    bvn = input("ENTER YOUR BVN, IF YOU DON'T HAVE ANY ENTER 'NO': \n\n")
    if bvn == "No".lower():
        print("VERIFYING NIN --/|----/|--")
        time.sleep(4)

        print("NIN VERIFIED")
        print("*******************")

        print("YOUR NEW ACCOUNT NUMBER WOULD BE GENERATED NOW...\n")
        print("GENERATING --/|----/|--")
        print("*******************")

        time.sleep(4) #account number generation time of 4 seconds....

        generate_Account_Number() #generating account number
        print("ALL DATA SAVED SUCCESSFULLY!!!\n")
        print("YOU'LL BE NOTIFIED VIA " + email + " WHEN YOUR BVN IS READY\n")
        print("THANKS FOR BANKING WITH US!!!")
        print("HERE ARE THE OPERATIONS YOU CAN PERFORM: \n")
        
        operationOnAccount = input("Select from the options below: \n" +

                                   "1.DEPOSIT " +
                                   "2.WITHDRAW " +
                                   "3.CHECK BALANCE " +
                                   "4.OPEN AN ACCOUNT " +
                                   "5.BUY AIRTIME \n >>: ")

        if operationOnAccount == "1":
            mainDeposit()
        elif operationOnAccount == "2":
            mainWithdraw()
        elif operationOnAccount == "3":
            print("check balance time")
        elif operationOnAccount == "4":
            open_an_account()
        elif operationOnAccount == "5":
            print("buy airtime time")
        else:
            print("Invalid Selection... Please choose a valid operation to perform: ")
            operation()
