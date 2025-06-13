import socket
import ipaddress

# Configuration
subnet = "192.168.1.0/24"  # ← uniquement ton IP
port = 80
timeout = 1.0

def scan_ip(ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((str(ip), port))
            if result == 0:
                print(f"[+] Hôte actif trouvé: {ip}:{port}")
            else:
                print(f"[-] {ip}:{port} fermé ou inactif")
    except Exception as e:
        print(f"[!] Erreur avec {ip}: {e}")

def main():
    print(f"[INFO] Début du scan sur {subnet} (port {port})")
    ip_net = ipaddress.ip_network(subnet, strict=False)
    for ip in ip_net.hosts():
        scan_ip(ip)

if __name__ == "__main__":
    main()
