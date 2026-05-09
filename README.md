 Network Traffic Analyzer
Show Image
Show Image
Show Image
Show Image
A real-time network packet sniffer and traffic analyzer built with Scapy. Captures live packets, classifies them by protocol, detects anomalies, logs everything to CSV, and generates a visual analysis report.

Output Preview

After running analyze.py, a traffic_report.png is generated with 3 charts:

Protocol Distribution (TCP / UDP / ICMP / OTHER)
Anomaly Types detected
Top 5 Source IPs by packet count



 Features

 Live packet capture — sniffs up to 200 real IP packets from your network interface
 Protocol classification — categorizes each packet as TCP, UDP, ICMP, or OTHER
 Anomaly detection — flags large packets (>1400 bytes), sensitive port access (SSH/Telnet/RDP), and ICMP flood risk
 CSV logging — every packet saved with timestamp, IPs, ports, protocol, and anomaly flag
 Visual report — auto-generated 3-panel chart saved as traffic_report.png


Tech Stack
ToolPurposeScapyLow-level packet capture and parsingPandasCSV reading and data aggregationMatplotlibChart generationCSV / OSFile I/O and log management

 Getting Started
Prerequisites
bashpip install scapy pandas matplotlib
Run

 Must be run as Administrator (Windows) or with sudo (Linux/Mac) — Scapy requires raw socket access.

Terminal 1 — Start the sniffer:
bashpython sniffer.py
Browse the web for 30 seconds to generate traffic, then press Ctrl+C.
Terminal 2 — Analyze and visualize:
bashpython analyze.py

 Project Structure
network_traffic_analyzer/
│
├── sniffer.py          # Core packet capture and anomaly detection
├── analyze.py          # Data analysis and chart generation
├── traffic_log.csv     # Auto-generated: all captured packets
└── traffic_report.png  # Auto-generated: visual analysis report

Sample Output
Starting packet capture... Press Ctrl+C to stop.

[18:04:12] TCP   | 192.168.1.5     → 142.250.80.46  | len= 512 | None
[18:04:13] TCP   | 192.168.1.5     → 142.250.80.46  | len=1450 | Large Packet
[18:04:14] ICMP  | 192.168.1.1     → 192.168.1.5    | len=  84 | ICMP Flood Risk
[18:04:15] TCP   | 192.168.1.5     → 10.0.0.1       | len= 128 | Sensitive Port Access

Total packets captured: 200

Protocol breakdown:
TCP     142
UDP      38
ICMP     14
OTHER     6

Anomalies detected:
Large Packet            23
Sensitive Port Access    8
ICMP Flood Risk         14

 Future Improvements

 Real-time web dashboard with Flask
 Email alerts for critical anomalies
 GeoIP mapping of source/destination IPs
 Support for filtering by specific IP or port


License
MIT License — free to use, modify, and distribute.
