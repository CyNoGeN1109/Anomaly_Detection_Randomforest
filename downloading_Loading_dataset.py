import requests
import zipfile
import io
import numpy as np
import pandas as pd
from pathlib import Path


file_path = "KDD+.txt"

# -------------------------------
# Step 1: Download NSL-KDD Dataset (if needed)
# -------------------------------
url = "https://academy.hackthebox.com/storage/modules/292/KDD_dataset.zip"

if not Path(file_path).exists():
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(".")  # Extract dataset to current directory
    print("Dataset downloaded and extracted.")
else:
    print("Local dataset found. Skipping download.")


# -------------------------------
# Step 2: Load Dataset
# -------------------------------

# Column names for NSL-KDD dataset
columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
    'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
    'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
    'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'attack', 'level'
]

df = pd.read_csv(file_path, names=columns)

print("\nFirst 5 rows of dataset:")
print(df.head())