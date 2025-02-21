import tkinter as tk
from tkinter import messagebox

# Fonction pour gérer les clics des boutons
def bouton_click(chiffre):
    entree.insert(tk.END, chiffre)

# Fonction pour évaluer l'expression
def evaluer():
    try:
        resultat = eval(entree.get())
        entree.delete(0, tk.END)
        entree.insert(0, str(resultat))
    except Exception as e:
        messagebox.showerror("Erreur", "Expression invalide")

# Fonction pour effacer le champ
def effacer():
    entree.delete(0, tk.END)

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice Tkinter")
fenetre.geometry("300x400")

# Champ d'affichage de la calculatrice
entree = tk.Entry(fenetre, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entree.pack(fill=tk.BOTH, padx=10, pady=10)

# Liste des boutons
boutons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Création des boutons
for ligne in boutons:
    frame = tk.Frame(fenetre)
    frame.pack(expand=True, fill='both')
    for bouton in ligne:
        action = lambda x=bouton: bouton_click(x) if x not in ('=',) else evaluer()
        b = tk.Button(frame, text=bouton, font=("Arial", 18), command=action)
        b.pack(side='left', expand=True, fill='both')

# Bouton d'effacement
frame_effacer = tk.Frame(fenetre)
frame_effacer.pack(expand=True, fill='both')
btn_effacer = tk.Button(frame_effacer, text="C", font=("Arial", 18), bg="red", fg="white", command=effacer)
btn_effacer.pack(side='left', expand=True, fill='both')

# Exécution de la boucle principale
fenetre.mainloop()