from datetime import datetime, timedelta
import time

# Demander le format d'heure à l'utilisateur
hour_format = input("Choisissez le format d'heure : 12h ou 24h ? (Entrez 12 ou 24) : ")

# Vérification du format
if hour_format not in ["12", "24"]:
    print("Format invalide. Par défaut, le format 24h sera utilisé.")
    hour_format = "24"

# Définir le format d'affichage en fonction du choix
if hour_format == "12":
    time_format = "%I:%M:%S %p"  # Format 12h avec AM/PM
else:
    time_format = "%H:%M:%S"  # Format 24h

#Saisie de l'alarme
set_time = input("Que souhaitez-vous faire ? : Afficher l'heure (H), régler l'heure (R) ou mettre une alarme (A) ?")

#Indique si l'horloge est en pause
paused = False

#Bascule l'état de pause
def toggle_pause():
    global paused
    paused = not paused

#Boucle de l'affichage de l'heure
if set_time == "H":
    while True :
        if not paused:
            now = datetime.now()
            current_time = now.strftime(time_format)
            print(f'\r{current_time}', end="\r")
        time.sleep(1)
         # Vérifier si la touche 'p' est pressée
        if keyboard.is_pressed('p'):  # Appuyer sur 'p' pour basculer l'état
            toggle_pause()
            time.sleep(0.3)  # Petite pause pour éviter plusieurs bascules

elif set_time == "R":
    new_time_input = (input(f"saisissez l'heure au format HH:MM:SS :"))
    try:
        # Convertir l'entrée utilisateur en un objet datetime
        new_time = datetime.strptime(new_time_input, "%H:%M:%S")
    except ValueError:
        print("Format invalide. Assurez-vous d'utiliser HH:MM:SS.")
        exit()
    while True:   
        current_time = new_time.strftime(time_format)  
        print(f'\r{current_time}', end="\r")
        time.sleep(1)
        new_time += timedelta(seconds=1)
    
elif set_time == "A":
    alarm = input("Saisissez l'heure à laquelle l'alarme doit sonner au format HH:MM:SS : ")
    while True : 
        now = datetime.now()
        current_time = now.strftime(time_format)
        time.sleep(1)
        print(f'\r{current_time}', end="\r")
        if current_time == datetime.strptime(alarm, "%H:%M:%S").strftime(time_format):
            print("\n L'alarme a sonné !")
            break
