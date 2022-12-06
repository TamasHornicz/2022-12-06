import string
szoveg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
Lbetuk = []
Lszamok = []



#1
print("1. feladat")
print("Szöveg karaktereinek összege: ",len(szoveg))  #a space az karakter?



#2
print("2. feladat")
mondat = szoveg.count(".")
print("Ennyi mondat van benne", mondat)



#3
print("3. feladat")
uj_szo = szoveg.replace("Lorem", "LOREM")
print(uj_szo)



#4
print("4. feladat")
for betu in szoveg:
    if(betu.isalpha()):
        Lbetuk.append(betu)
    elif(betu.isalnum()):
        Lszamok.append(int(betu))

print("Számok:", Lszamok)



#5
print("5. feladat")
szerepel_e = str(input("Írja be a szavát: "))
if szerepel_e in szoveg:
    print("Szerepel benne")
    print("Ennyiszer szerepel benne:", szoveg.count(szerepel_e))
else:
    print("Nem szerepel benne")
