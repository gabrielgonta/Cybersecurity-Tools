#!/usr/bin/env python
import argparse
import scapy.all as scapy


def get_arguments():
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description="Network Scanner - Scannez et identifiez les appareils connectés sur un réseau local.")
    parser.add_argument(
        "-t", "--target", 
        dest="target", 
        help="Spécifiez une IP ou une plage d'adresses (ex : 192.168.1.1/24)",
        required=True
    )
    return parser.parse_args()


def scan(ip):
    # Création de la requête ARP
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Envoi de la requête et récupération des réponses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Extraction des résultats
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    # Affichage des résultats scannés
    print("IP\t\t\tMAC Address\n-------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


# Récupération des arguments
options = get_arguments()

# Exécution du scan et affichage des résultats
scan_result = scan(options.target)
print_result(scan_result)
