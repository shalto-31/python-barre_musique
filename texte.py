from textdefilant import defiler_titre
import tkinter as tk

def texte(fenetre, fichiers):
    texte_initial = f"Piste : {fichiers[0]}          "


    label_titre = tk.Label(
        fenetre,
        text=texte_initial,
        font=("Arial", 11),
        anchor="w",
        bg="black",
        fg="white"
    )

    label_titre.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )


    defiler_titre(label_titre, fenetre)
