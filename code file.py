def one_way():
    print("\n------------------------------------")
    depart = input("* Enter Departure Airport : ")
    arrival = input("* Enter Arrival Airport   : ")
    print("------------------------------------")
    deptim = input("* Enter Departure Date: ")
    print("------------------------------------")
    print("\nCABIN CLASS")
    print("-----------------")
    print("1.Economy")
    print("2.Premium Economy")
    print("3.Business")
    clss = int(input("Select the class: "))
    if clss==1:
        p=("Economy")
    elif clss ==2:
        p = ("Premium Economy")
    elif clss==3:
        p = ("Business")
    else:
        print("Something went wrong....")
    print("-------------------------")
    mem = int(input("Enter no.of adults  : "))
    chil = int(input("Enter no.of childs  : "))
    infants = int(input("Enter no.of infants : "))
    print("-------------------------")
    like1 = input("Do you like to see the details(y/n): ")
    if like1 == 'y' or like1 =='Y' or like1 =='yes' or like1 == 'YES':
        print("-------------------------------------------")
        print("FROM-->TO           : ", depart.upper(), "-->", arrival.upper())
        print("DEPART              : ", deptim)
        print("CLASS               : ", p)
        print("NO.OF.ADULT'S       : ", mem)
        print("NO.OF.CHILDREN      : ", chil)
        print("NO.OF.INFANTS       : ", infants)
        total = mem + chil +infants
        print("-------------------------------------------")
        print("TOTAL TICKETS       : ", total)
        cntimu = input("\nDo you like to continue: ")
        if cntimu == 'y' or cntimu == 'Y' or cntimu == 'yes' or cntimu == 'YES':
            print("Departure from", depart)
            fligth_details()
        else:
            print("Something went wrong")
            main()
    else:
        fligth_details()

def round_trip():
    print("----------------------------------")
    depart1= input("* Enter Departure Airport: ")
    arrival2 = input("* Enter Arrival Airport: ")
    print("------------------------------------")
    deptim1 = input("* Enter Departure Date(*//*) : ")
    arritim1 = input("* Enter Arrival Date(*//*)  : ")
    print("------------------------------------")
    print("\nCABIN CLASS")
    print("-----------------")
    print("1.Economy")
    print("2.Premium Economy")
    print("3.Business")
    clss = int(input("Select the class: "))
    if clss == 1:
        p = ("Economy")
    elif clss == 2:
        p = ("Premium Economy")
    elif clss == 3:
        p = ("Business")
    else:
        print("Something went wrong....")
    print("-------------------------")
    mem1 = int(input("Enter no.of adults  : "))
    chil1 = int(input("Enter no.of childs  : "))
    infants1 = int(input("Enter no.of infants : "))
    print("-------------------------")
    like1 = input("Do you like to see the details(y/n): ")
    if like1 == 'y' or like1 == 'Y' or like1 == 'yes' or like1 == 'YES':
        print("----------------------------------")
        print("FROM-->TO           : ", depart1.upper(), "-->", arrival2.upper())
        print("DEPART & ARRIVAL    : ", deptim1,"&",arritim1)
        print("CLASS               : ", p)
        print("NO.OF.ADULT'S       : ", mem1)
        print("NO.OF.CHILDREN      : ", chil1)
        print("NO.OF.INFANTS       : ", infants1)
        print("-------------------------------------------")
        total1=mem1+chil1+infants1
        print("Total Tickets       : ",total1)
        cntimu = input("\nDo you like to continue: ")
        if cntimu == 'y' or cntimu == 'Y' or cntimu == 'yes' or cntimu == 'YES':
            print("Departure from",depart1)
            fligth_details()
        else:
            print("Something went wrong")
            main()
    else:
        fligth_details()

def fligth_details():
    print("\nFlight type")
    print("------------")
    print("1.Non-Stop")
    print("2.One-Stop")
    stops = int(input("Enter the stops: "))
    if stops == 1:
        print("Departure Time")
        print("------------------------------------")
        print("1.Early Morning / (12AM-6AM)")
        print("2.Morning / (6AM-12PM)")
        print("3.Afternoon / (12PM-6PM)")
        print("4.Night / (6PM-MIDNIGHT)")
        print("------------------------------------")
        dep = int(input("Select the departure(1-4): "))
        if dep == 1 or dep ==2 or dep ==3 or dep ==4:
            non_stop_timings()
        else:
            print("Something went wrong....")
    elif stops ==2:
        print("No flights found! ")
        input("Press Enter to continue")
        fligth_details()

def non_stop_timings():
    print("------------------------------------")
    print("\nAvailable Air Lines ")
    print("------------------------------------")
    print("1.Vistara,Air Lines Available at:")
    print("22:30 to 23:55")
    print("1h 25m")
    amount()
    print("------------------------------------")
    print("2.Air India,Air Lines Available at:")
    print("20:10 to 21:40")
    print("1h 30m")
    amount()
    print("------------------------------------")
    print("3.IndiGo,Air Lines Available at:")
    print("06:20 to 07:45")
    print("2h 25m")
    amount()
    print("------------------------------------")
    print("4.Qatar Airway, Air Lines Available at:")
    print("19:20 to 20:55")
    print("1h 35m")
    amount()
    print("------------------------------------")
    non=int(input("\nSlect the Airlines: "))
    if non == 1 or non == 2 or non==3 or non==4:
        amount_details()
    else:
        print("We can't find any flight at that time.")
        print("Thank you.")
        main()

def amount():
    import random
    x = random.randint(1, 9)
    y = random.random()
    cards = [1, 2, 3, 4, 5]
    random.shuffle(cards)
    num = [str(i) for i in cards]
    x = "".join(num)
    print("Rs", x)

def amount_details():
    import random
    x = random.randint(1, 9)
    y = random.random()
    cards = [1, 2, 3, 4, 5]
    random.shuffle(cards)
    num = [str(i) for i in cards]
    x = "".join(num)
    print("\nAMOUNT PAYABLE amount is calculated by the all the Taxes,fees,Check-in Baggage and Cabin Baggage Amount")
    more=input("Do you like to know more about the Amount payable(y/n): ")
    if more == 'y':
        help_flight()
    else:
        print("Amount Payable: ",x)

def help_flight():
    print("\nA 'ONE-WAY' ticket for a journey can only be used to travel in one direction and not for returning.")
    print("\nA 'ROUND TRIP' ticket that allows a person to travel to one place and then return back to the place he or she left.")
    print("\nThe Amount Payable amount may be increase or decrease they depends on the offers by the company.")
    help = input("\nIs this useful to you(y/n): ")
    if help == 'y':
        input("\nThank you,Payment successfull")
    else:
        print("\nPlease contact with our custumer care.Thank you")
        input("")

def exit_flight():
    exit()

input("\nWELCOME TO 'FLIGHT BOOKING'")
def main():
    print("\nFLIGHT TRIP TYPE")
    print("----------")
    print("1.ONE-WAY")
    print("2.ROUND TRIP")
    print("3.HELP")
    print("4.EXIT")
    t = int(input("Which type do you want(1-4): "))
    if t==1:
        one_way()
    elif t == 2:
        round_trip()
    elif t == 3:
        help_flight()
    elif t == 4:
        exit_flight()
    else:
        print("Something Went Wrong......")
        exit()
main()