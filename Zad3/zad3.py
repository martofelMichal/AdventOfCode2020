f = open("lista2.txt","r")

lista = []
for x in f:
    lista.append(x.replace("\n",""))

# czesc1
def petelki(parametrRight):
    # listaO = []
    listaDrzew = []
    right = parametrRight
    for i in lista:
        if right > len(lista[0])-1:
            right = right - len(i)
        if i == "....#...##......##..#..#.#...#.":
            continue
        # if i[right] == ".":
        #     listaO.append("O")
        elif i[right] == "#":
            listaDrzew.append("X")
        right = right + parametrRight

    return len(listaDrzew)
#czesc 2, 1right 2 down
def petelki2(parametrRight):
    # listaO = []
    listaDrzew = []
    right = parametrRight

    for i in range(0,len(lista),2):
        if right > len(lista[0]) - 1:
            right = right - len(lista[i])
        if lista[i] == "....#...##......##..#..#.#...#.":
            continue
        # if lista[i][right] == ".":
        #     listaO.append("O")
        elif lista[i][right] == "#":
            listaDrzew.append("X")
            right = right + parametrRight

    return len(listaDrzew)

liczbaPierwsza = petelki(1)
liczbaDruga = petelki(3)
liczbaTrzecia = petelki(5)
liczbaCzwarta = petelki(7)
liczbaPiata = petelki2(1)

print(liczbaPierwsza, liczbaDruga, liczbaTrzecia, liczbaCzwarta, liczbaPiata)
print("WYNIK: ", liczbaPierwsza*liczbaDruga*liczbaTrzecia*liczbaCzwarta*liczbaPiata)