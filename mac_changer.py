#!/usr/bin/env python
import subprocess
import optparse

# Fonction pour changer l'adresse MAC
def change(interface, new_mac):
    print(f"[INFO] Désactivation de l'interface {interface}...")
    subprocess.call(["ifconfig", interface, "down"])
    
    print(f"[INFO] Changement de l'adresse MAC de {interface} en {new_mac}...")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    
    print(f"[INFO] Réactivation de l'interface {interface}...")
    subprocess.call(["ifconfig", interface, "up"])
    print(f"[SUCCESS] L'adresse MAC a été modifiée avec succès.")

# Configuration du parseur d'options
parser = optparse.OptionParser()

# Ajout des options
parser.add_option("-i", "--interface", dest="interface", help="Interface réseau à modifier (ex : eth0)")
parser.add_option("-m", "--new_mac", dest="new_mac", help="Nouvelle adresse MAC (ex : 00:11:22:33:44:55)")

# Analyse des arguments fournis
(options, arguments) = parser.parse_args()

# Vérification des arguments
if not options.interface:
    parser.error("[-] L'option -i ou --interface est obligatoire. Utilisez -h pour voir l'usage.")
if not options.new_mac:
    parser.error("[-] L'option -m ou --new_mac est obligatoire. Utilisez -h pour voir l'usage.")

# Exécution de la fonction de changement
change(options.interface, options.new_mac)
