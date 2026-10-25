"""Check whether a client's signal is strong enough."""

# Constants
RSSI_THRESHOLD_DBM = -70  # above this, roaming should start

# Variables
client_mac = "aa:bb:cc:dd:ee:ff"
client_rssi_dbm = -60

# Check the signal
if client_rssi_dbm < RSSI_THRESHOLD_DBM:
    print(f"{client_mac}: weak signal ({client_rssi_dbm} dBm), should roam")
else:
    print(f"{client_mac}: signal OK ({client_rssi_dbm} dBm)")