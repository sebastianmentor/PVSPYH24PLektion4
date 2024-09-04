shoppinglista = []

while True:
    vara = input('Skriv in vara: ')
    # shoppinglista.append(vara)
    antal = input('Hur många behövs: ')

    orderrad = [vara,antal]

    shoppinglista.append(orderrad)

    är_klar = input('Är shoppinglistan klar?(y/n)')

    if är_klar.lower() == 'y':
        break

antal = 1
print('##################')
print('Id |Vara    |Antal')
print('##################')
for orderrad in shoppinglista:
    print(f'{antal:<3}|{orderrad[0]:<8}|{orderrad[1]:<3}|')
    antal = antal + 1
    # antal += 1

antal = 1
print('##################')
print('Id |Vara    |Antal')
print('##################')
for vara, hur_många in shoppinglista:
    print(f'{antal:<3}|{vara:<8}|{hur_många:<3}|')
    antal = antal + 1
    # antal += 1

# print('While loppen är klar och programmet fortsätter!!!!')
