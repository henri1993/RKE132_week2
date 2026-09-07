""" Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“ """

print("Tere tulemast programmi 'Tervitus!'")

name = input("Mis on sinu perekonnanimi? ")
sex = input("Mis on sinu sugu? (vali 'm' või 'n'): ")

if sex == "m":
    print(f"Tere, härra {name}!")
elif sex == "n":
    print(f"Tere, proua {name}!")
else:
    print(f"Tere tulemast, {name}! (sugu ei olegi tähtis).")