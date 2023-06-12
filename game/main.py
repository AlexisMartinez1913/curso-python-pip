#juego piedra papel o tijera en python
import random

#funcion para que el usuario elija opciones
def choose_option():
    options = ('piedra', 'papel', 'tijera')  #tupla opciones
    user_option = input('piedra, papel o tijera: ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('Opcion no valida.')
    #continue
        return None, None

    computerOption = random.choice(options)  #cargar la opcion del computer de la  tupla con random
    print('user eligio => ', user_option)
    print('computer eligio => ', computerOption)
    return user_option, computerOption

#function check rules

def check_rules(user_option,computerOption, userWins,computerWins ):
    
    if user_option == computerOption:
        print('EMPATE')
    elif user_option == 'piedra':
        if computerOption == 'tijera':
            print('Piedra gana a tijera')
            print('User gana')
            userWins +=1
        else:
        
            print('Papel gana a piedra')
            print('Computer gana')
            computerWins +=1
    elif user_option == 'papel':
        if computerOption == 'piedra':
        
            print('Papel gana a piedra')
            print('User gana')
            userWins+=1
        else:
            print('Tijera gana a papel')
            print('Computer gana')
            computerWins+=1
    elif user_option == 'tijera':
        if computerOption == 'papel':
            print('tijera gana a papel')
            print('User gana')
            userWins+=1
        else:
            print('Piedra gana a tijera')
            print('Computer gana')
            computerWins+=1
    return userWins, computerWins

#funcion desde donde corre el juego
def run_game():
    rounds = 1
    computerWins = 0
    userWins = 0
    
    while True:
        print('* ' *10)
        print('ROUND' , rounds)
        print('* ' *10)
        print('Score: ')
        print('computer wins: ', computerWins)
        print('User Wins: ', userWins)
        print('')
        rounds+=1
        user_option,computerOption= choose_option()
        userWins, computerWins = check_rules(user_option, computerOption,userWins,computerWins)
        if computerWins == 2:
            print('Gano el duelo el Computer')
            break
        if userWins == 2:
            print('¡Ganaste el duelo ¡User!')
            break


#llamada programa pppal
run_game()
