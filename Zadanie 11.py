#11 Stwórz grę , w której wylosujesz liczbę z przedziłau 1 - 100 zapiszesz tę liczbę do zmiennej , a następnie poprosisz użytkownika o odgadnięice tej liczby . Po każdej próbie wyświetalj informacje , czy liczba podana przez uzytkownik jest mniejsz czy większ od wylosowanej

#Gdy użytkownik odgadnie liczbe , ukończ gre

import random

print("Witaj w grze! Odgadnij liczbę z przedziału 1 - 100.")

# Losowanie liczby
wylosowana = random.randint(1, 100)

while True:
    try:
        los = int(input("Podaj liczbę: "))  # Pobranie liczby od użytkownika
    except ValueError:
        print("To nie jest liczba! Spróbuj ponownie.")
        continue  # Powrót do początku pętli

    if los < wylosowana:
        print("Za mało! Spróbuj większej liczby.")
    elif los > wylosowana:
        print("Za dużo! Spróbuj mniejszej liczby.")
    else:
        print(f"🎉 Brawo! Odgadłeś liczbę: {wylosowana}")
        break  # Koniec gry
