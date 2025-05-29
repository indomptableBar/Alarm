#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpiozero import MotionSensor
from datetime import datetime
from signal import pause

# Définition de la broche GPIO du capteur PIR
SENSOR_PIN = 23

# Fichier de log
LOG_FILE = '/home/pi/detection_mouvement/motion_log.txt'  # Chemin modifiable selon ton besoin

# Fonction exécutée lors d'une détection
def my_callback():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Mouvement détecté à {}".format(now))
    try:
        with open(LOG_FILE, 'a') as log:
            log.write("Mouvement détecté à {}\n".format(now))
    except IOError as e:
        print("Erreur d'écriture dans le fichier : {}".format(e))

# Initialisation du capteur de mouvement
pir = MotionSensor(SENSOR_PIN)

# Lier la fonction callback au mouvement détecté
pir.when_motion = my_callback

# Message de démarrage
print("Détection de mouvement active. Appuyez sur Ctrl+C pour quitter.")

# Boucle principale pour garder le script en attente
try:
    pause()
except KeyboardInterrupt:
    print("Arrêt du programme.")
