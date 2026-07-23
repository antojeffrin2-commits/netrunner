import socket
import os
import tkinter as tk
import time
import random
from tkinter import ttk

port_names = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

# ================= COLOR PALETTE =================
BG        = "#050507"
PANEL_BG  = "#0a0a12"
GRID_LINE = "#141428"
CYAN      = "#00fff9"
CYAN_DIM  = "#0aa9a4"
MAGENTA   = "#ff00c8"
AMBER     = "#ffb000"
RED       = "#ff2951"
TEXT_MAIN = "#00fff9"
TEXT_DIM  = "#4d8b8a"

FONT_TITLE = ("Consolas", 26, "bold")
FONT_SUB   = ("Consolas", 10)
FONT_LABEL = ("Consolas", 12, "bold")
FONT_BODY  = ("Consolas", 10)
FONT_BTN   = ("Consolas", 13, "bold")

# ================= WINDOW =================
root = tk.Tk()
root.title(":: NETRUNNER // GRID SCANNER v2.0.77 ::")
root.geometry("1000x680")
root.configure(bg=BG)

# ================= FULLSCREEN =================
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# ================= BACKGROUND GRID CANVAS =================
bg_canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

def draw_grid(event=None):
    bg_canvas.delete("grid")
    w = bg_canvas.winfo_width()
    h = bg_canvas.winfo_height()
    step = 28
    for x in range(0, w, step):
        bg_canvas.create_line(x, 0, x, h, fill=GRID_LINE, tags="grid")
    for y in range(0, h, step):
        bg_canvas.create_line(0, y, w, y, fill=GRID_LINE, tags="grid")
    bg_canvas.tag_lower("grid")

bg_canvas.bind("<Configure>", draw_grid)

# ================= MAIN FRAME (sits above grid) =================
main_frame = tk.Frame(root, bg=BG)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

# ================= TITLE (glitch-layered) =================
title_frame = tk.Frame(main_frame, bg=BG)
title_frame.pack(pady=(18, 4))

title_shadow_m = tk.Label(title_frame, text="NETRUNNER // GRID SCANNER",
                           font=FONT_TITLE, fg=MAGENTA, bg=BG)
title_shadow_m.place(x=2, y=2)

title_shadow_c = tk.Label(title_frame, text="NETRUNNER // GRID SCANNER",
                           font=FONT_TITLE, fg=CYAN_DIM, bg=BG)
title_shadow_c.place(x=-2, y=-2)

title_main = tk.Label(title_frame, text="NETRUNNER // GRID SCANNER",
                       font=FONT_TITLE, fg=CYAN, bg=BG)
title_main.pack()

subtitle = tk.Label(main_frame, text="◤ UNAUTHORIZED NODE DISCOVERY PROTOCOL ◢  //  BUILD 2077.02",
                     font=FONT_SUB, fg=TEXT_DIM, bg=BG)
subtitle.pack(pady=(0, 4))

sep = tk.Frame(main_frame, bg=CYAN_DIM, height=1)
sep.pack(fill="x", padx=40, pady=(4, 14))

# ================= INPUT =================
input_frame = tk.Frame(main_frame, bg=BG)
input_frame.pack()

tk.Label(input_frame, text="▸ TARGET SUBNET",
         font=FONT_LABEL, fg=RED, bg=BG).pack(side="left", padx=(0, 8))

entry_wrap = tk.Frame(input_frame, bg=CYAN, padx=1, pady=1)
entry_wrap.pack(side="left")

ip_entry = tk.Entry(entry_wrap, width=25,
                     font=("Consolas", 12),
                     bg="#000000", fg=CYAN,
                     insertbackground=CYAN,
                     relief="flat")
ip_entry.pack(ipady=4, padx=1, pady=1)
ip_entry.insert(0, "192.168.1.")

status_dot = tk.Label(input_frame, text="●", font=("Consolas", 14),
                       fg=RED, bg=BG)
status_dot.pack(side="left", padx=(12, 0))
status_label = tk.Label(input_frame, text="IDLE", font=FONT_SUB,
                         fg=TEXT_DIM, bg=BG)
status_label.pack(side="left", padx=(4, 0))

# ================= PROGRESS BAR =================
style = ttk.Style()
style.theme_use("default")
style.configure("Cyber.Horizontal.TProgressbar",
                 troughcolor="#0a0a12",
                 background=CYAN,
                 bordercolor=CYAN_DIM,
                 lightcolor=CYAN,
                 darkcolor=MAGENTA,
                 thickness=10)

progress = ttk.Progressbar(main_frame, length=500,
                            style="Cyber.Horizontal.TProgressbar")
progress.pack(pady=12)

# ================= PANELS =================
content_frame = tk.Frame(main_frame, bg=BG)
content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 16))

def make_panel(parent, label_text, accent):
    """Bordered retro terminal panel with a header strip."""
    outer = tk.Frame(parent, bg=accent, padx=1, pady=1)
    header = tk.Frame(outer, bg=PANEL_BG)
    header.pack(fill="x")
    tk.Label(header, text=f"╔═ {label_text} ", font=FONT_LABEL,
             fg=accent, bg=PANEL_BG, anchor="w").pack(side="left", padx=6, pady=4)
    tk.Label(header, text="═══════════════════╗", font=FONT_LABEL,
             fg=accent, bg=PANEL_BG, anchor="e").pack(side="right", padx=6)
    body_wrap = tk.Frame(outer, bg=PANEL_BG)
    body_wrap.pack(fill="both", expand=True)
    return outer, body_wrap

