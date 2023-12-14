#Stworzyć *list comprehension* tupli składających się z w/w liczb całkowitych i
# ich reprezentacji jako napis
  #- np. `[(1, "1"), (2, "2")]`


[(x,str(x)) for x in range(10)]

#biorąc słownik `{"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400,
# "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}` stworzyć list comprehension nazw pojazdów cięższych niż 5000
  #- Nazwy podać dużymi literami (*uppercase*)

s = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
        "Motorcycle": 110}

for k in s.keys():
    print(k)
for k, v in s.items():
    print(k)
if v > 5000:
    print(k)
############

    s = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600,
                   "Bicycle": 7, "Motorcycle": 110}

    [x for x in s.keys() if s[x] > 5000]

lista = [x for x in s.keys() if s[x] < 5000]
lista.sort()
print(lista)


