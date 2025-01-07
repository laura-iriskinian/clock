from datetime import datetime, timedelta
import time
import keyboard

# ask the time format
hour_format = input("What time format would you want? \n12h: type '12'\n24h: type '24' \nYour choice: ")

# format check
if hour_format not in ["12", "24"]:
    print("Wrong format. The time will be set on 24h")
    hour_format = "24"

# Define print format
if hour_format == "12":
    time_format = "%I:%M:%S %p"  # Format 12h with AM/PM
else:
    time_format = "%H:%M:%S"  # Format 24h

#alarm choice
set_time = input("What would you like to do? \nPrint time (P) \nSet time (T) \nSet alarm (A) \nMake your choice: ")

#Boucle de l'affichage de l'heure
if set_time == "P":
    while True :
        now = datetime.now()
        current_time = now.strftime(time_format)
        print(f'\r{current_time}', end="\r")
        time.sleep(1)
        
elif set_time == "T":
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
