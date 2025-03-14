#4 Napisz program któyr zapyta uzytkowinika o wynik na egzaminie (od 0 do 100) i  wyswietli odpowiednia ocene:
#90-100 -> 5
#80-89 -> 4
#70-79 -> 3
#60-69 -> 2
#poniżej 60 -> 1

print("Witaj w prostym programie który pyta uzytkowinika o wynik na egzaminie (od 0 do 100) i  wyswietli odpowiednia ocene")

exam = input("Podaj ilość punktów która zdobyłeś na egzaminie ")

if int(exam) >= 90:
    print("Brawo otrzymałeś 5 !")
elif int(exam) >= 80:
    print("Brawo otrzymałeś 4 !")
elif int(exam) >= 70:
    print("Brawo otrzymałeś 3 !")
elif int(exam) >= 60:
    print("Brawo otrzymałeś 2 !")
else:
    print("Przykro mi otrzymałes ocene niedostateczna ( Banie) ! ")