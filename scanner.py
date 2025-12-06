import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        sock.connect((host, port))
        return True
    except:
        return False
    finally:
        sock.close()


def scan_range(host, start_port, end_port):
    print(f"\n[*] Scanning {host} from {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[+] Port {port} is OPEN")
    print("\n[+] Scan completed.\n")


if __name__ == "__main__":
    target = input("Enter target host (IP or domain): ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    scan_range(target, start, end)
