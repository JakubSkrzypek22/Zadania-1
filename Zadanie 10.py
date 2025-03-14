#10 Pobierz od użytkownik trzy liczby całkowite i uporzadkuj je w kolejnosc od najmniejsze do największej

# #1 Wersja próbna działa ale nie za dobrze
# print("Witaj w prostym programie porównującym liczby całkowite")
#
# pierwsza = input("Podaj pierwszą liczbe całkowita ")
# druga = input("Podaj pierwszą liczbe całkowita ")
# trzecia = input("Podaj pierwszą liczbe całkowita ")
#
# if pierwsza > druga and trzecia:
#     print(pierwsza + " > " + druga + " > " + trzecia)
# elif druga > pierwsza and  trzecia:
#     print(druga + " > " + pierwsza + " > " + trzecia)
# else:
#     print(trzecia + " > " + druga + " > " + pierwsza)

pierwsza = int(input("Podaj pierwsza liczbe całkowita "))
druga = int(input("Podaj druga liczbe całkowita "))
trzecia = int(input("Podaj trzecia liczbe całkowita "))

liczby = sorted([pierwsza,druga,trzecia])

print("Posortowane liczby", liczby)