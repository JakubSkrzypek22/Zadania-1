#3.Napisz program , który sprawdza czy podana przez uzytkownika liczba jest
# wieksz od 0 czy tez mniejsza czy tez równa

print("Witaj w prostym programie sprawdzajacym czy podana przez uzytkowniak liczba jest wieksza , równa czyy też mniejsza od zera")

numbers = input("Podaj liczbe")

if int(numbers) > 0:
    print('Podana liczba jest większa od 0')
elif int(numbers) < 0:
    print('Podana liczba jest mniejsza od 0')
else:
    print('Podana liczba jest równa 0')