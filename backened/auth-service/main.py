from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import jwt

app = FastAPI()

SECRET_KEY = "supersecretkey"

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    token = jwt.encode({"user": user.username}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}

@app.get("/verify")
def verify_token(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"user": decoded["user"]}
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
