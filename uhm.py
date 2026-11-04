print("Vad heter folket? ")
namn=str(input("Ange namn: "))
print(f"Tjena {namn} hoppas du förlorar")

import random
tal=random.randint(1,10)


for i in range(3,0,-1):
    try:
        giss=int(input("Ange gissning: "))
        if giss==tal:
            print("Du hade rätt")
            break
        else:
            if i == 1:
                print("Du dog")
            else:
                print(f"Du hade fel, du har {i-1} gissningar kvar")
    except:
          print("Inte tillåtet tecken")
          break

