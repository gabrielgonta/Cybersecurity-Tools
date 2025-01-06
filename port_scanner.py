import socket
from IPy import IP
import threading
import argparse

# Liste des ports et des bannières détectées
ports = []
banners = []


def get_arguments():
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description="Port Scanner - Scannez des ports sur une cible pour détecter des vulnérabilités potentielles.")
    parser.add_argument(
        "-t", "--target",
        dest="target",
        help="Spécifiez l'adresse IP ou le nom de domaine de la cible.",
        required=True
    )
    parser.add_argument(
        "-p", "--ports",
        dest="port_range",
        help="Spécifiez le nombre de ports à scanner (par défaut : 100).",
        type=int,
        default=100
    )
    return parser.parse_args()


def port_scanner(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            target_ip = IP(target)
        except ValueError:
            target_ip = socket.gethostbyname(target)

        s.connect((str(target_ip), port))
        try:
            banner_name = banner(s).decode(errors="ignore")
            ports.append(port)
            banners.append(banner_name.strip())
        except:
            pass
    except:
        pass
    finally:
        s.close()


def banner(s):
    return s.recv(1024)


def scan_ports(target, port_range):
    print(f"[INFO] Scanning {port_range} ports on {target}...")
    threads = []
    for port in range(1, port_range + 1):
        thread = threading.Thread(target=port_scanner, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("[INFO] Scan terminé. Recherche de vulnérabilités...")
    check_vulnerabilities()


def check_vulnerabilities():
    try:
        with open("vulnerable_banners.txt", "r") as file:
            data = file.read()
            for i in range(len(banners)):
                if banners[i] in data:
                    print(f"[!] Vulnérabilité trouvée : {banners[i]} sur le port {ports[i]}")
    except FileNotFoundError:
        print("[WARNING] Fichier 'vulnerable_banners.txt' non trouvé. Impossible de vérifier les vulnérabilités.")


# Récupération des arguments de la ligne de commande
options = get_arguments()

# Lancement du scanner
scan_ports(options.target, options.port_range)
