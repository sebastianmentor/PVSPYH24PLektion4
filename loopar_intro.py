# Skriv ut kvadraterna av alla ojämna tal mellan 0 och 100!
# for i in range(101):
#     if i % 2 != 0:
#         print(i**2)


# Skriv ut kvadraterna av alla ojämna tal mellan 0 och 100, samt 
# skriv ut kubiken av alla tal som är delbart med 3!
# for i in range(101):
#     if i % 2 != 0 and i % 3 == 0:
#         print('Kvadraten av', i, 'är', i**2, 'och kubiken är', i**3)

#     elif i % 3 == 0:
#         print('Kubiken är', i**3)

#     elif i % 2 != 0:
#         print('Kvadraten av', i, 'är', i**2)

# Version 2
# for i in range(101):
#     # kvadrat = None
#     # kubik = None
#     strängen = ''
#     if i % 2 != 0:
#         strängen = strängen + f'Kvadraten av talet är {i**2}.'
#         # kvadrat = 'Kvadraten av '+ str(i) + ' är ' + str(i**2)
#         # strängen += 'Kvadraten av '+ str(i) + ' är ' + str(i**2)
#         # kvadrat = f'Kvadraten av {i} är {i**2}')
#         # print('Kvadraten av', i, 'är', i**2, 'och kubiken är', i**3)

#     if i % 3 == 0:
#         strängen = strängen + f'Kubiken av talet är {i**3}.'
#         # kubik = 'Kubiken av '+ str(i) + ' är ' + str(i**3) 
#         # strängen += 'Kubiken av '+ str(i) + ' är ' + str(i**3) 
#         # print('Kubiken är', i**3)

#     if strängen != '':
#         print(strängen)
#     # print(kvadrat + kubik)

for i in range(101):
    if i % 2 != 0:
        print(f'Kvadraten av talet är {i**2}.')
    if i % 3 == 0:
        print(f'Kubiken av talet är {i**3}.')