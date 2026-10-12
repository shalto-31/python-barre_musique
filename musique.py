import os
import pygame

DOSSIER_MUSIQUE = "./musique"

# État de la musique
musique_lancee = False
en_lecture = False
musique_actuelle = 0

# Liste des fichiers disponibles
fichiers = [
    f for f in os.listdir(DOSSIER_MUSIQUE)
    if f.lower().endswith((".mp3", ".wav", ".ogg"))
]


def initialiser_musique():
    """Initialise pygame et charge le premier morceau."""
    global musique_lancee

    if not fichiers:
        print("Aucun fichier audio trouvé.")
        return False

    pygame.mixer.init()


    chemin = os.path.join(DOSSIER_MUSIQUE, fichiers[musique_actuelle])
    pygame.mixer.music.load(chemin)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

    musique_lancee = False

    return True