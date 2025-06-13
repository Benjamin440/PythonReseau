import socket
import time
import datetime
import threading

def choose_protocol():
    print("=== Choix du protocole ===")
    print("1. TCP")
    print("2. UDP")
    choice = input("Choisissez le protocole (1-2): ")
    return "TCP" if choice == '1' else "UDP"


def menu():
    print("\n=== Menu Scanner ===")
    print("1. Scanner un port spécifique")
    print("2. Scanner une plage de ports")
    print("3. Scanner tous les ports simultanément")
    print("4. Quitter")
    choice = input("Choisissez une option (1-4): ")
    return choice


def log_scan_result(ip, port, status, elapsed_time, now, proto):
    with open(f'scan_log_{proto.lower()}.txt', 'a') as f:
        f.write(f"[{proto}] Port {port} sur {ip}: {status}\n")
        f.write(f"Temps écoulé: {elapsed_time:.2f} secondes\n")
        f.write(f"Date : {now.strftime('%A %d %B %y')} à {now.strftime('%H:%M:%S')}\n")
        f.write('+' + '-' * 26 + '+\n')
        f.write(f"| Port: {port:<5} | État: {status:<10} |\n")
        f.write('+' + '-' * 26 + '+\n\n')

# Scan de port spécifique

def scan_tcp_port(ip, port):
    now = datetime.datetime.now()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            status = "ouvert" if result == 0 else "fermé"
            print(f"[TCP] Port {port} est {status} sur {ip}")
    except socket.timeout:
        status = "timeout"
        print(f"[TCP] Port {port} → timeout (délai dépassé)")

    except socket.error:
        status = "erreur de connexion"
        print(f"[TCP] Erreur de connexion au port {port} sur {ip}")

    except KeyboardInterrupt:
        status = "interrompu par l'utilisateur"
        print("Scan interrompu par l'utilisateur.")

    except Exception as e:
        status = f"erreur ({e})"
        print(f"[TCP] Erreur sur le port {port}: {e}")
    log_scan_result(ip, port, status, 0, now, "TCP")  # On ne logge plus de temps individuel

#Scan de port en fonction d'un range de port

def scan_tcp_ports(ip, start_port, end_port):
    now = datetime.datetime.now()
    print("Date :", now.strftime('%A %d %B %y'))
    print("Horaire :", now.strftime('%H:%M:%S'))
    print(f"[TCP] Début du scan des ports {start_port} à {end_port}")
    start_time = time.time()
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_tcp_port, args=(ip, port)) # target permet de spécifier la fonction à exécuter dans le thread
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    elapsed_time = time.time() - start_time
    print(f"[TCP] Scan terminé en {elapsed_time:.2f} secondes.")

# scan de tout les ports en utilisant les threads


def scan_all_tcp_ports(ip):
    now = datetime.datetime.now()
    print("Date :", now.strftime('%A %d %B %y'))
    print("Horaire :", now.strftime('%H:%M:%S'))
    print("[TCP] Début du scan de tous les ports (1-1024)")
    start_time = time.time()
    threads = []
    for port in range(1, 65535):  # 1025 pour démo
        t = threading.Thread(target=scan_tcp_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    elapsed_time = time.time() - start_time
    print(f"[TCP] Scan de tous les ports terminé en {elapsed_time:.2f} secondes.")


# Scan de port spécifique UDP

def scan_udp_port(ip, port):
    now = datetime.datetime.now()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)  # Toujours mettre le timeout AVANT l’envoi
            s.sendto(b'\x00', (ip, port))  # Envoie un paquet non vide (important)

            try:
                s.recvfrom(1024)
                status = "ouvert"
            except socket.timeout:
                status = "aucune réponse (filtré ou fermé)"
            except ConnectionResetError:
                status = "fermé (réinitialisé par l’hôte)"
    except KeyboardInterrupt:
        status = "interrompu par l'utilisateur"
        print("Scan interrompu par l'utilisateur.")
    except socket.error as e:
        status = f"erreur de socket ({e})"
    except Exception as e:
        status = f"erreur ({e})"
    
    print(f"[UDP] Port {port} → {status}")
    log_scan_result(ip, port, status, 0, now, "UDP")


#Scan de port en fonction d'un range de port UDP


def scan_udp_ports(ip, start_port, end_port):
    now = datetime.datetime.now()
    print("Date :", now.strftime('%A %d %B %y'))
    print("Horaire :", now.strftime('%H:%M:%S'))
    print(f"[UDP] Début du scan des ports {start_port} à {end_port}")
    start_time = time.time()
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_udp_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    elapsed_time = time.time() - start_time
    print(f"[UDP] Scan terminé en {elapsed_time:.2f} secondes.")


# scan de tout les ports en utilisant les threads UDP


def scan_all_udp_ports(ip):
    now = datetime.datetime.now()
    print("Date :", now.strftime('%A %d %B %y'))
    print("Horaire :", now.strftime('%H:%M:%S'))
    print("[UDP] Début du scan de tous les ports (1-1024)")
    start_time = time.time()
    threads = []
    for port in range(1, 65535):
        t = threading.Thread(target=scan_udp_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    elapsed_time = time.time() - start_time
    print(f"[UDP] Scan de tous les ports terminé en {elapsed_time:.2f} secondes.")



