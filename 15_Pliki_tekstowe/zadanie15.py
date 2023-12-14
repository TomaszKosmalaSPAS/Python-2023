#- Stwórz czytnik plików CSV bez użycia modułu CSV
  #- napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
  #- wypisze jego zawartość oddzielając pola tabulacją `\t`

import os
print(os.getcwd())

first_line = None
data = []
with open('data/foods.csv') as f:
    for l in f:
        if first_line is None:
            first_line = l.strip().split(',')
        else:
            dane = l.strip().split(',')

            slownik = dict(zip(first_line, dane))
            print(slownik)