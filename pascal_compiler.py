import os, sys, subprocess, re
from pascal_error_displayer import *


def check_error_message(message: str):
    """Vérifie si le dernier message enregistré dans le fichier texte est identique à celui actuel.
    Si c'est le cas, il arrête le programme et affiche le message d'erreur original"""

    if not os.path.exists("./last_error.txt"):
        save_error_message("")

    with open("./last_error.txt", "r", encoding="UTF-8") as file:
        if file.read() == message:
            print("Vous avez compilé 2 fois le meme programme d'affilé. Affichage du message original\n\n"
                  f"{message}")
            exit(1)


def save_error_message(message: str):
    """Écrit dans un fichier le message d'erreur"""

    with open("./last_error.txt", "w", encoding="UTF-8") as file:
        file.write(message)


args = sys.argv

program_executable = f'{args[args.index("-p") + 1]}.exe'

program_pascal = f'{args[args.index("-p") + 1]}.pas'

file_path = args[args.index("-c") + 1]

result = subprocess.check_output('tasklist', text=True)

if file_path == ".":
    print("Le fichier que vous essayez de compiler n'est pas enregistré\n"
          "Faites Ctrl+S pour l'enregistrer puis réessayez")
    exit(1)


for line in result.splitlines():
    if program_executable.lower() in line.lower():
        parts = line.split()
        process_name = parts[0]
        process_pid = int(parts[1].strip())
        print(f'Processus {process_name} (PID {process_pid}) est en cours d\'exécution. Fermeture en cours.')
        subprocess.call(f"taskkill /F /PID {process_pid}")
        

process = subprocess.Popen(f"fpc \"{file_path}\\{program_pascal}\" -FE\"{file_path}\"",
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

if process.returncode == 0:
    print("\n\n\n"
          "Compilation réussie ! Appuyez sur Ctrl + Maj + T pour lancer le programme\n\n")
    
else:

    print(f"\nSi ce message ne s'affiche pas correctement, relance la compilation 2 fois d'affilé pour "
          f"afficher le message original\n\n")

    print("La compilation a échoué. Erreurs de compilation :\n")

    if f"Fatal: Cannot open file \"{program_pascal}\"" in stdout:
        print("Free pascal n'as pas pu ouvrir votre fichier\n"
              "Faites attention ! Le nom du fichier ne doit pas contenir d'espace ni de point virgule!\n")
        exit(1)

    check_error_message(stdout)
    save_error_message(stdout)

    error_lines = [i.removeprefix(program_pascal) for i in stdout.splitlines() if i.startswith(program_pascal) and not
                   i.lower().endswith("errors compiling module, stopping")]

    for error in error_lines:
        print(Error(error))

    exit(1)


################################
##   Crée par Téo Landsmann   ##
################################
