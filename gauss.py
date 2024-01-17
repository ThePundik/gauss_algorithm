import numpy as np

E = pow(np.e, -5)


def okresl_rozmiar():
    x = int(input("Podaj ilosc wierszy: "))
    y = int(input("Podaj ilosc kolumn: "))

    if x <= 0 or y <= 0:
        print("Ilosc wierszy i kolumn musi byc wieksza od 0")
        return -1
    elif x != y:
        print("Ilosc wierszy musi byc rowna ilosci kolumn")
        return -1
    else:
        return x


def wprowadz_dane(macierz, wektor_rozwiazan, rozmiar):
    for i in range(rozmiar):
        print(f"\n{i + 1} Rownanie:")
        for j in range(rozmiar + 1):
            if j < rozmiar:
                input_str = f"A[{i}][{j}]: "
                macierz[i][j] = float(input(input_str))
            if j == rozmiar:
                input_str = f"A[{i}][{j}]: "
                macierz[i][j] = float(input(input_str))
    for i in range(rozmiar):
        wektor_rozwiazan[i] = i


def wyswietl_macierz(macierz, rozmiar):
    szerokosc_kolumny = 12
    precyzja = 5

    for i in range(rozmiar):
        print("{:>{}}".format(f'x{i + 1}', szerokosc_kolumny), end="")
    print("{:>{}}".format('b', szerokosc_kolumny))

    for i in range(rozmiar):
        print()
        for j in range(rozmiar + 1):
            value = format(macierz[i][j], f".{precyzja}f").rstrip('0').rstrip('.')
            print("{:>{}}".format(value, szerokosc_kolumny), end="")

    print("\n")


def zamiana_k(macierz, wektor_rozwiazan, rozmiar, k1, k2):
    for i in range(rozmiar):
        temp = macierz[i][k1]
        macierz[i][k1] = macierz[i][k2]
        macierz[i][k2] = temp
    temp = wektor_rozwiazan[k1]
    wektor_rozwiazan[k1] = wektor_rozwiazan[k2]
    wektor_rozwiazan[k2] = temp


def zamiana_w(macierz, rozmiar, w1, w2):
    for i in range(rozmiar + 1):
        temp = macierz[w1][i]
        macierz[w1][i] = macierz[w2][i]
        macierz[w2][i] = temp


def czy_zero(in_val):
    return abs(in_val) < E


def krok(macierz, rozmiar, wk):
    for i in range(wk + 1, rozmiar):
        p = macierz[i][wk] / macierz[wk][wk]
        for j in range(wk, rozmiar + 1):
            macierz[i][j] -= p * macierz[wk][j]


def zeruj(macierz, rozmiar):
    for i in range(1, rozmiar):
        for j in range(rozmiar + 1):
            if czy_zero(macierz[i][j]):
                macierz[i][j] = 0


def postepowanie_odwrotne(macierz, wektor_rozwiazan, rozmiar):
    wynik = [0] * rozmiar
    wynik[rozmiar - 1] = macierz[rozmiar - 1][rozmiar] / macierz[rozmiar - 1][rozmiar - 1]

    for i in range(rozmiar - 2, -1, -1):
        suma = 0
        for j in range(i + 1, rozmiar):
            suma += wynik[j] * macierz[i][j]

        wynik[i] = (macierz[i][rozmiar] - suma) / macierz[i][i]

    for i in range(1, rozmiar):
        j = i
        while j > 0 and wektor_rozwiazan[j] < wektor_rozwiazan[j - 1]:
            wektor_rozwiazan[j], wektor_rozwiazan[j - 1] = wektor_rozwiazan[j - 1], wektor_rozwiazan[j]
            wynik[j], wynik[j - 1] = wynik[j - 1], wynik[j]
            j -= 1

    szerokosc_kolumny = 12
    precyzja = 4

    print("\nRozwiazanie Ukladu: ")
    for i in range(rozmiar):
        print("{:>{}}".format(f'x{i + 1}', szerokosc_kolumny), end="")
    print()

    for i in range(rozmiar):
        value = format(wynik[i], f".{precyzja}f").rstrip('0').rstrip('.')
        print("{:>{}}".format(value, szerokosc_kolumny), end="")

    print("\n")


