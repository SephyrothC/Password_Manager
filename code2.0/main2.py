import tkinter as tk
from tkinter import messagebox
from psw_check import *
from psw_generator import *


def password_checker(psw):
    # Votre code ici
    if check_psw_in_dataBase(psw):
        res = messagebox.askyesno(
            "Nouveau mot de passe", "Voulez-vous un nouveau mot de passe ?")
        if res:
            password_generator()
    elif check_password_in_Web(psw):
        res = messagebox.askyesno(
            "Nouveau mot de passe", "Voulez-vous un nouveau mot de passe ?")
        if res:
            password_generator()
    else:
        score = check_secure(psw)
        if score <= 50:
            messagebox.showinfo("Sécurité du mot de passe",
                                "Votre mot de passe est trop faible.")
            res = messagebox.askyesno(
                "Nouveau mot de passe", "Voulez-vous un nouveau mot de passe ?")
            if res:
                password_generator()
        elif score <= 80:
            messagebox.showinfo("Sécurité du mot de passe",
                                "Votre mot de passe est acceptable pour les comptes non sensibles.")
            res = messagebox.askyesno(
                "Nouveau mot de passe", "Voulez-vous un nouveau mot de passe ?")
            if res:
                password_generator()
        else:
            messagebox.showinfo("Sécurité du mot de passe",
                                "Votre mot de passe est fort.")


def check_password():
    password = password_entry.get()
    password_checker(password)


def generate_password():
    password_generator()


def transform_sentence():
    sentence = sentence_entry.get()
    santence_tranformation(sentence)


root = tk.Tk()

password_entry = tk.Entry(root)
password_entry.pack()
check_button = tk.Button(
    root, text="Vérifier la sécurité du mot de passe", command=check_password)
check_button.pack()

generate_button = tk.Button(
    root, text="Générer un mot de passe", command=generate_password)
generate_button.pack()

sentence_entry = tk.Entry(root)
sentence_entry.pack()
transform_button = tk.Button(
    root, text="Transformer la phrase en mot de passe", command=transform_sentence)
transform_button.pack()

root.mainloop()
