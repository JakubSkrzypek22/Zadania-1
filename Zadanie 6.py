#Napisz program , który wyswietli wszystkie liczby pierwsze od 1 do 100
import a


for numbers in range(2,101):
    if all(numbers % i != 0 for i in range(2, int(numbers**0.5) + 1)):
        print(numbers, end=" ")