left_outer, left_body = make_panel(content_frame, "SCAN LOG", CYAN)
left_outer.pack(side="left", fill="both", expand=True, padx=(0, 10))

output_box = tk.Text(left_body, bg="#000000", fg=CYAN,
                      insertbackground=CYAN,
                      font=FONT_BODY, bd=0, padx=10, pady=8,
                      selectbackground=MAGENTA)
output_box.pack(fill="both", expand=True)

right_outer, right_body = make_panel(content_frame, "SYSTEM STATUS", MAGENTA)
right_outer.pack(side="right", fill="both", expand=True, padx=(10, 0))

stats_box = tk.Text(right_body, bg="#000000", fg=AMBER,
                     font=FONT_BODY, bd=0, padx=10, pady=8,
                     selectbackground=CYAN)
stats_box.pack(fill="both", expand=True)

# color tags for the log
output_box.tag_config("ok", foreground=CYAN)
output_box.tag_config("warn", foreground=AMBER)
output_box.tag_config("err", foreground=RED)
output_box.tag_config("dim", foreground=TEXT_DIM)

# ================= TYPEWRITER EFFECT =================
def type_line(text, tag="ok"):
    output_box.insert(tk.END, "", tag)
    for char in text:
        output_box.insert(tk.END, char, tag)
        output_box.see(tk.END)
        output_box.update()
        time.sleep(0.004)
    output_box.insert(tk.END, "\n")
    output_box.see(tk.END)

# ================= CURSOR BLINK ON ENTRY LABEL =================
cursor_visible = True
def blink_cursor():
    global cursor_visible
    cursor_visible = not cursor_visible
    status_dot.config(fg=(CYAN if cursor_visible else RED) if status_label.cget("text") != "IDLE"
                       else (RED if cursor_visible else "#3a0d16"))
    root.after(500, blink_cursor)

# ================= PORT SCAN =================
def scan_ports(ip):
    open_ports = []
    for port in [21, 22, 80, 443]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((ip, port)) == 0:
            open_ports.append(f"{port}({port_names.get(port)})")
        sock.close()
    return open_ports

# ================= UPDATE STATS =================
def update_stats(active, total):
    stats_box.delete("1.0", tk.END)

    load = min(active * 7, 100)
    bar_len = 20
    filled = int(bar_len * load / 100)
    bar = "█" * filled + "░" * (bar_len - filled)

    stats_box.insert(tk.END, "╭─ NODE TELEMETRY ─────────╮\n\n")
    stats_box.insert(tk.END, f"  ACTIVE NODES   : {active}/{total}\n")
    stats_box.insert(tk.END, f"  NETWORK LOAD   : {load}%\n")
    stats_box.insert(tk.END, f"  [{bar}]\n\n")
    stats_box.insert(tk.END, f"  SECURITY GRID  : STABLE\n")
    stats_box.insert(tk.END, f"  ENCRYPTION     : AES-256\n\n")
    stats_box.insert(tk.END, "╰───────────────────────────╯\n\n")

    stats_box.insert(tk.END, "◤ ACTIVITY FEED ◢\n")
    for i in range(6):
        glitch = random.choice(["▓", "▒", "░", "█"])
        stats_box.insert(tk.END, (glitch * random.randint(3, 10)) + "\n")

# ================= SCAN =================
def scan_network():
    output_box.delete("1.0", tk.END)
    progress["value"] = 0
    status_label.config(text="SCANNING", fg=AMBER)

    ip_input = ip_entry.get()
    if not ip_input:
        type_line("> ERROR: NO TARGET SUBNET SPECIFIED", "err")
        status_label.config(text="ERROR", fg=RED)
        return

    type_line("> BOOTING GRID SCANNER...", "dim")
    type_line("> HANDSHAKE ESTABLISHED", "dim")
    type_line(f"> TARGET RANGE: {ip_input}0/24", "warn")
    type_line("> COMMENCING SWEEP...\n", "warn")

    active = 0
    total = 24

    for i in range(1, total + 1):
        ip = ip_input + str(i)

        type_line(f"> [{i:02}] PROBING {ip} ...", "dim")

        response = os.system(f"ping -n 1 -w 100 {ip} > nul")

        if response == 0:
            active += 1
            ports = scan_ports(ip)
            port_text = ", ".join(ports) if ports else "NONE"

            type_line(f"   └─ NODE ONLINE  → {ip}", "ok")
            type_line(f"   └─ OPEN PORTS   → {port_text}\n", "ok")

        progress["value"] = (i / total) * 100
        root.update()

    type_line(f"> SWEEP COMPLETE :: {active}/{total} NODES ACTIVE", "warn")
    update_stats(active, total)
    status_label.config(text="COMPLETE", fg=CYAN)

# ================= BUTTON (glow-frame style) =================
btn_wrap = tk.Frame(main_frame, bg=CYAN, padx=2, pady=2)
btn_wrap.pack(pady=(0, 18))

scan_btn = tk.Button(btn_wrap, text="▶  INITIATE SCAN",
                      command=scan_network,
                      bg="#000000", fg=CYAN,
                      activebackground=CYAN, activeforeground="#000000",
                      font=FONT_BTN, relief="flat", bd=0,
                      padx=24, pady=8, cursor="hand2")
scan_btn.pack()

def on_enter(e):
    scan_btn.config(bg=CYAN, fg="#000000")
def on_leave(e):
    scan_btn.config(bg="#000000", fg=CYAN)

scan_btn.bind("<Enter>", on_enter)
scan_btn.bind("<Leave>", on_leave)

blink_cursor()
draw_grid()

root.mainloop()