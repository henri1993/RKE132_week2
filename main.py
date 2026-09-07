""" day = input("Mis päev on homme? (tööpäev/puhkepäev):") 
if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus")
 """

""" print("Tere tulemast programmi 'Finantsnõustaja!'")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul praegu on? "))

if money < 2500:
    print("Sul pole veel piisavalt raha. Ole kannatalik ja kogu edasi.")
elif money == 2500:
    print("Palju õnne! Saad osta uue iPhone 17 Pro sularahas!")
else:
    print("Saad osta iPhone 17 Pro ja jääb veel raha üle!") """

goal = 10000
steps = int(input("Mitu sammu oled juba teinud?: "))

percent = (steps / goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi saavutanud!")