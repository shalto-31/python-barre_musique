def activer_masquage(fenetre, largeur, hauteur):

    y_visible = 0

    # On cache complètement la fenêtre
    y_cache = -(hauteur + 10)

    # Zone en haut de l'écran qui fait apparaître la barre
    zone_declenchement = 5

    barre_visible = False

    # Commence cachée
    fenetre.geometry(
        f"{largeur}x{hauteur}+0+{y_cache}"
    )

    fenetre.update_idletasks()

    def afficher():
        nonlocal barre_visible

        if not barre_visible:
            barre_visible = True

            fenetre.geometry(
                f"{largeur}x{hauteur}+0+{y_visible}"
            )

            fenetre.update_idletasks()

    def cacher():
        nonlocal barre_visible

        if barre_visible:
            barre_visible = False

            fenetre.geometry(
                f"{largeur}x{hauteur}+0+{y_cache}"
            )

            fenetre.update_idletasks()

    def verifier_souris():

        souris_x = fenetre.winfo_pointerx()
        souris_y = fenetre.winfo_pointery()

        if barre_visible:

            # La barre est visible :
            # on vérifie si la souris est encore dessus.
            sur_la_barre = (
                0 <= souris_y <= hauteur
            )

            if not sur_la_barre:
                cacher()

        else:

            # La barre est cachée :
            # on regarde si la souris arrive en haut.
            if souris_y <= zone_declenchement:
                afficher()

        fenetre.after(30, verifier_souris)

    verifier_souris()
