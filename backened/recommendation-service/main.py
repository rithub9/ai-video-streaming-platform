from fastapi import FastAPI
import random

app = FastAPI()

videos = [
    {"title": "AI in Healthcare", "category": "AI"},
    {"title": "DevOps Best Practices", "category": "DevOps"},
    {"title": "Python for Machine Learning", "category": "Python"},
]

@app.get("/recommend")
def recommend():
    return {"recommendation": random.choice(videos)}
