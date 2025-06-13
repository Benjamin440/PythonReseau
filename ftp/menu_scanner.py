import scanner_port
# ------------------- Programme principal -------------------
def scan():
    ip = input("Entrez l'adresse IP à scanner (par défaut 127.0.0.1): ") or "127.0.0.1"
    protocol = scanner_port.choose_protocol()

    while True:
        choice = scanner_port.menu()
        if choice == '1':
            port = int(input("Entrez le port à scanner: "))
            if protocol == "TCP":
                scanner_port.scan_tcp_port(ip, port)
            else:
                scanner_port.scan_udp_port(ip, port)
        elif choice == '2':
            start_port = int(input("Port de début: "))
            end_port = int(input("Port de fin: "))
            if protocol == "TCP":
                scanner_port.scan_tcp_ports(ip, start_port, end_port)
            else:
                scanner_port.scan_udp_ports(ip, start_port, end_port)
        elif choice == '3':
            if protocol == "TCP":
                scanner_port.scan_all_tcp_ports(ip)
            else:
                scanner_port.scan_all_udp_ports(ip)
        elif choice == '4':
            print("Fermeture du scanner.")
            break
        else:
            print("Choix invalide. Réessayez.")
