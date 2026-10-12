import tkinter as tk


def bouton_pause(fenetre, interrupteur_musique):

    bouton = tk.Button(
        fenetre,
        text="▶",
        font=("Arial", 12, "bold"),
        width=3,
        height=1,
        bg="#000000",
        fg="white",
        activebackground="#000000",
        activeforeground="white",
        bd=0,
        relief="flat",
        highlightthickness=0,
        padx=0,
        pady=0,
        cursor="hand2",
        command=lambda: interrupteur_musique(bouton)
    )

    bouton.pack(side="left")

    return bouton

def bouton_avant(fenetre, musique_avant):

    bouton = tk.Button(
        fenetre,
        text="<<",
        font=("Arial", 12, "bold"),
        width=3,
        height=1,
        bg="#000000",
        fg="white",
        activebackground="#000000",
        activeforeground="white",
        bd=0,
        relief="flat",
        highlightthickness=0,
        padx=0,
        pady=0,
        cursor="hand2",
        command=lambda: musique_avant()
    )

    bouton.pack(side="left")

    return bouton