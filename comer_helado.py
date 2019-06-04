
apetece_helado_input = input( "te apetece un helado ? (Si/No): ").upper()

if apetece_helado_input == "SI"
    apetece_helado = True
elif

tiene_dinero_input = input("tiene dinero suficiente? (Si/No) : ").upper()
esta_el_senor_de_los_helados_input = input("Esta el senor de los helados? (Si/No) : ").upper()
esta_tu_tia_input = input("estas con tu tia? (Si/No) : ").upper()

apetece_helado = apetece_helado_input == "Si"
puede_permitirselo = tiene_dinero_input == "Si" or esta_el_senor_de_los_helados_input == "Si"
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_input == "Si"

if apetece_helado and puede_permitirselo and esta_el_senor_de_los_helados:
    print("Esta bien")
else:
    print("Pues no comas")


