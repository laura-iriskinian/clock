from datetime import datetime, timedelta
import time

#Saisie de l'alarme
set_time = input("Que souhaitez-vous faire ? : Afficher l'heure (H), régler l'heure (R) ou mettre une alarme (A) ?")

#Boucle de l'affichage de l'heure
if set_time == "H":
    while True :
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        time.sleep(1)

        print(f'\r{current_time}', end="\r")
    
elif set_time == "R":
    new_time_input = (input(f"saisissez l'heure au format HH:MM:SS :"))
    try:
        # Convertir l'entrée utilisateur en un objet datetime
        new_time = datetime.strptime(new_time_input, "%H:%M:%S")
    except ValueError:
        print("Format invalide. Assurez-vous d'utiliser HH:MM:SS.")
        exit()
    while True:   
        current_time = new_time.strftime('%H:%M:%S')  
        print(f'\r{current_time}', end="\r")
        time.sleep(1)
        new_time += timedelta(seconds=1)
    
elif set_time == "A":
    alarm = input("Saisissez l'heure à laquelle l'alarme doit sonner au format HH:MM:SS : ")
    while True : 
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        time.sleep(1)
        print(f'\r{current_time}', end="\r")
        if current_time == alarm:
            print("\n L'alarme a sonné !")
            break