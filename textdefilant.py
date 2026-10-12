import tkinter as tk
from tkinter import scrolledtext

def defiler_titre(label_titre, fenetre):
    texte_actuel = label_titre.cget("text")
    
    nouveau_texte = texte_actuel[1:] + texte_actuel[0]
    
    label_titre.config(text=nouveau_texte)
    
    fenetre.after(150, lambda: defiler_titre(label_titre, fenetre))