def gauss_podstawowy(macierz, wektor_rozwiazan, rozmiar):
    print("\nGauss Podstawowy: ")
    for k in range(rozmiar - 1):
        if czy_zero(macierz[k][k]):
            print("Pojawilo sie a(kk) = 0. Macierz jest osobliwa oraz nie istnieje dokladnie 1 rozwiazanie.")
            print("Przerywanie programu.")
            return
        krok(macierz, rozmiar, k)

    zeruj(macierz, rozmiar)

    print("\nMacierz Uzupelniona: ")
    wyswietl_macierz(macierz, rozmiar)

    if macierz[rozmiar - 1][rozmiar - 1] == 0:
        if macierz[rozmiar - 1][rozmiar] != 0:
            print("Uklad sprzeczny, brak rozwiazan")
        else:
            print("Uklad nieoznaczony, nieskonczenie wiele rozwiazan")
        return

    postepowanie_odwrotne(macierz, wektor_rozwiazan, rozmiar)


def gauss_pelny(macierz, wektor_rozwiazan, rozmiar):
    print("\nGauss z Pelnym Wyborem Elementu Maksymalnego: ")
    for k in range(rozmiar - 1):
        kolumna = k
        wiersz = k
        maks = abs(macierz[k][k])
        for j in range(k, rozmiar):
            for i in range(k, rozmiar):
                if abs(macierz[j][i]) > maks:
                    maks = abs(macierz[j][i])
                    kolumna = i
                    wiersz = j


        if kolumna != k:
            zamiana_k(macierz, wektor_rozwiazan, rozmiar, kolumna, k)


        if wiersz != k:
            zamiana_w(macierz, rozmiar, wiersz, k)


        if czy_zero(macierz[k][k]):
            print("Pojawilo sie a(kk) = 0. Macierz jest osobliwa oraz nie istnieje dokladnie 1 rozwiazanie.")
            print("Przerywanie programu.")
            return

        krok(macierz, rozmiar, k)

    zeruj(macierz, rozmiar)

    print("\nMacierz Uzupelniona: ")
    wyswietl_macierz(macierz, rozmiar)

    if macierz[rozmiar - 1][rozmiar - 1] == 0:
        if macierz[rozmiar - 1][rozmiar] != 0:
            print("Uklad sprzeczny, brak rozwiazan")
        else:
            print("Uklad nieoznaczony, nieskonczenie wiele rozwiazan")
        return

    postepowanie_odwrotne(macierz, wektor_rozwiazan, rozmiar)


def menu():
    print("Proszę wybrac metode: ")
    print("1) Metoda Gaussa (Podstawowa)")
    print("2) Metoda Gaussa z pelnym wyborem elementu maksymalnego")
    wybor_metody = int(input("Wybor: "))
    print()

    print("Sposob testowania: ")
    print("1) Samodzielne wprowadzanie danych ")
    print("2) Testowanie danych zawartych w programie ")
    wybor_testowania = int(input("Wybor: "))
    print()

    if wybor_testowania == 1:

        rozmiar = okresl_rozmiar()
        if rozmiar == -1:
            return

        macierz = np.zeros((rozmiar, rozmiar + 1))
        wektor_rozwiazan = np.arange(rozmiar)

        wprowadz_dane(macierz, wektor_rozwiazan, rozmiar)

        print("\nWejsciowa Macierz: ")
        wyswietl_macierz(macierz, rozmiar)

        if wybor_metody == 1:
            gauss_podstawowy(macierz, wektor_rozwiazan, rozmiar)
        elif wybor_metody == 2:
            gauss_pelny(macierz, wektor_rozwiazan, rozmiar)
        else:
            print("Byl podany nie poprawny wybor. ")
            return

    elif wybor_testowania == 2:
        macierz = np.array([[1.0, -2.0, 0.0, 3.0, 1.0, 1.0],
                            [2.0, -3.0, 1.0, 8.0, 2.0, 3.0],
                            [1.0, -2.0, 1.0, 3.0, -1.0, 1.0],
                            [0.0, 1.0, 0.0, 3.0, 5.0, 0.0],
                            [1.0, -2.0, 0.0, 5.0, 8.0, -1.0]])

        wektor_rozwiazan = np.arange(len(macierz))
        rozmiar = len(wektor_rozwiazan)

        print("\nWejsciowa Macierz: ")
        wyswietl_macierz(macierz, rozmiar)

        if wybor_metody == 1:
            gauss_podstawowy(macierz, wektor_rozwiazan, rozmiar)
        elif wybor_metody == 2:
            gauss_pelny(macierz, wektor_rozwiazan, rozmiar)
        else:
            print("Byl podany nie poprawny wybor. ")
            return


menu()
