import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("traffic_log.csv")

print(f"\nTotal packets captured: {len(df)}")
print(f"\nProtocol breakdown:\n{df['protocol'].value_counts()}")
print(f"\nAnomalies detected:\n{df[df['anomaly'] != 'None']['anomaly'].value_counts()}")
print(f"\nTop 5 source IPs:\n{df['src_ip'].value_counts().head()}")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Network Traffic Analysis Report", fontsize=14, fontweight="bold")

# Chart 1 — Protocol distribution
df['protocol'].value_counts().plot(kind='bar', ax=axes[0], color=['#1A56A5','#2E8B57','#E07B39','#888'])
axes[0].set_title("Protocol Distribution")
axes[0].set_xlabel("Protocol")
axes[0].set_ylabel("Packet Count")
axes[0].tick_params(axis='x', rotation=0)

# Chart 2 — Anomaly types
anomalies = df[df['anomaly'] != 'None']['anomaly'].value_counts()
if not anomalies.empty:
    anomalies.plot(kind='bar', ax=axes[1], color='#C0392B')
else:
    axes[1].text(0.5, 0.5, 'No anomalies\ndetected', ha='center', va='center')
axes[1].set_title("Anomaly Types")
axes[1].set_xlabel("Type")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis='x', rotation=15)

# Chart 3 — Top 5 source IPs
df['src_ip'].value_counts().head(5).plot(kind='barh', ax=axes[2], color='#1A56A5')
axes[2].set_title("Top 5 Source IPs")
axes[2].set_xlabel("Packet Count")

plt.tight_layout()
plt.savefig("traffic_report.png", dpi=150)
plt.show()
print("\nReport saved as traffic_report.png")