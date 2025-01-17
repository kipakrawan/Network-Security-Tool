from scapy.all import sniff, IP

def detect_intrusion(packet):
    if IP in packet:
        if packet[IP].src == "192.168.1.100":  # Example rule
            print(f"Intrusion alert! Suspicious packet from {packet[IP].src}")

def intrusion_detection():
    print("\nStarting intrusion detection system. Press Ctrl+C to stop...\n")
    sniff(prn=detect_intrusion)

