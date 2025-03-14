#1.Zadanie
# Rozwiń powyższy program pytając użytkownika
# o imie , nazwisko oraz wiek i wyswietlajac
# te inforamcje w nastepujacy sposob
#
# Imie: Jakub
# Nazwisko: Skrzypek
# Wiek: 23
# Status pełnoletnosci (pełnoletni/niepełnoletni)

name = input("Podaj swoje imie ")
age = input("Podaj swój wiek ")

print("Masz na imie " + name + " i masz " + age + " lat!")

if int(age)>=18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")