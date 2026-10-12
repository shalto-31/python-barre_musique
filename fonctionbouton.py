import pygame
import musique


def interrupteur_musique(bouton):
    """Lecture / pause / reprise de la musique."""

    # Première utilisation du bouton
    if not musique.musique_lancee:

        if not musique.initialiser_musique():
            return

        pygame.mixer.music.play()

        musique.musique_lancee = True
        musique.en_lecture = True

        bouton.config(text="⏸")

    # La musique est actuellement en train de jouer
    elif musique.en_lecture:

        pygame.mixer.music.pause()

        musique.en_lecture = False

        bouton.config(text="▶")

    # La musique est en pause
    else:

        pygame.mixer.music.unpause()

        musique.en_lecture = True

        bouton.config(text="⏸")



def musique_avant():
    if not musique.musique_lancee:

        if not musique.initialiser_musique():
            return
    elif musique.musique_actuelle > 0:
        musique.musique_actuelle -= 1
    else:
        musique.musique_actuelle = len(musique.fichiers) - 1

