from scapy.all import sniff, IP, TCP, UDP, ICMP
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import os

LOG_FILE = "traffic_log.csv"

# Write CSV header if file doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "src_ip", "dst_ip", "protocol", "length", "src_port", "dst_port", "anomaly"])

def detect_anomaly(protocol, length, dst_port):
    if length > 1400:
        return "Large Packet"
    if dst_port in [22, 23, 3389]:
        return "Sensitive Port Access"
    if protocol == "ICMP":
        return "ICMP Flood Risk"
    return "None"

def process_packet(packet):
    if IP in packet:
        timestamp = datetime.now().strftime("%H:%M:%S")
        src_ip   = packet[IP].src
        dst_ip   = packet[IP].dst
        length   = len(packet)
        src_port = dst_port = 0

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "OTHER"

        anomaly = detect_anomaly(protocol, length, dst_port)

        print(f"[{timestamp}] {protocol:5} | {src_ip:15} → {dst_ip:15} | len={length:4} | {anomaly}")

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, src_ip, dst_ip, protocol, length, src_port, dst_port, anomaly])

print("Starting packet capture... Press Ctrl+C to stop.\n")
try:
    sniff(filter="ip", prn=process_packet, store=False, count=200)
except KeyboardInterrupt:
    print("\nCapture stopped.")