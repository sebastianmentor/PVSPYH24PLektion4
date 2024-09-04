favoriträtter = ['pankaka', 'pizza', 'hamburgare', 'tacos']

DAGAR_PÅ_ETT_ÅR = 365
SEBASTIANS_BABBEL = 'Bla bla blaa blaaa'

run_program = True
print('Hej och välkommen till Sebastians lustiga lektion!')
while run_program:
    print('1. Gå på lunch')
    print('2. Ta rast')
    print('3. Gå hem')
    print('4. Lyssna på Sebastians babbel')
    print('5. Avsluta programmet')

    meny_val = input('Vänligen gör ett val från ovanstående meny:')

    if meny_val == '1':
        print('Vad tänkte du äta?')
        lunch = input(': ')
        if lunch.lower() in favoriträtter:
            print('Bra val! Jag är avundsjuk på dig!')
        else:
            print('Kul för dig men jag skulle inte välja det!')

    elif meny_val == '2':
        hur_lång_rast = input('Hur lång rast vill vi ta? Svara i minuter: ')
        # 89
        # -20
        # 0
        # 2.5
        # öalsdkasfdölfasdjlö


    elif meny_val == '3':
        pass
    elif meny_val == '4':
        print(SEBASTIANS_BABBEL)
    elif meny_val == '5':
        break
        # run_program = False
    else:
        print('Hoppa katten på tangenbordet eller??? Ogiltligt val!!!!!')
    # finns ingen kod här
    # print('*'*20)
    # print('Vi har nått slutet av vårat Kodblock!')
    # print('*'*20)
