#  Basic Port Scanner

A beginner Python project that scans a target host for open and closed ports
using Python's built-in socket library.

## Features
- Scans common ports (HTTP, HTTPS, SSH, FTP) on any target host
- Identifies and labels open ports with their service name
- Counts total open and closed ports after scan
- 1-second timeout per port for fast scanning
- No external libraries needed — uses Python built-in `socket` only

## Tech Stack
- Python 3
- Socket module (built-in)

## How to Run

1. Clone the repository:
   git clone https://github.com/Lovish123-tech/Basic-Port_scanner.git

2. Navigate into the folder:
   cd Basic-Port_scanner

3. Run the script:
   python port_scanner.py

## Example Output

Scanning Target

Port 80 Is Open - HTTP
Port 443 Is Open - HTTPS
Port 22 Is Closed
Port 21 Is Closed
------------------SCAN COMPLETED------------------
OPEN PORTS:  2
CLOSE PORTS: 2

## Ports Scanned

| Port | Service |
|------|---------|
| 80   | HTTP    |
| 443  | HTTPS   |
| 22   | SSH     |
| 21   | FTP     |

## Author
Lovish 
GitHub: [@Lovish123-tech](https://github.com/Lovish123-tech)