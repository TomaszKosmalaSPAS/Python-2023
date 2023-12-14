#wczytaj przy użyciu `input` liczbę; wypisz sumę jej cyfr; jeśli podano błędne wejście,
# poproś jeszcze raz

suma = 0
while True:
    try:
        x = str(input("Podaj liczbe"))
        for c in x:
            suma += int(c)
        print(suma)
        if x == "":
            break
    except IndexError as e:
        print(e)
    except ValueError as e:
        print("In Value Error")
        print(e)
    except Exception as e:
        print("In Exception")
        print(e)
    else:
        break
    finally:
        print("Finally")