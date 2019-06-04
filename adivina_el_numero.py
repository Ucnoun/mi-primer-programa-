number_to_guess = 2

user_number = int(input('adivina el numero: '))

if number_to_guess == user_number:
    print('has ganado en tu primer intento')
else:
    print('has perdido')

user_number = int(input('adivina el numero: '))

if number_to_guess == user_number:
    print('has ganado en tu segundo intento')
else:
    print('volviste a perder')

user_number = int(input('adivina el numero: '))

if number_to_guess == user_number:
    print('has ganado en tu tercer intento')
else:
    print('has perdido todos tus intentos')
