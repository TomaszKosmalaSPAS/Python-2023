#stworzyc słownik `{ 'first': funkcja1, 'second': funkcja2 }`, wczytać przez `input` klucz, wywołać funkcję

def funkcja1():
    print("wpisz1")
def funkcja2():
    print("wpisz2")

s = {'first': funkcja1, 'second':funkcja2}
def funkcja3():
    s = {'first': funkcja1, 'second':funkcja2}
    return s.get(funkcja3)

#- stworzyc funckcję `alphabet_range` działająca jak `range` ale dla liter (z trzema parametrami - `start`, `end`, `step`)
 # - przykład: `alphabet_range('E')` -> `['A', 'B', 'C', 'D']` - albo jeszcze lepiej generator
 # - użyć
  #  - `ord` - podaje kod calkowity danego znaku
  #  - `chr` - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range(start="A", end="z", step=1):
    return ( chr(x) for x in range (ord(start), ord(end), step))

alphabet_range("a", "f", 1)

list(alphabet_range(end='M'))




#- stworzyć funkcję `slownie_do999()` która zwróci słownie liczbę z zakresu 0-999
 # - stworzyć funkcję pomocniczą `_slownie_do999()` zwracającą listę tupli `(wartość, słownie)` dla 1 i "nastek" , 10, 100
 # - stworzyć funkcję pomocniczą `_sklej()` sklejającą w/w listę



def slownie_do999(n):
    nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                9: "dziewięć"}
    nazwy_nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "pietnascie",
              16: "szesnaście",
              17: "siedemnascie", 18: "osiemnaście", 19: "dziewietnascie"}
    nazwy_dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści",
                  40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt",
                  80: "osiemdziesiąt",
                  90: "dziewięćdziesiąt"}
    nazwy_setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta",
             400: "czterysta", 500: "piecset", 600: "szescset", 700: "siedemset",
             800: "osiemset", 900: "dziewiecset"}
    ret = []

    jednosci = n % 10
    dziesiatki = n % 100 - jednosci
    setki = n - dziesiatki - jednosci

    if setki:
        ret.append((setki, nazwy_setki[setki]))

    if dziesiatki == 10 and jednosci > 0:
        nastki = 10 + jednosci
        ret.append((nastki, nazwy_nastki[nastki]))
    else:
        if dziesiatki:
            ret.append((dziesiatki, nazwy_dziesiatki[dziesiatki]))
        if jednosci:
            ret.append((jednosci, nazwy_jednosci[jednosci]))

    return ret

def sklej(lista):
    return [t[1] for t in lista]


    print(_slownie999(3))
    print(_slownie999(13))
    print(_slownie999(33))
    print(_slownie999(133))
    print(_slownie999(313))
    print(_slownie999(310))
    assert _slownie999(313) == [(300, 'trzysta'), (13, 'trzynaście')]