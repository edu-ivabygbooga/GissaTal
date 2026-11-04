print("Vad heter folket? ")
namn=str(input("Ange namn: "))
print(f"Tjena {namn} hoppas du förlorar")

import random

tal=random.randint(1,10)
giss=int(input("Ange gissning: "))


if giss==tal:
    print("Du hade rätt")
else:
    print(f"Du hade fel det var {tal}")
    
#try, except