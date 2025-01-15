print("¡Juguemos piedra, papel o tijera!: ")

player_1 = input("Jugador 1, ¿Cual es tu nombre?: ")
player_2 = input("Jugador 2, ¿Cual es tu nombre?: ")

player_choice = int(input(f"Hola {player_1} Elije entre piedra, papel o tijera:\n1.Piedra\n2.Papel\n3.Tijera"))
player_2_choice = int(input(f"Hola {player_2} Elije entre piedra, papel o tijera:\n1.Piedra\n2.Papel\n3.Tijera"))

if player_choice == 1 and player_2_choice == 3:
    print("Piedra gana a tijera!")
elif player_choice == 2 and player_2_choice == 1:
    print("Papel le gana a piedra!")
elif player_choice == 3 and player_2_choice == 2:    
    print("Tijera le gana a papel!")
else:
    print("¡Es un empate!")