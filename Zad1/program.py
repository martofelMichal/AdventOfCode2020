f = open("lista.txt", "r")
lista = []
drugaLista = []
trzeciaLista = []

for x in f:
    lista.append(int(x))

print("START")
for x in lista:
    for n in lista:
        if x + n == 2020:
            drugaLista.append(x)
            drugaLista.append(n)


for x in lista:
    for n in lista:
        for i in lista:
            if x + n + i == 2020:
                trzeciaLista.append(x)
                trzeciaLista.append(n)
                trzeciaLista.append(i)

print("CZESC 1 ")
print("SUMA")
print(drugaLista[0], " + ", drugaLista[1], " = ",drugaLista[0] + drugaLista[1])
print("ILOCZYN")
print(drugaLista[0], " * ", drugaLista[1], " = ",drugaLista[0] * drugaLista[1])

print("CZESC 2 ")
print("SUMA")
print(trzeciaLista[0], " + ", trzeciaLista[1], " + ", trzeciaLista[2] ," = ",trzeciaLista[0] + trzeciaLista[1] + trzeciaLista[2])
print("ILOCZYN")
print(trzeciaLista[0], " * ", trzeciaLista[1], " * ", trzeciaLista[2] ," = ",trzeciaLista[0] * trzeciaLista[1] * trzeciaLista[2])