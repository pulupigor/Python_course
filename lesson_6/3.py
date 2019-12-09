if input("Тварина літає? ")=='y':
    if input("Тварина має пір'я? ")=='y':
        print("Це пташка")
    elif input("Тварина є мишою? ")=='y':
        print("Це кажан")
    else:
        print("Це комаха")    
else: 
    if input("Тварина живе у воді? ")=='y':
        print("Це риба")
    elif input("Тварина має ноги? ")=='y':
        print("Це ссавець")
    else:
        print("Це змія") 