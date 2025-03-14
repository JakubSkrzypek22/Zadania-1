#9 Napisz program który sprawdzi czy podane imie jest imieniem męskim czy żeńskim
# ( założ ze imiona żenskie kończą się na literę a)

print("Witaj w prostym programie sprawdzajacaym czy imie jest meskie czy żeńskie")

name = input("Podaj imię ! ")

for letter in name:
  if letter == name[-1]:


    if letter == 'a':
        print("Podane imie jest żeńskie")
    else:
        print("Podane imie jest męskie")