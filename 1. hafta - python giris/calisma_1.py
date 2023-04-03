def sırala(num):
    return num ** 2 - 20

liste = []
for i in range(5):
    num = int(input("Enter a number: "))
    liste.append(num)

print(liste)

liste.sort(key=sırala())

print("Numbers sorted by their squared values minus 20:")
print(liste)