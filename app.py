from pincode import passcode
from afterLogin import after_login
from deposit import mainDeposit
from operations import operation
from withdraw import mainWithdraw
from checkBalance import check_balance
from openAnAccount import open_an_account
from buyAirtime import buy_airtime

print("<<<AUTOMATED TELLER MACHINE SIMULATOR>>>")

try:
    pin = int(input("Please enter your pincode: "))
    if pin == passcode():
        after_login()
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
            check_balance()
        elif operationOnAccount == "4":
            open_an_account()
        elif operationOnAccount == "5":
            buy_airtime()
        else:
            print("Invalid Selection... Please choose a valid operation to perform: ")
            operation()



except ValueError:
    print("*** Only numbers are allowed... TRY AGAIN *** ")

