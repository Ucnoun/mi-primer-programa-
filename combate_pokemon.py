
pokemon_elegido = input("Contra que Pokemon quieres combatir? (Squirtle / Charmander / Bulbasur) : ")

vida_pikachu =100
vida_enemigo =0
ataque_pokemon =0

#Elegimos enemigo
if pokemon_elegido == "Squirtle" :
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander" :
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 10

elif pokemon_elegido == "Bulbasur" :
    vida_enemigo = 100
    nombre_pokemon = "Bulbasur"
    ataque_pokemon = 7

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input ("Que ataque vamos a usar? (Chispazo / Bola Voltio ) ")
    if ataque_elegido == "Chispazo" :
        vida_enemigo -=10

    elif ataque_elegido == "Bola Voltio" :
        vida_enemigo -= 15
        #Elegimos ataque

    print("La vida del {} es de  {} ".format(nombre_pokemon, vida_enemigo))

    print("Te hace un ataque de {} de dano {} " .format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("La vida de pikachu es de  {} ".format(vida_pikachu))


if vida_enemigo <= 0: print("Victoria eres un gran combatiente")
else:
    print("Derrota, sigue intentandolo")

print ("Combate finalizado")