f = open("lista.txt", "r")
znaki = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','u','v','p','r','s','t','w','x','y','z','q']
# lista odczytana z pliku
lista = []
# lista dwuwymiarowa ktora posiada liczby odczytane z pliku
listaZLiczbami = []
# lista z poszukiwanymi literkami
listaZLiterkami = []
# lista ze stringiem w którym należy zliczyć literki
listaZeStringiem = []

for x in f:
    lista.append(x)

for word in lista:
    nowyString = ''
    for x in word:
        if x in znaki:
            listaZLiterkami.append(x)
            break;
        else:
            nowyString += x
        if x == " ":
            listaZLiczbami.append(nowyString.split('-'))


for word in lista:
    nowyString = ''
    for x in word[::-1]:
        nowyString += x
        if x == " ":
            listaZeStringiem.append(nowyString)
            break;

iloscWystepowan = []
for i in range(0,len(listaZeStringiem)):
    iloscWystepowan.append(listaZeStringiem[i].count(listaZLiterkami[i]))


count = 0
# 1CZESC rozwiazanie
# for i in range(0,len(listaZLiczbami)):
#     if iloscWystepowan[i] >= int(listaZLiczbami[i][0]) and iloscWystepowan[i] <= int(listaZLiczbami[i][1]):
#         print("----------")
#         print("W stringu: ", listaZeStringiem[i], " literka ", listaZLiterkami[i], " znajduje się ", iloscWystepowan[i])
#         print("Liczba ",iloscWystepowan[i], " jest pomiedzy ",listaZLiczbami[i][0], " a ", listaZLiczbami[i][1])
#         print("-----------")
#         count += 1

# print("Ilosc prawidłowych haseł CZ1:", count)

listaOdwroconaZeStringami = []
for i in listaZeStringiem:
    listaOdwroconaZeStringami.append(i[::-1].replace("\n",""))

print(listaOdwroconaZeStringami)

listaWygrana = []
# 2 CZESC rozwiazanie
for i in range(0,len(listaOdwroconaZeStringami)):
    if (listaZLiterkami[i] == listaOdwroconaZeStringami[i][int(listaZLiczbami[i][0])] and listaZLiterkami[i] != listaOdwroconaZeStringami[i][int(listaZLiczbami[i][1])]) or (listaZLiterkami[i] != listaOdwroconaZeStringami[i][int(listaZLiczbami[i][0])] and listaZLiterkami[i] == listaOdwroconaZeStringami[i][int(listaZLiczbami[i][1])]):
        print("----------")
        print("W stringu: ")
        print(listaOdwroconaZeStringami[i], " literka ", listaZLiterkami[i])
        print("1: ", listaZLiczbami[i][0], " 2: ", listaZLiczbami[i][1])
        print("Co to za literka: ", listaOdwroconaZeStringami[i][int(listaZLiczbami[i][0])])
        print("Co to za literka: ", listaOdwroconaZeStringami[i][int(listaZLiczbami[i][1])])
        print("-----------")
        listaWygrana.append(i)

print("Dlugosc2 ", len(listaWygrana))


