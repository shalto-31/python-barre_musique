import tkinter as tk
import pygame

import musique
from fonctionbouton import interrupteur_musique, musique_avant
from barre_cachee import activer_masquage
from bouton import bouton_pause, bouton_avant
from texte import texte


fenetre = tk.Tk()

fenetre.configure(bg="black")
fenetre.overrideredirect(True)
fenetre.attributes("-topmost", True)

activer_masquage(fenetre, 200, 50)

bouton_avant(fenetre, musique_avant)
bouton_pause(fenetre, interrupteur_musique)

texte(fenetre, musique.fichiers)


def verifier_fin_musique():
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            print("La musique est terminée !")

    fenetre.after(100, verifier_fin_musique)

fenetre.mainloop()