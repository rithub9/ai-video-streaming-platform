from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {"message": "File uploaded successfully", "path": file_path}

@app.get("/optimize/{filename}")
def optimize_video(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    cap = cv2.VideoCapture(file_path)
    optimized_path = os.path.join(UPLOAD_FOLDER, "optimized_" + filename)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(optimized_path, fourcc, 20.0, (640,480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            out.write(frame)
        else:
            break

    cap.release()
    out.release()
    return {"message": "Video optimized", "optimized_path": optimized_path}
