from port_scanner import port_scanner
from traffic_sniffer import traffic_sniffer
from vulnerability_scanner import vulnerability_scanner
from intrusion_detection import intrusion_detection

def main_menu():
    while True:
        print("\nNetwork Security Toolkit")
        print("1. Port Scanner")
        print("2. Traffic Sniffer")
        print("3. Vulnerability Scanner")
        print("4. Intrusion Detection")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter the target IP address: ")
            ports = range(1, 1025)
            port_scanner(target, ports)
        elif choice == "2":
            traffic_sniffer()
        elif choice == "3":
            service = input("Enter the service name (e.g., ssh): ")
            version = input("Enter the service version (e.g., 2.0): ")
            vulnerability_scanner(service, version)
        elif choice == "4":
            intrusion_detection()
        elif choice == "5":
            print("Exiting... Stay safe!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

