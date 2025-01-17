from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def traffic_sniffer():
    print("\nStarting network traffic sniffer. Press Ctrl+C to stop...\n")
    sniff(prn=packet_callback)

