import socket
import ipaddress


def scan_ports(target, start_port, end_port):
    """Scan a range of TCP ports on an IP address."""
    try:
        ipaddress.ip_address(target)
    except ValueError:
        print("Please enter a valid IPv4 or IPv6 address.")
        return

    print(f"\nScanning {target} from port {start_port} to {end_port}...")
    print("-" * 45)
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((target, port))

                if result == 0:
                    print(f"Port {port}: OPEN")
                    open_ports.append(port)
        except OSError as error:
            print(f"Could not check port {port}: {error}")

    print("-" * 45)
    print(f"Scan completed. Open ports found: {len(open_ports)}")
    if not open_ports:
        print("No open TCP ports were found in this range.")


def main():
    print("Python Network Port Scanner")
    print("Only scan systems you own or have explicit permission to test.\n")

    target = input("Target IP (use 127.0.0.1 for your own computer): ").strip()

    try:
        start_port = int(input("Starting port (1-65535): "))
        end_port = int(input("Ending port (1-65535): "))

        if not (1 <= start_port <= end_port <= 65535):
            print("Invalid port range. Use ports from 1 to 65535, with start <= end.")
            return

        scan_ports(target, start_port, end_port)

    except ValueError:
        print("Please enter valid whole-number port values.")


if __name__ == "__main__":
    main()
