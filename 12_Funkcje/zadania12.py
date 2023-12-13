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

def alphabet_range(start="A", end="Z", step=1):
    return [ chr(x) for x in range (ord(start), ord(end), step)]

alphabet_range("a", "f", 1)



*************
def choinka(poziom, separator=" ", znak="*"):
    S = separator
    G = znak


 for x in range(n)

     x = chr(ord('A'))
     litera = x + 1
     return litera
for i in range(n)
    chr(ord('A'))