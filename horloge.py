import time
import os

# Insérer l'heure
heure_initiale = (16, 30, 0)

# Insérer l'heure de l'alarme
heure_alarme = (16, 30, 15)

def convertir_en_format_am_pm(heure, minute, seconde):
    # Convertir l'heure en format AM/PM
    am_pm = "AM" if heure < 12 else "PM"
    heure_am_pm = heure % 12 if heure % 12 != 0 else 12
    return heure_am_pm, minute, seconde, am_pm

def afficher_heure_et_alarme(heure_initiale, heure_alarme, format_heure):

    while True:
        heure, minute, seconde = heure_initiale

        # Conditions pour afficher le format de l'heure
        if format_heure == "24H":
            heure_actuelle = f"{heure:02d}:{minute:02d}:{seconde:02d}"
        elif format_heure == "AM/PM":
            heure_am_pm, minute_am_pm, seconde_am_pm, am_pm = convertir_en_format_am_pm(heure, minute, seconde)
            heure_actuelle = f"{heure_am_pm:02d}:{minute_am_pm:02d}:{seconde_am_pm:02d} {am_pm}"
        else:
            print("Format non valide")
            return
        # Efface la ligne précédente
        os.system('cls' if os.name == 'nt' else 'clear')
        # Imprime l'heure choisi
        print(f"{heure_actuelle}")

        # Vérifie l'heure de l'alarme
        if heure == heure_alarme[0] and minute == heure_alarme[1] and seconde == heure_alarme[2]:
            # Efface la ligne précédente
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Snoooz ! Snoooz !")

        # Condition heure/minute/seconde du temps actuel
        seconde += 1
        if seconde == 60:
            seconde = 0
            minute += 1
            if minute == 60:
                minute = 0
                heure += 1
                if heure == 24:
                    heure = 0

        # Mettre en pause pendant une seconde entre chaque seconde
        time.sleep(1)

        # Créez un nouveau tuple avec la nouvelle heure, minute et seconde
        heure_initiale = (heure, minute, seconde)

# Demande à l'utilisateur de choisir le format d'heure (en majuscule)
format_heure = input("Choisissez le format d'heure ('24H' ou 'AM/PM') : ").upper()

# Lance la fonction d'affichage de l'heure et de l'alarme
afficher_heure_et_alarme(heure_initiale, heure_alarme, format_heure)