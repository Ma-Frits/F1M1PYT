import datetime

def start():
    print ("Hello you!, ik ben Frits")
    naam = input ("Wie ben jij?")
    print("hallo: " + naam)

    print("Het is momenteel")
    x = datetime.datetime.now()

    print(x)
    
    print("Vraag1: Heb ik een huisdier?")
    eeen = input ("type A voor nee, B voor kat of C voor hond")

    if eeen.lower() == "b":
        print("Dat klopt")
    else:
      print("nee het antwoord was B")

    print("vraag2: heb ik broers of zussen")
    tweee = input ("type A voor nee, B voor zus en C voor broer")

    if tweee.lower() == "c":
        print("dat klopt")
    else:
        print("nee het antwoord was C")

    print(naam + " wil je dit opnieuw doen?")
    antwoord = input ("type een Y of een N:")

    if antwoord.lower() == "y":
        start()
    else:
        print("tot ziens")
        exit()

start()