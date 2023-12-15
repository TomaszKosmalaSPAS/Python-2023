range(10) #generator

list(range(10)) #lista uzupełniona generatorem

(x * x for x in range(10)) #generator
[x * x for x in range(10)] #lista uzupełniona generatorem

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0] #TYLKO PARZYSTE

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(10)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0} #tworzenie z generatora słownika

