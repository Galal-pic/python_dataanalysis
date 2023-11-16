frinds = input('frinds:').split(',')
presents = input('presents:').split(',')
x = input('what is in his mind: ')
if x in presents:
    print(f'Oh {frinds[presents.index(x)]}, Thank you friend :)')