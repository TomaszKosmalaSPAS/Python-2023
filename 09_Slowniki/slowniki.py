s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s|s2

s|={'e':5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}

#- Dla listy napisów pobranej w pętli z wejścia wypisać słownik ilości wystąpień napisów
  #- np. dla `['Ala', 'ma' 'kota', 'kota']` wypisać `{'Ala': 1, 'ma': 1, ;'kota': 2}`

s = {}
while True:
    x = input("wpis")
    if x == "":
       break
    #print(s.(x))
    n = (s.get(x, 0))
    n += 1
    s[x] = n
    print(s)

from collections import Counter
Counter(lista)
Counter({'kota': 2, 'ALa': 1, 'ma': 1})



lista  = []
lista.append("ala2")
c = Counter(lista)
print(c)

c["ala2"]


#- Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
 # - np. dla `73` wypisać `siedemdziesiąt trzy`

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14:"czternaście", 15:"pietnascie", 16:"szesnaście",
          17: "siedemnascie", 18:"osiemnaście", 19:"dziewietnascie"}
dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści",
                   40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdziesiąt",
                 90: "dziewięćdziesiąt"}
setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta",
                   400: "czterysta", 500: "piecset", 600: "szescset", 700: "siedemset",
         800: "osiemset", 900: "dziewiecset"}
slownik = {}

n = int(input("wpisz liczbe:"))
napis = setki[n-n%100]
n%= 100
if n in range (11, 20):
    napis += nastki[n]
else:
    napis += dziesiatki[n-n%10] + " " + nazwy_jednosci[n%10]

print(napis)


