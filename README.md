# 🔒 Cybersecurity Tools - MAC Address Changer, Network Scanner, HTTP Sniffer & Port Scanner

## Description

Welcome to Cybersecurity Tools! 🎉
This repository contains four essential tools for cybersecurity enthusiasts and professionals:

- MAC Address Changer: Modify the MAC address of a network interface.
- Network Scanner: Discover devices on a local network by scanning a target IP or IP range.
- HTTP Sniffer: Capture HTTP traffic on a specified network interface and identify potential sensitive information such as usernames and passwords.
- Port Scanner: Scan open ports on a target and check for known vulnerabilities based on banners.

These tools are designed to assist in learning and exploring network security practices while maintaining ethical usage standards.

## Features

1. **MAC Address Changer**

✔ Quickly change the MAC address of any network interface.  
✔ Automate disabling and re-enabling of the specified interface.  
✔ Simple and lightweight, built with Python. 

2. **Network Scanner**

✔ Scan a target IP or range to identify connected devices.  
✔ Displays device IP and MAC address.  
✔ Built with the powerful `scapy` library for network packet manipulation.

3. **HTTP Sniffer**

✔ Capture HTTP requests on a specified network interface.  
✔ Display URLs visited by clients.  
✔ Identify potential sensitive information like usernames and passwords.  
✔ Lightweight and efficient.  

4. **Port Scanner**

✔ Scans open ports on a target IP or domain name.  
✔ Retrieves banners to identify potential vulnerabilities.  
✔ Compares banners against a database of known vulnerable services.  
✔ Multi-threaded for fast scanning.  

## Installation

Clone the repository :

```
git clone https://github.com/gabrielgonta/Cybersecurity-Tools.git
```

Navigate to the project directory :

```
cd Cybersecurity-Tools
```

Install dependencies :

```
pip install -r requirements.txt
```

## Usage

### 1. MAC Address Changer

1. Run the script:
Launch the MAC Address Changer with the desired interface and new MAC address :

```
python mac_changer.py -i <interface> -m <new_mac>
```

Example :

```
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

2. View help message:
To see all available options, use the -h flag:

```
python mac_changer.py -h
```

### 2. Network Scanner

1. Run the script:
Launch the Network Scanner with the target IP or range :

```
python network_scanner.py -t <target>
```

Example :

```
python network_scanner.py -t 192.168.1.0/24
```

2. View help message:
To see all available options, use the -h flag:

```
python network_scanner.py -h
```

### 3. HTTP Sniffer

1. Run the script:
Launch the HTTP Sniffer with the desired network interface :

```
python http_sniffer.py -i <interface>
```

Example :

```
python http_sniffer.py -i eth0
```

2. View help message:
To see all available options, use the -h flag:

```
python http_sniffer.py -h
```

### 4. Port Scanner

1. Run the script:
Launch the Port Scanner with the desired target and port range :

```
python port_scanner.py -t <target> -p <number_of_ports>
```

Example :

```
python port_scanner.py -t 192.168.1.1 -p 200
```

2. View help message:
To see all available options, use the -h flag:

```
python port_scanner.py -h
```

3. Detected Vulnerabilities :
If any banner matches a known vulnerability in vulnerable_banners.txt, it will be displayed with the port number.

## Purpose and Ethical Use

These tools are intended for educational purposes and for security professionals to test and configure their systems securely. 
Unauthorized or malicious use is strictly prohibited. Ensure you have proper authorization before using any of these tools.

## Authors

* **Gabriel Gonta** - *Initial work* - [Cybersecurity Tools](https://github.com/gabrielgonta/Cybersecurity-Tools.git)