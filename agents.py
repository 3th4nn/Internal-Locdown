import requests

# --- PLUG IN YOUR VALUES ---
API_URL = "https://localhost:1337/api/v2"
USERNAME = "empireadmin"
PASSWORD = "Password123"
VERIFY_SSL = False  # Set False if self-signed cert

# --- LOGIN AND GET TOKEN ---
def get_token():
    r = requests.post(f"{API_URL}/admin/login", json={"username": USERNAME, "password": PASSWORD}, verify=VERIFY_SSL)
    r.raise_for_status()
    return r.json()["token"]

# --- GET AGENTS ---
def get_agents(token):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{API_URL}/agents", headers=headers, verify=VERIFY_SSL)
    r.raise_for_status()
    return r.json()["agents"]

# --- MAIN ---
def main():
    token = get_token()
    agents = get_agents(token)
    
    for agent in agents:
        print(f"Agent: {agent['name']} | Hostname: {agent['hostname']} | Username: {agent['username']}")

if __name__ == "__main__":
    main()
