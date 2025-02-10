from fastapi import FastAPI
import requests

app = FastAPI()

BACKEND_SERVICES = {
    "auth": "http://auth-service:8001",
    "video": "http://video-service:8002",
    "recommendation": "http://recommendation-service:8003",
}

@app.get("/{service}/{path:path}")
def proxy(service: str, path: str):
    if service not in BACKEND_SERVICES:
        return {"error": "Invalid service"}

    response = requests.get(f"{BACKEND_SERVICES[service]}/{path}")
    return response.json()
