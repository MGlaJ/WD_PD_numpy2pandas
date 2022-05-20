# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

import numpy as np

# m1 = np.array([2, 4, 6])
# m2 = np.array([3, 5, 7])
# print(m1*m2)


# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

# m3 = np.array([0, 2, 5, 1, 4, 7, 3, 6, 8]).reshape(3, 3)
# m4 = np.array([2, 7, 5, 11, 8, 15, 7, 6, 10, 13, 3, 9, 4, 19, 6, 12]).reshape(4, 4)
#
# print(m3)
# print(m4)
#
# print(m3.min(axis=0))
# print(m3.min(axis=1))
# print(m4.min(axis=0))
# print(m4.min(axis=1))


# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.

# m1 = np.array([2, 4, 6])
# m2 = np.array([3, 5, 7])
# print(m1.dot(m2))

# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga
# liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

# m5 = np.array([2, 5, 8])
# m6 = np.array([3.14, 7/8, 12.5])
# print(m5*m6)

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i
# zapisz do zmiennej “a”.

# m7 = np.array([2, 1.75, 4, 1.01, 8, 3.14]).reshape(2, 3)
# a = np.sin(m7)


# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej
# wartości i zapisz do zmiennej “b”.

# m8 = np.array([7, 6.5, 8, 10, 1.1, 1.75]).reshape(2, 3)
# b = np.cos(m8)


# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

# def dodawanie(a, b):
#     print(a+b)
#
# dodawanie(a,b)


# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

# m9 = np.arange(9).reshape(3, 3)
# print(m9)
#
# for x in m9.flat:
#     print(x)



# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia”
# macierzy. (użyj funkcji flat())

# m10 = np.arange(9).reshape(3, 3)
# for y in m10.flat:
#     print(y)

# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

# m11 = np.arange(81).reshape(9, 9)
# print(m11)
# m12 = m11.reshape(3, 27)
# print(m12)
# m13 = m11.reshape(27, 3)
# print(m13)

# po wymnożeniu wymiarów macierzy musimy uzyskać wyjściową liczbę elementów tj. 81
# możliwe wymiary macierzy to 3x27, 27x3, 1x81 i 81x1


# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób
# jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
# m14 = np.arange(12).reshape(3,4)
# m15 = m14.reshape(4, 3)
# m16 = m14.reshape(2, 6)
# print(m14.flat)
# print(m15.flat)
# print(m16.flat)

########

# Zadanie 1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

import pandas as pd
 pd.ExcelFile('imiona.xlsx')

# Zadanie 2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# • tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# • tylko rekordy gdzie nadane imię jest takie jak Twoje
# • sumę wszystkich urodzonych dzieci w całym danym okresie,
# • sumę dzieci urodzonych w latach 2000-2005
# • sumę urodzonych chłopców i dziewczynek,
# • najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# • najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,



# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
# • listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z
# DataFrame)
# • 5 najwyższych wartości zamówień
# • ilość zamówień złożonych przez każdego sprzedawcę
# • sumę zamówień dla każdego kraju
# • sumę zamówień dla roku 2005, dla sprzedawców z Polski
# • średnią kwotę zamówienia w 2004 roku,
# • zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku
# zamówienia_2005.csv

#####################################

# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

# Zadanie 2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

# Zadanie 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5
# latach z datasetu.

# Zadanie 4
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych
# sprzedawców (zbiór danych zamówienia.csv).




