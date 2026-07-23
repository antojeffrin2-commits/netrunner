# netrunner
a network scanner i made for my college tech exhibition

netrunner is a simple network scanning tool built using Python.  
It scans a local subnet, detects active devices, and checks for open ports — all displayed through a custom terminal-style GUI.

This project was built as a way to learn how networking actually works under the hood, instead of just reading theory.

---

## Features

- Scans a subnet (e.g. `192.168.1.0/24`)
- Detects active devices using ping
- Checks common ports:
  - 21 (FTP)
  - 22 (SSH)
  - 80 (HTTP)
  - 443 (HTTPS)
- Real-time terminal-style output
- Progress bar for scan tracking
- System stats panel (active nodes, network load)
- Custom retro/cyberpunk UI built with Tkinter

---

## What I Learned

This project helped me understand:

- How devices communicate over a network
- What an IP address and subnet really mean
- How ping (ICMP) is used to detect live hosts
- How port scanning works using sockets
- The difference between:
  - a device being online
  - and a service actually running on a port
- Building GUI applications using Tkinter
- Structuring a project from scratch

---

## How It Works

1. You enter a subnet (example: `192.168.1.`)
2. The program loops through IPs in that range
3. Each IP is pinged to check if it's online
4. If a device responds:
   - It scans common ports using `socket.connect_ex()`
5. Results are displayed live in the UI

---

## How to Run

Make sure Python is installed.

```bash
python main.py
